#!/usr/bin/python3
from crontab import CronTab
i=1
tym=cron.new(command='/usr/bin/echo')
tym.minute.duration(3,9).every(3)
print("python",i)
i=i+1
