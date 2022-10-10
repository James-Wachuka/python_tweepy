###### Python-Tweepy-Cron
Using python and tweeter API to follow back new followers. This task is scheduled using windows schduler
###### data
This script fetches followers and friends using tweepy and a ```to_follow``` list. Then follows all followers who are not friends using ```api.create_friendship()```
##### dataframe
A dataframe of followers and friend is created by fetching usernames using ```follower_.screen_name```

###### Automating the job with windows scheduler
This etl job is scheduled to run every 5 minutes for one day, using the windows task scheduler.  ```schedule_follow_back.bat``` activates the environment and runs the python script.
Creating a task in windows task scheduler.
```start->task scheduler->create a folder (mytask)->create task (tweepy_follow_back)->trigger(repeat after 5 mins)->action(start program-schedule_follow_back.bat)```

###### Usage
* clone the repository
* install the requirements, activate venv and run the script
