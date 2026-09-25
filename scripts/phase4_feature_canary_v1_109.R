args <- commandArgs(trailingOnly=TRUE)
if(length(args)<2) stop("usage: Rscript phase4_feature_canary_v1_109.R <pbp_dir> <schedule_csv>")
pbp_dir<-args[1]; sched<-read.csv(args[2],stringsAsFactors=FALSE)
need<-c("season","game_id","start_date","home_team","away_team","home_points","away_points","neutral_site")
m<-setdiff(need,names(sched)); if(length(m)) stop(paste("schedule missing",paste(m,collapse=",")))
sched<-sched[sched$season>=2016&sched$season<=2024,,drop=FALSE]; if(any(sched$season==2025)) stop("2025 TEST leakage")
sched$game_id<-as.character(sched$game_id); sched$start_date<-as.POSIXct(sched$start_date,tz="UTC")
one<-function(v)!is.na(v)&v==1; parts<-list()
for(yr in 2016:2024){
 x<-readRDS(file.path(pbp_dir,sprintf("pbp_%d.rds",yr)))
 req<-c("game_id","pos_team","def_pos_team","rush","pass","pass_attempt","punt","yards_gained","interception_thrown_stat","interception_stat")
 mm<-setdiff(req,names(x)); if(length(mm)) stop(paste(yr,"missing",paste(mm,collapse=",")))
 x$game_id<-as.character(x$game_id); x<-x[x$game_id%in%sched$game_id[sched$season==yr],,drop=FALSE]
 sr<-(one(x$rush)|one(x$pass)|one(x$pass_attempt))&!one(x$punt); rr<-sr&one(x$rush); pr<-sr&(one(x$pass)|one(x$pass_attempt)); ints<-one(x$interception_thrown_stat)|one(x$interception_stat)
 y<-ifelse(is.na(x$yards_gained),0,x$yards_gained)
 key<-paste(x$game_id,x$pos_team,sep="|"); dkey<-paste(x$game_id,x$def_pos_team,sep="|")
 sumby<-function(v,k)tapply(v,k,sum,na.rm=TRUE)
 vals<-data.frame(key=names(sumby(sr,key)),off_plays=as.numeric(sumby(sr,key)),stringsAsFactors=FALSE)
 add<-function(n,v,k=key){q<-sumby(v,k); vals[[n]]<<-as.numeric(q[match(vals$key,names(q))]); vals[[n]][is.na(vals[[n]])]<<-0}
 add("off_yards",y*sr); add("rush_plays",rr); add("pass_plays",pr); add("rush_yards",y*rr); add("pass_yards",y*pr); add("pass_attempts",one(x$pass_attempt)); add("interceptions",ints)
 dv<-sumby(sr,dkey); dy<-sumby(y*sr,dkey)
 sp<-strsplit(vals$key,"|",fixed=TRUE); vals$game_id<-vapply(sp,`[`,"",1); vals$team<-vapply(sp,`[`,"",2)
 dk<-paste(vals$game_id,vals$team,sep="|"); vals$def_plays<-as.numeric(dv[dk]); vals$def_yards<-as.numeric(dy[dk]); vals$def_plays[is.na(vals$def_plays)]<-0; vals$def_yards[is.na(vals$def_yards)]<-0
 sg<-sched[sched$season==yr,,drop=FALSE]; vals<-merge(vals,sg,by="game_id",all.x=TRUE,sort=FALSE)
 vals$game_points_for<-ifelse(vals$team==vals$home_team,vals$home_points,vals$away_points); vals$game_points_against<-ifelse(vals$team==vals$home_team,vals$away_points,vals$home_points)
 vals$venue<-ifelse(vals$neutral_site,"NEUTRAL",ifelse(vals$team==vals$home_team,"HOME","AWAY")); vals$season<-yr
 parts[[length(parts)+1]]<-vals[,c("season","game_id","team","start_date","venue","game_points_for","game_points_against","off_plays","def_plays","off_yards","def_yards","rush_plays","pass_plays","rush_yards","pass_yards","pass_attempts","interceptions")]
}
tg<-do.call(rbind,parts); tg<-tg[order(tg$season,tg$team,tg$start_date,tg$game_id),]; safe<-function(n,d)ifelse(d==0,NA_real_,n/d); rows<-list()
for(yr in sort(unique(tg$season))) for(tm in unique(tg$team[tg$season==yr])){z<-tg[tg$season==yr & tg$team==tm,,drop=FALSE]; n<-nrow(z); prior_n<-0:(n-1); cs<-function(v)c(0,head(cumsum(v),-1))
 rows[[length(rows)+1]]<-data.frame(season=z$season,game_id=z$game_id,team=tm,start_date=z$start_date,home_away_neutral=z$venue,qualified_prior_games=prior_n,
 points_for_per_game=safe(cs(z$game_points_for),prior_n),points_against_per_game=safe(cs(z$game_points_against),prior_n),
 offensive_scrimmage_plays_per_game=safe(cs(z$off_plays),prior_n),defensive_scrimmage_plays_per_game=safe(cs(z$def_plays),prior_n),
 offensive_yards_per_play=safe(cs(z$off_yards),cs(z$off_plays)),defensive_yards_per_play=safe(cs(z$def_yards),cs(z$def_plays)),
 rush_play_rate=safe(cs(z$rush_plays),cs(z$off_plays)),pass_play_rate=safe(cs(z$pass_plays),cs(z$off_plays)),
 rush_yards_per_play=safe(cs(z$rush_yards),cs(z$rush_plays)),pass_yards_per_play=safe(cs(z$pass_yards),cs(z$pass_plays)),
 interception_rate=safe(cs(z$interceptions),cs(z$pass_attempts)),rest_days=c(NA,as.numeric(diff(z$start_date),units="days")))}
feat<-do.call(rbind,rows); if(any(feat$season==2025)) stop("2025 TEST leakage")
write.csv(tg,"phase4_team_game_mechanical_primitives_v1_109.csv",row.names=FALSE); write.csv(feat,"phase4_feature_canary_v1_109.csv",row.names=FALSE)
cat("rows",nrow(feat),"seasons",paste(sort(unique(feat$season)),collapse=","),"2025",sum(feat$season==2025),"\n")
