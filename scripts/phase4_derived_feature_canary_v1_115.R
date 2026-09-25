args<-commandArgs(trailingOnly=TRUE)
if(length(args)<2)stop("usage: Rscript phase4_derived_feature_canary_v1_115.R <pbp_dir> <schedule_csv>")
dir<-args[1]; s<-read.csv(args[2],stringsAsFactors=FALSE); s<-s[s$season>=2016&s$season<=2024,]; if(any(s$season==2025))stop("2025 TEST leakage")
s$game_id<-as.character(s$game_id); s$start_date<-as.POSIXct(s$start_date,tz="UTC")
one<-function(v)!is.na(v)&v==1; parts<-list()
for(yr in 2016:2024){
 x<-readRDS(file.path(dir,sprintf("pbp_%d.rds",yr))); x$game_id<-as.character(x$game_id)
 req<-c("game_id","pos_team","def_pos_team","rush","pass","pass_attempt","punt","yards_gained","down","distance","drive_id","yards_to_goal")
 m<-setdiff(req,names(x));if(length(m))stop(paste(yr,"missing",paste(m,collapse=",")))
 x<-x[x$game_id%in%s$game_id[s$season==yr],]
 scr<-(one(x$rush)|one(x$pass)|one(x$pass_attempt))&!one(x$punt)&!is.na(x$yards_gained)
 succq<-scr&!is.na(x$down)&!is.na(x$distance)&x$distance>0&x$down%in%1:4
 succ<-succq&((x$down==1&x$yards_gained>=.5*x$distance)|(x$down==2&x$yards_gained>=.7*x$distance)|(x$down%in%c(3,4)&x$yards_gained>=x$distance))
 key<-paste(x$game_id,x$pos_team,sep="|"); dkey<-paste(x$game_id,x$def_pos_team,sep="|")
 sumby<-function(v,k)tapply(v,k,sum,na.rm=TRUE)
 ks<-sort(unique(c(key[scr],dkey[scr]))); p<-data.frame(key=ks,stringsAsFactors=FALSE)
 add<-function(n,v,k=key){q<-sumby(v,k);p[[n]]<<-as.numeric(q[p$key]);p[[n]][is.na(p[[n]])]<<-0}
 add("off_scr",scr);add("off_exp",scr&x$yards_gained>=20);add("off_succ_q",succq);add("off_succ",succ)
 add("def_scr",scr,dkey);add("def_exp",scr&x$yards_gained>=20,dkey);add("def_succ_q",succq,dkey);add("def_succ",succ,dkey)
 sp<-strsplit(p$key,"|",fixed=TRUE);p$game_id<-vapply(sp,`[`,"",1);p$team<-vapply(sp,`[`,"",2)
 dq<-!is.na(x$pos_team)&!is.na(x$drive_id)&!is.na(x$yards_to_goal)
 dd<-data.frame(game_id=x$game_id[dq],team=x$pos_team[dq],drive_id=x$drive_id[dq],ytg=x$yards_to_goal[dq],ord=which(dq))
 dd<-dd[order(dd$game_id,dd$team,dd$drive_id,dd$ord),]; dd<-dd[!duplicated(dd[,c("game_id","team","drive_id")]),]
 fd<-aggregate(ytg~game_id+team,dd,function(v)c(sum=sum(v),n=length(v)))
 # aggregate matrix/list handling
 fsum<-aggregate(dd$ytg,list(game_id=dd$game_id,team=dd$team),sum); names(fsum)[3]<-"start_ytg_sum"
 fn<-aggregate(dd$ytg,list(game_id=dd$game_id,team=dd$team),length); names(fn)[3]<-"start_drive_n"
 p<-merge(p,fsum,by=c("game_id","team"),all.x=TRUE);p<-merge(p,fn,by=c("game_id","team"),all.x=TRUE)
 p$start_ytg_sum[is.na(p$start_ytg_sum)]<-0;p$start_drive_n[is.na(p$start_drive_n)]<-0
 p<-merge(p,s[s$season==yr,c("game_id","start_date")],by="game_id",all.x=TRUE);p$season<-yr;parts[[length(parts)+1]]<-p
}
g<-do.call(rbind,parts);g<-g[order(g$season,g$team,g$start_date,g$game_id),]
safe<-function(n,d)ifelse(d==0,NA_real_,n/d); rows<-list()
for(yr in sort(unique(g$season)))for(tm in unique(g$team[g$season==yr])){
 z<-g[g$season==yr&g$team==tm,];cs<-function(v)c(0,head(cumsum(v),-1));n<-nrow(z)
 rows[[length(rows)+1]]<-data.frame(season=yr,game_id=z$game_id,team=tm,start_date=z$start_date,qualified_prior_games=0:(n-1),
  offensive_explosive_play_rate=safe(cs(z$off_exp),cs(z$off_scr)),defensive_explosive_play_rate=safe(cs(z$def_exp),cs(z$def_scr)),
  offensive_success_rate=safe(cs(z$off_succ),cs(z$off_succ_q)),defensive_success_rate_allowed=safe(cs(z$def_succ),cs(z$def_succ_q)),
  average_starting_yards_to_goal=safe(cs(z$start_ytg_sum),cs(z$start_drive_n)),
  explosive_play_denominator=cs(z$off_scr),success_play_denominator=cs(z$off_succ_q),field_position_drive_denominator=cs(z$start_drive_n))}
}
out<-do.call(rbind,rows);if(any(out$season==2025))stop("2025 TEST leakage")
write.csv(g,"phase4_derived_team_game_primitives_v1_115.csv",row.names=FALSE);write.csv(out,"phase4_derived_feature_canary_v1_115.csv",row.names=FALSE)
cat("rows",nrow(out),"2025",sum(out$season==2025),"\n")
