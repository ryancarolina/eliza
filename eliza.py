from gtts import gTTS
import os

# Vars
language = "en"

# Functions
def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

# Intro
def eliza_speech(speech, fname):
    myobj = gTTS(text=speech, lang=language, slow=False)
    myobj.save(fname)
    os.system("mpg321 " + fname)

eliza_speech("Hello! My name is Eliza. I am a nurse AI specializing in well being analysis. I am here to help. I am going to ask you a series of questions to help me calculate your wellness score.", "eliza_intro.mp3")
print("Hello! My name is Eliza.")
print("I am a nurse AI specializing in well being analysis. I am here to help.")

# Get Name
eliza_speech("What is your name?", "eliza_whatisyourname.mp3")
print("What is your name?")

def getname():
    while True:
        name = input("Reply: ")
        if name.isalpha():
            break
        eliza_speech("Please enter alphabetic characters only.", "eliza_namevalidation.mp3")
        print("Please enter characters A-Z only.")
    return name

name = getname()

# Get Age
eliza_speech("How old are you?", "eliza_howoldareyou.mp3")
print("How old are you?")

def getage():
    while True:
        age = input("Reply: ")
        if age.isdigit():
            break
        eliza_speech("Please enter digits only.","eliza_agevalidation.mp3")
        print("Please enter digits 0-9 only.")
    retval = clamp(int(age), 0, 150)
    return str(retval)

age = getage() #TODO add logic to ask additional questions for those over 55

#TODO add logic to get user gender for gender related medical questions

#TODO connect to database so Eliza will have memory

# Health Check
eliza_speech("So your name is " + name + " and you are " + age + " years old.", "eliza_statenameandage.mp3")
print("So your name is " + name + " and you are " + age + " years old.")

eliza_speech(name + " I am going to ask some questions about your physical health.", "eliza_healthquestionsprompt.mp3")

eliza_speech("How do you feel physically? Enter a value between 1 and 10 with 10 meaning you feel amazing.", "eliza_howdoyoufeelphysically.mp3")
print("How do you feel physically? Enter a value between 1 and 10 with 10 meaning you feel amazing.")

def physcheck():
    while True:
        phys_score = input("1 - 10: ")
        if phys_score.isdigit(): #TODO add logic to restrict range between 1 and 10
            eliza_speech("Ok " + name + " thanks!", "eliza_oknamethanks.mp3")
            print("Ok " + name + " thanks!")
            break
        eliza_speech("Please enter a valid number between 1 and 10.", "eliza_physscorevalidation.mp3")
        print("Please enter a valid number between 1 and 10.")
    retval = clamp(int(phys_score), 1, 10)
    return str(retval)

phys_score = physcheck()

eliza_speech(name + " let's get your temperature. Please take your temperature and reply with the result. For example if the thermometer reads 98.5, enter 98.5", "eliza_checktemp.mp3")
print(name + " let's get your temperature. Please take your temperature and reply with the result. For example if the thermometer reads 98.5, enter 98.5")

def tempcheck(): #TODO look into thermometers with an API
    temp_reply = input("Reply: ")
    clamp(float(temp_reply), 0.0, 200.0)
    if float(temp_reply) > 100.4:
        eliza_speech(name + " your temperature is higher than expected. Please re-take your temperature and speak with your doctor if it reads higher than 100.4 degrees fahrenheit.", "eliza_temphigh.mp3")
        print(name + " your temperature is higher than expected. Please re-take your temperature and speak with your doctor if it reads higher than 98.6 degrees fahrenheit.")
        temp_score = 3
        return temp_score

    elif (float(temp_reply) <= 96.0):
        eliza_speech(name + " your temperature is lower than expected. Please re-take your temperature and speak with your doctor if it reads lower than 96 degrees fahrenheit.", "eliza_templow.mp3")
        print(name + " your temperature is lower than expected. Please re-take your temperature and speak with your doctor if it reads lower than 96 degrees fahrenheit.")
        temp_score = 3
        return temp_score
    else:
        eliza_speech(name + " your temperature is within the expected range. That's good news!", "eliza_normaltemp.mp3")
        temp_score = 0
        return temp_score

temp_score = tempcheck()

#TODO add logic for a blood pressure check

#TODO add logic to check time stamp against users last physical

# Mental Health Check

eliza_speech(name + " Now I am going to ask some questions about your mental health.", "eliza_mentalhealthquestionsprompt.mp3")

eliza_speech("How do you feel emotionally? Enter a value between 1 and 10 with 10 meaning you feel perfectly sound.", "eliza_howdoyoufeelemo.mp3")
print("How do you feel emotionally? Enter a value between 1 and 10 with 10 meaning you fell perfectly sound.")

