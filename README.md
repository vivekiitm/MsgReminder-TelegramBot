# MsgReminder-TelegramBot
There are times, when we have to send some message at certain time but we forget till then. 
MsgReminder is here to fix this problem. All you have to do is to send time and message to this bot and it will automatically remind you to with the message at the given time. 
For some fun, you can play a game too with this bot ;). 

# Description
The main motto to develop this bot is to set reminder across cross-platform. There are times when our phone is on charging or anywhere else and we may miss our reminders set on phone app. To solve that issue, I developed this Bot which works on cross platform, means you can set reminder on phone and notified on laptop or vice versa too, on which ever device you are working.
Its implementation is relatively easy and simple. While creating bot, telegram give us a token id which is unique for every bot and it can be converted into url with slight modification and it acts as NGROK server. NGROK server helps us to create a web hook and exposing a local server to internet. So my local server gets connected to main server of telegram with this NGROK server. So, whenever I have to send a POST or GET request it will come through that given url. Data is shared as JSON objects. The main challenge in this pobject is to schedule reminders in python but that is also done easily using python module threading. It basically creates separate flow of executions. I also made a small game “Hand Cricket” for fun in it. It’s a simple game, user have to enter a number between 1 to 6 and my program will also generate a random number in that range and if both are same the player is given out otherwise the that many runs will get added to his total score.

