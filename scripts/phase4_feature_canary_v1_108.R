args <- commandArgs(trailingOnly=TRUE)
if (length(args) < 2) stop("usage: Rscript phase4_feature_canary_v1_108.R <pbp_dir> <schedule_csv>")
pbp_dir <- args[1]; schedule_path <- args[2]
sched <- read.csv(schedule_path, stringsAsFactors=FALSE)
required_sched <- c("season","game_id","start_date","home_team","away_team","home_points","away_points")
miss <- setdiff(required_sched,names(sched)); if(length(miss)) stop(paste("schedule missing",paste(miss,collapse=",")))
sched <- sched[sched$season >= 2016 & sched$season <= 2024,,drop=FALSE]
if(any(sched$season==2025)) stop("2025 TEST leakage")
sched$game_id <- as.character(sched$game_id); sched$start_date <- as.POSIXct(sched$start_date,tz="UTC")
out <- list()
for (yr in 2016:2024) {
  p <- file.path(pbp_dir,sprintf("pbp_%d.rds",yr)); if(!file.exists(p)) stop(paste("missing",p))
  x <- readRDS(p)
  req <- c("game_id","pos_team","def_pos_team","rush","pass","pass_attempt","punt","yards_gained","interception_thrown_stat","interception_stat")
  m <- setdiff(req,names(x)); if(length(m)) stop(paste(yr,"missing",paste(m,collapse=",")))
  one <- function(v) !is.na(v) & v==1
  x$game_id <- as.character(x$game_id)
  scrim <- (one(x$rush)|one(x$pass)|one(x$pass_attempt)) & !one(x$punt)
  ints <- one(x$interception_thrown_stat)|one(x$interception_stat)
  gids <- intersect(unique(x$game_id),sched$game_id[sched$season==yr])
  for(gid in gids) {
    g <- x[x$game_id==gid,,drop=FALSE]; sg <- sched[sched$game_id==gid,,drop=FALSE]
    if(nrow(sg)!=1) next
    for(tm in c(sg$home_team[1],sg$away_team[1])) {
      tr <- !is.na(g$pos_team)&as.character(g$pos_team)==tm
      dr <- !is.na(g$def_pos_team)&as.character(g$def_pos_team)==tm
      sr <- (one(g$rush)|one(g$pass)|one(g$pass_attempt)) & !one(g$punt)
      rr <- sr & one(g$rush); pr <- sr & (one(g$pass)|one(g$pass_attempt))
      pf <- if(tm==sg$home_team[1]) sg$home_points[1] else sg$away_points[1]
      pa <- if(tm==sg$home_team[1]) sg$away_points[1] else sg$home_points[1]
      venue <- if(tm==sg$home_team[1]) "HOME" else "AWAY"
      out[[length(out)+1]] <- data.frame(season=yr,game_id=gid,team=tm,start_date=sg$start_date[1],venue=venue,
        game_points_for=pf,game_points_against=pa,
        off_plays=sum(tr&sr),def_plays=sum(dr&sr),
        off_yards=sum(ifelse(tr&sr&!is.na(g$yards_gained),g$yards_gained,0)),
        def_yards=sum(ifelse(dr&sr&!is.na(g$yards_gained),g$yards_gained,0)),
        rush_plays=sum(tr&rr),pass_plays=sum(tr&pr),
        rush_yards=sum(ifelse(tr&rr&!is.na(g$yards_gained),g$yards_gained,0)),
        pass_yards=sum(ifelse(tr&pr&!is.na(g$yards_gained),g$yards_gained,0)),
        pass_attempts=sum(tr&one(g$pass_attempt)),interceptions=sum(tr&ints),stringsAsFactors=FALSE)
    }
  }
}
tg <- do.call(rbind,out); tg <- tg[order(tg$team,tg$start_date,tg$game_id),]
safe <- function(n,d) ifelse(d==0,NA_real_,n/d)
rows <- list()
for(tm in unique(tg$team)) {
 z <- tg[tg$team==tm,,drop=FALSE]
 for(i in seq_len(nrow(z))) {
  prior <- z[seq_len(i-1),,drop=FALSE]
  if(i==1) prior <- z[FALSE,,drop=FALSE]
  rows[[length(rows)+1]] <- data.frame(season=z$season[i],game_id=z$game_id[i],team=tm,start_date=z$start_date[i],home_away_neutral=z$venue[i],
   qualified_prior_games=nrow(prior),
   points_for_per_game=safe(sum(prior$game_points_for),nrow(prior)),
   points_against_per_game=safe(sum(prior$game_points_against),nrow(prior)),
   offensive_scrimmage_plays_per_game=safe(sum(prior$off_plays),nrow(prior)),
   defensive_scrimmage_plays_per_game=safe(sum(prior$def_plays),nrow(prior)),
   offensive_yards_per_play=safe(sum(prior$off_yards),sum(prior$off_plays)),
   defensive_yards_per_play=safe(sum(prior$def_yards),sum(prior$def_plays)),
   rush_play_rate=safe(sum(prior$rush_plays),sum(prior$off_plays)),
   pass_play_rate=safe(sum(prior$pass_plays),sum(prior$off_plays)),
   rush_yards_per_play=safe(sum(prior$rush_yards),sum(prior$rush_plays)),
   pass_yards_per_play=safe(sum(prior$pass_yards),sum(prior$pass_plays)),
   interception_rate=safe(sum(prior$interceptions),sum(prior$pass_attempts)),
   rest_days=if(nrow(prior)) as.numeric(difftime(z$start_date[i],prior$start_date[nrow(prior)],units="days")) else NA_real_)
 }
}
feat <- do.call(rbind,rows)
if(any(feat$season==2025)) stop("2025 TEST leakage")
write.csv(tg,"phase4_team_game_mechanical_primitives_v1_108.csv",row.names=FALSE)
write.csv(feat,"phase4_feature_canary_v1_108.csv",row.names=FALSE)
cat("rows",nrow(feat),"seasons",paste(sort(unique(feat$season)),collapse=","),"2025",sum(feat$season==2025),"\n")
