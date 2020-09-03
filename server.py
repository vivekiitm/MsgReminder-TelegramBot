from bot import telegram_chatbot
import random
import threading

bot = telegram_chatbot("config.cfg")

def make_reply(msg):

    reply =None

    if msg is not None:

        if(msg.lower() == 'hi' or msg.lower() == 'hello' or msg.lower() =='hii'):
            reply = "Hi! How are you! You can set reminder by typing 'reminder' or if you are in a mood to play I have something for you ;). Just type game."
            return reply, False

        if(msg.lower() == 'reminder'):
            reply = ("Enter your reminder according to following format: \n 1st line: When to remind(After how much minutes) \n 2nd line: Your reminder message" )
            return reply, True
            
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
play = False
run = -1
score = 0
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
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
                else:
                    bot.send_message("Reminder Set!", from_)
                continue
            
            ''' 
                Hand Cricket
            '''
            if( play == True):
                run = message
                print(run)
                try:
                    temp = int(run)
                    if(temp>=1 or temp<=6):
                        run = int(run)
                        print(run)
                        bowler = random.randint(1,6)
                        print(bowler, run)
                        if(bowler == run):
                            play = False
                            bot.send_message("OUT!!!!\n Total Score: "+str(score), from_)
                            score = 0
                            run = -1
                        else:
                            bot.send_message(bowler, from_)
                            score += run
                    else:
                        play = False
                        bot.send_message("You typed invalid number! Game Over\n Total Score: "+str(score), from_)
                        score = 0
                        run = -1 
                        continue
                    
                except:
                    play = False
                    bot.send_message("You typed invalid number! Game Over\n Total Score: "+str(score), from_)
                    score = 0
                    run = -1 
                    continue

                continue


            if(message.lower() == 'game'):
                play = True
                bot.send_message("Let's play Hand Cricket. You have to enter number between 1 and 6. If it matches with my number, you gets out otherwise you score that much. Simple! Let's start. It's your first ball", from_)
                continue



            reply, reminderMessage = make_reply(message)
            bot.send_message(reply, from_)