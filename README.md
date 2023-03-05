# Quickstart
Put folder sync in root of your obsidian repo that folder structure will look like that
```
.
├── README.md
├── cooking
│   ├── recipe1
│   └── recipe2
├── philosophy
│   ├── cioran
│   └── taleb
└── sync
    ├── Makefile
    ├── requirements.txt
    └── sync.py
```


```
sudo apt update
sudo apt install python3 make python3-pip git
pip3 install virtualenv
make install
make sync
```

# Autosync
Add execution of script to your favourite scheduler e.g. cron, windows task scheduler etc. Remember to add `HOME` env variable, without it git command will fail

example of cron script
```
➜  ~ cat /etc/crontab 
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
SHELL=/bin/bash
17 *	* * *	root	cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.daily; }
47 6	* * 7	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.weekly; }
52 6	1 * *	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.monthly; }
#
* *	* * *	root	cd / && run-parts --report /etc/cron.minutely >> /var/log/0.log 2>&1


➜  ~ cat /etc/cron.minutely/sync-git 
#!/bin/bash
export HOME=/home/pawelee
bash -c 'cd /home/pawelee/ownCloud\ -\ pawelee@dysk.inf0r.pl/Notes/sync/ && sudo -u pawelee make sync'

```
