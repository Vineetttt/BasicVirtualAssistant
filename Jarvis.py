import random                         # randome module to use wherever necessary
import pyttsx3                        # python text to speech library
import datetime                       # datetime library for greeting equivalent with the live date and time
import pywhatkit                      # to browse and play the selected song/video automatically from youtube
import speech_recognition as sr       # to take user microphone input (voice input)
import wikipedia                      # to browse the wikipedia content
import webbrowser                     # to display the results fetched from the browser after the user input is taken
import os                             # to interact with the operation system
import time                           # for reminder
from plyer import notification        # to display the notifiaction
import smtplib                        # to send emails

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print("Enter 0 for FEMALE Assistant")
print("Enter 1 for MALE Assistant")
choice = int(input("Enter Your Choice: "))         # user option selection for the voice over male/female
if choice == 0:
    voices = voices[0].id
    engine.setProperty('voice', voices)
elif choice == 1:
    voices = voices[1].id
    engine.setProperty('voice', voices)
else:
    print('Invalid Choice,Please enter your choice again!')
    choice = int(input("Enter Your Choice: "))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# creating a wish function to greet the user at the start-- greets according to the time and returns
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning ")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening ")
WishMe()

print("VINEET:-I am Vineet, I hope you and your loved ones are staying safe and healthy . What can I do for you?")
speak("I am Vineet, I hope you and your loved ones are staying safe and healthy. What can I do for you?")

# Creating function to take user microphone input and return the string version of the input
def takeCommand():
    r = sr.Recognizer()               # sr==speech_recognition
    with sr.Microphone() as src:
        print("Listening...")
        r.pause_threshold = 2         # 2 seconds pause after which the user said phrase is assumed to be complete.
        audio = r.listen(src)

    try:                              # to test the block of code
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        print("User:-", query)

    except Exception as e:            # error handling part
        print("Please Say that Again!...Try saying -NAME- before your command")
        return "None"
    return query

def thereExist(terms):
    for term in terms:
        if term in query:
            return True

#Creating a Dictonary with names as the keys and the corresponding email address as values
Emails = {'vineet': 'vineetchotaliya30@gmail.com', 'mayank': 'mayankchotaliya2001@gmail.com',
          'dad': 'narendrachotaliya618@gmail.com'}

# Creating a function to send Email using the smtp library
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('vineetchotaliya30@gmail.com','*******') # type your email passowrd here
    server.sendmail('vineetchotaliya30@gmail.com',to,content)
    server.close()

