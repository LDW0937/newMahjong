cd srcs
currTime=$(date "+%Y_%m_%d")
logfile=${currTime}_smart_win.log 
python -m index >& logs/$logfile &
