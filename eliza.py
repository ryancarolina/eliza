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

age = getage()

#TODO add logic to get user gender for gender related medical questions

#TODO connect to database so Eliza will have memory

# Health Check
eliza_speech("So your name is " + name + " and you are " + age + " years old.", "eliza_statenameandage.mp3")
print("So your name is " + name + " and you are " + age + " years old.")

# Coronavirus
def covid19check():
    # Covid19 screening
    eliza_speech("Have you recently experienced any of the following symptoms, fever, cough, shortness of breath, and/or breathing difficulties?", "eliza_coloncancerscreen.mp3")
    while True:
        covid19_screening_reply = input("Yes or No: ")
        if covid19_screening_reply.isalpha():
            if (covid19_screening_reply.lower() == "yes"):
                eliza_speech(
                    "If you have a fever, cough and difficulty breathing, seek medical attention and call in advance. Follow the directions of your local health authority" + name,
                    "eliza_covid19yes.mp3")
                print(
                    "If you have a fever, cough and difficulty breathing, seek medical attention and call in advance. Follow the directions of your local health authority " + name)
                covid19_score = 10

                return covid19_score

            elif (covid19_screening_reply.lower() == "no"):
                eliza_speech(
                    "Great, please continue to do the 5! Wash your hands often, cough into your elbow, don't touch your face, maintain social distance, and stay home if you can " + name,
                    "eliza_getcoloncancerscreen.mp3")
                print("Great, please continue to do the 5! Wash your hands often, cough into your elbow, don't touch your face, maintain social distance, and stay home if you can " + name)
                covid19_score = 0

                return covid19_score

            elif (covid19_screening_reply.lower() != "yes" or "no"):
                eliza_speech(name + " please reply with yes or no.", "eliza_yesnovalidation.mp3")
        eliza_speech("Please enter alphabetic characters only.", "eliza_selfharmalphvalidation.mp3")
        print("Please enter alphabetic characters only.")

covid19_score = covid19check()

# If user is over 55, ask additional questions
def agecheck():
    if int(age) > 55:
        eliza_speech(name + "Because you are older than 55, I am going to ask you some additional questions.", "eliza_over55.mp3")
        print(name + " Because you are older than 55, I am going to ask you some additional questions.")

        # Colon cancer screening
        eliza_speech(name + "Have you been screened for colon cancer in the last 5 years?", "eliza_coloncancerscreen.mp3")
        while True:
            colon_cancer_screening_reply = input("Yes or No: ")
            if colon_cancer_screening_reply.isalpha():
                if (colon_cancer_screening_reply.lower() == "yes"):
                    eliza_speech(
                        "Well done " + name,
                        "eliza_welldonename.mp3")
                    print(
                        "Well done " + name)
                    colon_cancer_score = 0
                    eliza_speech("Ok thats all the age related questions I have for you " + name,
                                 "eliza_agequestionswrapup.mp3")
                    print("Ok that's all the age related questions I have for you " + name)
                    return colon_cancer_score
                elif (colon_cancer_screening_reply.lower() == "no"):
                    eliza_speech("Colon cancer screening is recommended for everyone at age 50. The colonoscopy is a test that is most frequently recommended, though there are other options. Ask your doctor which screening test is best for you. " + name, "eliza_getcoloncancerscreen.mp3")
                    print("That is something that everyone should look into after 50 " + name)
                    colon_cancer_score = 2
                    eliza_speech("Ok thats all the age related questions I have for you " + name,
                                 "eliza_agequestionswrapup.mp3")
                    print("Ok that's all the age related questions I have for you " + name)
                    return colon_cancer_score
                elif (colon_cancer_screening_reply.lower() != "yes" or "no"):
                    eliza_speech(name + " please reply with yes or no.", "eliza_yesnovalidation.mp3")
            eliza_speech("Please enter alphabetic characters only.", "eliza_selfharmalphvalidation.mp3")
            print("Please enter alphabetic characters only.")

colon_cancer_score = agecheck()

eliza_speech("I am going to ask some questions about your physical health.", "eliza_healthquestionsprompt.mp3")

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
# TODO look into apple/android watch temperature APIs
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

#TODO add logic to check time stamp against users last physical. Can we gain access to medical data via an API?

# Mental Health Check

eliza_speech(name + " Now I am going to ask some questions about your mental health.", "eliza_mentalhealthquestionsprompt.mp3")

eliza_speech("How do you feel emotionally? Enter a value between 1 and 10 with 10 meaning you feel perfectly sound.", "eliza_howdoyoufeelemo.mp3")
print("How do you feel emotionally? Enter a value between 1 and 10 with 10 meaning you fell perfectly sound.")

# TODO Should there be a separate subjective optional path?
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
    # TODO Refactor the scoring, needs to be clean.
    total_danger_score = int(danger_score) + int(danger_score2) + int(colon_cancer_score) + int(covid19_score)
    total_mindbody_score = int(emot_score) + int(phys_score)
    wellbeing_score = int(total_mindbody_score) - int(total_danger_score)
    wellbeing_score_total = int(wellbeing_score) - int(temp_score)
    wellbeing_score_tostring = str(wellbeing_score_total)
    eliza_speech("Your wellness score is: " + wellbeing_score_tostring + " out of 20", "eliza_wellnessscore.mp3")
    print("Your wellness score is: " + wellbeing_score_tostring + " out of 20")
    if (wellbeing_score_total <= 10):
        if (wellbeing_score_total > 5):
            eliza_speech(name + " your wellness score is sub-optimal, I recommend you take a day of rest and increase your water intake to boost your well being. I would also suggest following up with your health care provider if you do not improve within the next seven days.", "eliza_suboptimalscore.mp3")
            print(name + " your wellness score is sub-optimal, I recommend you take a day of rest and increase your water intake to boost your well being. I would also suggest following up with your health care provider if you do not improve within the next seven days.")
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

# TODO Look into reporting, dashboards, etc... Think heatmap of user temp data and producing fever trends on a dashboard.