def emotcheck():
    while True:
        emot_score = input("1 - 10: ")
        if emot_score.isdigit():
            eliza_speech("Great " + name + " thanks!", "eliza_greatnamethanks.mp3")
            print("Great " + name + " thanks!")
            break
        eliza_speech("Please enter a valid number between 1 and 10.", "eliza_emotscorevalidation.mp3")
        print("Please enter a valid number between 1 and 10.")
    retval = clamp(int(emot_score), 1, 10)
    return retval

emot_score = emotcheck()

eliza_speech("Have you harmed yourself or thought about harming yourself?", "eliza_selfharm.mp3")
print("Have you harmed yourself or thought about harming yourself?")

def selfharmcheck():
    while True:
        self_harm_reply = input("Yes or No: ")
        if self_harm_reply.isalpha():
            if (self_harm_reply.lower() == "yes"):
                eliza_speech("Please call 1-800-273-8255 for help! If it's an emergency call 911! You matter. You are loved.", "eliza_pleasecall.mp3")
                print("Please call 1-800-273-8255 for help! If it's an emergency call 911! You matter. You are loved.")
                danger_score = 20
                return danger_score
            elif (self_harm_reply.lower() == "no"):
                eliza_speech("I'm glad to hear that " + name, "eliza_gladtohear.mp3")
                print("I'm glad to hear that " + name)
                danger_score = 0
                return danger_score
            elif (self_harm_reply.lower() != "yes" or "no"):
                eliza_speech(name + " please reply with yes or no.", "eliza_yesnovalidation.mp3")
        eliza_speech("Please enter alphabetic characters only.", "eliza_selfharmalphvalidation.mp3")
        print("Please enter alphabetic characters only.")

danger_score = selfharmcheck()

eliza_speech("Have you harmed anyone or thought about harming anyone?", "eliza_harm.mp3")
print("Have you harmed anyone or thought about harming anyone?")

def harmcheck():
    while True:
        harm_reply = input("Yes or No: ")
        if (harm_reply.isalpha()):
            if (harm_reply.lower() == "yes"):
                eliza_speech("Please call 1-800-273-8255 for help! If it's an emergency call 911! You matter. You are loved.", "eliza_pleasecall.mp3")
                print("Please call 1-800-273-8255 for help! If it's an emergency call 911! You matter. You are loved.")
                danger_score2 = 20
                return danger_score2
            elif (harm_reply.lower() == "no"):
                eliza_speech("That's good to hear " + name, "eliza_goodtohear.mp3")
                print("That's good to hear " + name)
                danger_score2 = 0
                return danger_score2
            elif (harm_reply.lower() != "yes" or "no"):
                eliza_speech(name + " please reply with yes or no.", "eliza_yesnovalidation.mp3")
        eliza_speech("Please enter alphabetic characters only.", "eliza_selfharmalphvalidation.mp3")
        print("Please enter alphabetic characters only.")

danger_score2 = harmcheck()

# Calculate Well Being Score
def sumscore():
    total_danger_score = int(danger_score) + int(danger_score2)
    total_mindbody_score = int(emot_score) + int(phys_score)
    wellbeing_score = int(total_mindbody_score) - int(total_danger_score)
    wellbeing_score_total = int(wellbeing_score) - int(temp_score)
    wellbeing_score_tostring = str(wellbeing_score_total)
    eliza_speech("Your wellness score is: " + wellbeing_score_tostring + " out of 20", "eliza_wellnessscore.mp3")
    print("Your wellness score is: " + wellbeing_score_tostring + " out of 20")
    if (wellbeing_score_total <= 10):
        if (wellbeing_score_total > 5):
            eliza_speech(name + " your wellness score is sub-optimal, I recommend you go for a short walk to boost your well being", "eliza_suboptimalscore.mp3")
            print(name + " your wellness score is sub-optimal, I recommend you go for a short walk to boost your well "
                         "being.")
        elif (wellbeing_score_total <= 5):
            eliza_speech(name + " your wellness score is dangerously low, I recommend you speak with a loved one and/or your doctor about options to improve your well being.", "eliza_dangerscore.mp3")
            print(name + " your wellness score is dangerously low, I recommend you speak with a loved one and/or your "
                         "doctor about options to improve your well being.")
    if (wellbeing_score_total > 10):
        if (wellbeing_score_total <= 15):
            eliza_speech(name + " your wellness score is within the optimal range, nice! You're doing great!", "eliza_optimalscore.mp3")
            print(name + " your wellness score is within the optimal range, nice! You're doing great!")
        elif (wellbeing_score_total > 15):
            eliza_speech(name + " your wellness score is amazing! Keep it up!", "eliza_amazingscore.mp3")
            print(name + " your wellness score is amazing! Keep it up!")
    return wellbeing_score_total

sumscore()
