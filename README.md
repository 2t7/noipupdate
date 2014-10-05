noipudate
=========

Script for updating (free) noip hosts and thus preventing them from getting removed

You might want to start the script via a crontab entry (crontab -e) like this:
min hour day * * date>>noipupdate.log && python /path/to/script/noipupdate.py  >>noipupdate.log 2>&1
replace min, hour and day by the minute, hour and day of the month you want the command to be executed
A log file name noipupdate.log will be created in your homedirectory containing the date when the script was executed and the output of the script

IMPORTANT:
No root privileges are needed, but be sure nobody else than you can read the noipupdate.py file since it contains your username and password.
Storing the file in an encrypted home-directory seems wise (though you will have to mount the directory every time the machine restarts).
