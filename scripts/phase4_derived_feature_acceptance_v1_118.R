args<-commandArgs(trailingOnly=TRUE); dir<-args[1]; s<-read.csv(args[2],stringsAsFactors=FALSE);s<-s[s$season>=2016&s$season<=2024,];s$game_id<-as.character(s$game_id);s$start_date<-as.POSIXct(s$start_date,tz="UTC")
one<-function(v)!is.na(v)&v==1
samples<-list(); orders<-list(); ots<-list()
for(yr in 2016:2024){
 x<-readRDS(file.path(dir,sprintf("pbp_%d.rds",yr)));x$game_id<-as.character(x$game_id);x$.row<-seq_len(nrow(x))
 x<-x[x$game_id%in%s$game_id[s$season==yr],]
 # chronology: compare raw row first with numeric id_play first where possible
 dq<-!is.na(x$pos_team)&!is.na(x$drive_id)&!is.na(x$yards_to_goal)
 d<-x[dq,c("game_id","pos_team","drive_id","yards_to_goal","id_play",".row")]
 d$id_num<-suppressWarnings(as.numeric(as.character(d$id_play)))
 raw<-d[order(d$game_id,d$pos_team,d$drive_id,d$.row),];raw<-raw[!duplicated(raw[,c("game_id","pos_team","drive_id")]),]
 num<-d[!is.na(d$id_num),];num<-num[order(num$game_id,num$pos_team,num$drive_id,num$id_num,num$.row),];num<-num[!duplicated(num[,c("game_id","pos_team","drive_id")]),]
 m<-merge(raw,num,by=c("game_id","pos_team","drive_id"),suffixes=c("_raw","_id"))
 orders[[length(orders)+1]]<-data.frame(season=yr,drives=nrow(raw),id_comparable=nrow(m),different_start=sum(m$.row_raw!=m$.row_id),different_ytg=sum(m$yards_to_goal_raw!=m$yards_to_goal_id,na.rm=TRUE))
 # overtime semantic diagnostic, especially 2021+: identify periods >4 and scrimmage flags, two-point-like text/type
 scr<-(one(x$rush)|one(x$pass)|one(x$pass_attempt))&!one(x$punt)&!is.na(x$yards_gained)
 ot<-!is.na(x$period)&x$period>4
 txt<-tolower(ifelse(is.na(x$play_text),"",x$play_text)); typ<-tolower(ifelse(is.na(x$play_type),"",x$play_type))
 twopt<-grepl("two.point|2.point|two point",txt)|grepl("two.point|2.point|two point",typ)
 ots[[length(ots)+1]]<-data.frame(season=yr,ot_rows=sum(ot),ot_scrimmage=sum(ot&scr),ot_twopt_like=sum(ot&twopt),ot_twopt_like_scrimmage=sum(ot&twopt&scr),period7plus_scrimmage=sum(!is.na(x$period)&x$period>=7&scr))
 # independent direct recomputation for deterministic sample target rows at depths 1,5,8,12 when available
 sch<-s[s$season==yr,]
 teams<-sort(unique(c(x$pos_team,x$def_pos_team)));teams<-teams[!is.na(teams)]
 for(depth in c(1,5,8,12)){
   candidates<-list()
   for(tm in teams){
    games<-sch[sch$game_id%in%unique(x$game_id[x$pos_team==tm|x$def_pos_team==tm]),];games<-games[order(games$start_date,games$game_id),]
    if(nrow(games)>depth){ target<-games[depth+1,]; pri<-games$game_id[1:depth]
      xp<-x[x$game_id%in%pri,]
      os<-(xp$pos_team==tm)&(one(xp$rush)|one(xp$pass)|one(xp$pass_attempt))&!one(xp$punt)&!is.na(xp$yards_gained)
      ds<-(xp$def_pos_team==tm)&(one(xp$rush)|one(xp$pass)|one(xp$pass_attempt))&!one(xp$punt)&!is.na(xp$yards_gained)
      oq<-os&!is.na(xp$down)&!is.na(xp$distance)&xp$distance>0&xp$down%in%1:4
      dq2<-ds&!is.na(xp$down)&!is.na(xp$distance)&xp$distance>0&xp$down%in%1:4
      suc<-function(q) q&((xp$down==1&xp$yards_gained>=.5*xp$distance)|(xp$down==2&xp$yards_gained>=.7*xp$distance)|(xp$down%in%c(3,4)&xp$yards_gained>=xp$distance))
      drives<-xp[xp$pos_team==tm&!is.na(xp$drive_id)&!is.na(xp$yards_to_goal),c("game_id","drive_id","yards_to_goal",".row")]
      drives<-drives[order(drives$game_id,drives$drive_id,drives$.row),];drives<-drives[!duplicated(drives[,c("game_id","drive_id")]),]
      samples[[length(samples)+1]]<-data.frame(season=yr,team=tm,target_game=target$game_id,depth=depth,off_exp=sum(os&xp$yards_gained>=20)/sum(os),def_exp=sum(ds&xp$yards_gained>=20)/sum(ds),off_success=sum(suc(oq))/sum(oq),def_success=sum(suc(dq2))/sum(dq2),avg_start_ytg=mean(drives$yards_to_goal),off_den=sum(os),success_den=sum(oq),field_den=nrow(drives))
      break
    }
   }
 }
}
write.csv(do.call(rbind,samples),"phase4_derived_acceptance_samples_v1_118.csv",row.names=FALSE)
write.csv(do.call(rbind,orders),"phase4_field_position_order_audit_v1_118.csv",row.names=FALSE)
write.csv(do.call(rbind,ots),"phase4_overtime_semantics_audit_v1_118.csv",row.names=FALSE)
