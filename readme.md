### This folder contains all the scripts created and used in the system to show notifications and other stuff

- To edit the crontab entries, run the command: `crontab -e`
- To list existing cron jobs: `crontab -l`

Sample entries(with tabs in between, not spaces):

15      9-18    *       *       1-5     /Users/hardhik/dev/macCronJobs/waterReminder45min.sh

0       9-18    *       *       1-5     /Users/hardhik/dev/macCronJobs/takeBreak.sh

0       9       *       *       *       /usr/bin/python /Users/hardhik/dev/macCronJobs/morningMessage.py



- Helpful link to understand the syntax: https://crontab.guru

Repo backed up at: https://github.com/Hardhik/macCronJobs