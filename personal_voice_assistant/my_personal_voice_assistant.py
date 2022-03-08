import pyttsx3 # which voice choose from system for our assistant
import datetime # show date nd time
import speech_recognition as sr # only speech recognize nd store as a string
import wikipedia # serching in wikkipedia uses
import webbrowser # open web browser use
import os
import smtplib # for email sending uses
#import time # sleep for time
import pandas as pd # for excel file read 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[2].id) # print the all voices in our computer
#engine.setProperty('voices',voices[2].id) #set property means you set the voice mail or female



def speak(audio):
    engine.say(audio) # engine say the audio word from main function
    engine.runAndWait() # it going to be run

def wishMe():
    hour= int(datetime.datetime.now().hour) # it will give hour in int form
    if hour>=0 and hour<12:
        speak("   Good Morning..")
    elif hour>=12 and hour<17:
        speak("   Good AfterNoon..")
    else:
        speak("   Good Evening..")
    speak("I am your assistant sir, how may i help you")

def takecommand(): # ye sirf mic me boli hui aawaj ko store krta h bs
    '''it take microphone input from user and return string o/p'''
    r=sr.Recognizer() # it helps to recogniz the audio
    with sr.Microphone() as source:
        print("Listening..") # means that code sun rha hai apki voice ko
        r.pause_threshold=1 # means code sun k 1 second ruk k phase ko complete krega...yaha mene 1 second liaa h..1 second k baad code ka phase compelte hoga
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in') # user ne jo bhi kuch bola hoga ussko sunega(in english langauge) or smjhega
        print("User Said : ",query,"\n") # apne jo bhi bola usko print kr k show krega ki ye bola
    except Exception:
        print("Say that again please...") # voice recognize nhi hui...ya mic ko thik se sunai nhi diaa to ye RUN hoga
        return "None" #ye bs ek simple string h none ye tbhi print hoga jb koi or problem hogi unexceptd

    return query # jo bhi bola gya hai usko ek 'query' variable me store kr lega

def sendEmail(to,content): # sending email
    server=smtplib.SMTP("smtp.gmail.com",587) # compulsary to write i don't know why but you have to write
    server.ehlo()  # compulsary to write i don't know why but you have to write
    server.starttls() # compulsary to write i don't know why but you have to write
    #server.login('pankajverma2319975@gmail.com', 'your-password')
    server.login(input("Enter Sender Email : "),input(("Password : "))) # apka khud ka email id or password
    #server.sendmail('pankajverma231997@gmail.com', to, content)
    server.sendmail(to,to,content) # jisko bhejna h uska email address # isme jo phla 'to' hai usme reciver tha emai store hoga..aap chaho to direct email address bhi likh skte hoo
    server.close() # connection close...bohot zaruri hai


if __name__ == '__main__':
    wishMe()
    while(True):
      query = takecommand().lower() # query is just a varible you can take anything. .lower() isiliye taaki recognize word ko small later me convert krde nhi to agr hum google.com kholegnge to Google.com(wrong url) khulega
      if 'wikipedia' in query:
          speak("please wait...")
          query=query.replace("wikipedia","") # jo query me bola h usme agar wikipedia kahi likha h usko replace kr dega blank("") se..like[(salman khan wikkipedia) replace to (salman khan)]
          result=wikipedia.summary(query,sentences=2) #ye wikipedia website me serch krega jo bhi query me store the like(salman khan)
          speak("According to wikipedia")
          print(result)
          speak(result)

      elif 'open youtube' in query: # query me kahi bhi agar 'open youtube' bola gya toh ye RUN hoga...like['open youtube','please open youtube', 'bhai plese plase krdo yr open youtube']
          speak("please wait..")
          result=webbrowser.open("https://www.youtube.com")

      elif ('open ' and '.com') in query:
          query = query.replace('open ',"")
          query = query.replace('.com',"")
          query = query.replace(" ", "")
          result=webbrowser.open(f"https://www.{query}.com")

      elif ('open ' and '.in') in query:
          query = query.replace('open ',"")
          query = query.replace('.in',"")
          query = query.replace(" ","")
          result=webbrowser.open(f"https://www.{query}.in")

      elif "play music" in query:
          allsongs=os.listdir(r"F:\new mp3 songs")
          os.startfile(os.path.join(r"F:\new mp3 songs",allsongs[0]))# path k sath join hoga like F:\new mp3 songs\Dil Chori_320(WapKing) and start. allsongs[0] means randomly file open hogi

      elif 'time' in query:
          strtime=datetime.datetime.now().strftime("%H:%M:%S") # it is the just strftime("%H:%M:%S") format of the time
          print("The Time Is : ",strtime)
          speak(strtime)

      elif 'open sublime text' in query:
          os.startfile(r"C:\Program Files\Sublime Text 3\sublime_text.exe")
          print("done")

      elif 'shutdown system' in query:
          print("speak 'YES' for shut down otherwise 'NO' ".title())
          shutdown = takecommand()
          if shutdown == 'no':
              pass
          elif shutdown=='yes':
              os.system("bye bye..... shuting down.....".title())
          else:
              print("sorrry....")

      elif 'send email' in query:
          try:
              speak("what should i say ?")
              emailContent=takecommand() # email ka jo msg hoja wo yaha bolo
              to=input("Enter Reciver Email : ")
             # to = "pankajverma231997@gmail.com" #jisko email bhejna uska email addresss
              sendEmail(to, emailContent)
              print("Email has been sent successfully !!!")
              speak("Email has been sent successfully !!!")
          except Exception:
              print("Sorry!!...Unable To Send Message")

      elif 'show contact' in query:
          DataF = pd.read_excel(r"E:\SampleExcelFileWithNameContactAge.xlsx", sheet_name='Sheet1',usecols=['NAME', 'CONTACTS'])
          speak("here the contacts with name".title())
          print(DataF)


      elif 'exit code' in query:
          print("Bye bye Sir ...have a good day")
          speak("Bye bye Sir ...have a good day")
         # time.sleep(1)
          exit()
      else:
          print("sorry...Can't undersatnd\n".title())