while True:
    query = takeCommand().lower()

    # Creating the Logic for user command
    # if 'who is' in query:
    #     speak("Searching the Wikipedia ")
    #     query = query.replace('who is', '')
    #     results = wikipedia.summary(query, sentences=2)
    #     speak('According to the wikipedia,')
    #     print('\n', results)
    #     speak(results)

    if thereExist(['start a game','play a game','games can i play','start game','game','i want to play a game']):
        speak('Which game will you play?')
        print('1 for TIC-TAC-TOE\n2 for DOTS AND BOXES\n3 for UNO\n4 for SUBWAY SURFER\n5 for AMONG US  ')
        choose=int(takeCommand())
        if choose==1:
            myGame = webbrowser.open('https://playtictactoe.org/')
            speak('You are Playing Tic-Tac-Toe versus AI')
        elif choose==2:
            myGame = webbrowser.open(' https://gametable.org/games/dots-and-boxes/')
            speak('You are playing Dot And Boxes versus AI')
        elif choose==3:
            myGame=webbrowser.open('https://poki.com/en/g/uno-online')
            speak('You are playing UNO')
        elif choose==4:
            myGame=webbrowser.open('https://poki.com/en/g/subway-surfers')
            speak('You are playing Subway Surfers')
        elif choose==5:
            myGame=webbrowser.open('https://amongus-online.net/')
            speak('You are playing Among Us')

    elif thereExist(['how are you','how is everything','how are you doing','how have you been','are you fine',
                     'what are you upto']):
        response=['Somewhere between better and best.','At minding my own business? Better than most people.'
        ,'Do you really care?','Armed and ready!','My creator said not to answer that question',
        'I was fine until you asked',"If I were any better, I'd be you."]
        compResponse=random.choice(response)      # fetches random value from the response list
        print(compResponse)
        speak(compResponse)

    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
        speak('Opening Youtube')

    elif 'open google' in query:
        webbrowser.open('google.com')
        speak('Opening Google')

    elif 'open spotify' in query:
        codePath = "C:\\Users\\sanjay patel\\AppData\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(codePath)
        speak('Opening Spotify')

    elif thereExist(['play','youtube']):
        song=query.replace('play'or'youtube','')
        speak('Playing'+song)
        pywhatkit.playonyt(song)

    elif thereExist(['search for','search','what is','who is']) and 'youtube' not in query:
        browse=query.split('for'or'is')[-1]
        search = 'https://www.google.com/search?q=' +browse
        webbrowser.open(search)
        speak('Here is what I found for'+browse+'on google')

    elif thereExist(['what can you do','how can you help me','what are the tasks you can perform','help','assit me']):
        print(f"VINEET:- Try Saying\n\tOpen Spotify\n\tOpen Youtube\n\tSend an Email\n\tSet a Reminder\n\tStart a game")
        speak('Try saying Open youtube , open spotify and everything you wish i will probably try and fulfil it!')

    elif thereExist(['set a reminder','remind me','set reminder','save reminder','save a reminder']):
        print('Please state the topic for your reminder ')
        r = speak('Please state the topic for your reminder ')
        rem=takeCommand()
        print('Enter The Message associated with Reminder: ')
        m = speak('Enter The Message associated with Reminder: ')
        mess=takeCommand()
        print("After how many minutes Should I remind You? ")
        d = speak("After how many minutes Should I remind You? ")
        duration=int(takeCommand())
        time_min = duration * 60
        if __name__ == "__main__":
            while True:
                notification.notify(
                    title=rem,
                    message=mess,
                    timeout=15  # notification stays for 15 seconds and goes off after that
                )
                time.sleep(time_min)
        takeCommand()

    elif thereExist(['what is the time','tell me the time','what time is it','tell the time']):
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        dt = datetime.date.today()
        print(f"Today is {dt} and It is {strTime} now ")
        speak(f"Today is {dt} and The time is {strTime}")

    elif 'email'  in query:
        try:
            name=input('Enter the name to whom you want to send the mail (mayank/vineet/dad)')
            x=Emails.get(name)
            speak("What Should the Email Say? ")
            content = takeCommand()
            to = x
            sendEmail(to, content)
            speak("Your Email has been sent ")
        except Exception as e:
            print(e)

    elif thereExist(['on amazon','amazon']):
        browse=query.split('for')[-1]
        search='https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+browse
        webbrowser.open(search)
        speak('Here is what i found for'+browse)

    elif thereExist(['start instagram','open instagram','launch instagram']):
        search='https://www.instagram.com/'
        webbrowser.open(search)
        speak('Opening Instagram')

    elif thereExist(['start twitter','open twitter']):
        search='https://www.twitter.com/'
        webbrowser.open(search)
        speak('Opening Twitter')

    elif thereExist(['twitter messages','open my twitter messages']):
        search = 'https://twitter.com/messages'
        webbrowser.open(search)
        speak('Opening your twitter messages')

    elif thereExist(['open my instagram dm','instagram dm','instagram messages','open my instagram messages'
        ,'open my instagram inbox','instagram inbox']):
        search='https://www.instagram.com/direct/inbox/?hl=en'
        webbrowser.open(search)
        speak('Opening your instagram inbox')

    elif thereExist(['thank you']):
        response=["Anything for you!","Don’t mention it.","It’s my pleasure","Anytime and anywhere for you"]
        compResponse=random.choice(response)
        print(compResponse)
        speak(compResponse)

    elif thereExist(['goodbye','see you ']):
        print('VINEET:-GoodBye! Happy To Help You Anytime')
        speak('GoodBye! Happy To Help You Anytime')
        break          # killing the code after the user says goodbye

    else:
        if query=='none':
            speak('Please say that again')
        # else:
        #     search = 'https://www.google.com/search?q=' + query
        #     webbrowser.open(search)
        #     speak('Fetching appropriate result for you from GOOGLE!')
