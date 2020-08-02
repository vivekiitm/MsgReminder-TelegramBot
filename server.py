from bot import telegram_chatbot
import random
import threading
#import gizoogle

bot = telegram_chatbot("config.cfg")

def make_reply(msg):

    reply =None

    if msg is not None:

        if(msg.lower() == 'game'):
            _1 = random.randint(1,6)
            _2 = random.randint(1,6)
            reply = "You have got " + str(_1) + " and " + str(_2) + " on two dices having a total sum of " + str(_1 + _2) + "!!!"
            return reply, False

        if(msg.lower() == 'reminder'):
            reply = ("Enter your reminder according to following format: \n 1st line: When to remind(After how much minutes) \n 2nd line: Your reminder message" )
            return reply, True
            
        #reply = gizoogle.text(msg)
        reply = "Hiii!!! \n Sorry, but i cann't understant ehat are you trying to say. Let's start again. Type 'Game' or 'Reminder'."
    return reply, False



def runReminder(msg, from_):
    bot.send_message(msg, from_)

def setReminder(msg, from_):
        content = msg.split('\n')
        if(len(content)!=2):
            reply = "Incorrect format, please try again :("
            return reply, True
        else:
            time=0
            try:
                time = int(content[0])
            except:
                reply = "Given time is not valid! Please try again."
                return reply
            remindTo =content[1]
            msg = "Reminder! \n You have to " + remindTo
            sTime = threading.Timer(time*60, runReminder, [msg, from_])
            sTime.start()
            return None, False


update_id = None
reminderMessage = False
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        print(reminderMessage)
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]

            if(reminderMessage == True):
                reply, reminderMessage = setReminder(message, from_)
                if(reminderMessage == True):
                    bot.send_message(reply ,from_)
                continue
            reply, reminderMessage = make_reply(message)
            bot.send_message(reply, from_)