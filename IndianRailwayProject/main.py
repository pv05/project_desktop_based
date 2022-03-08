import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def generteskeleton():
    audio=AudioSegment.from_mp3("railway.mp3")

#1 generate--> kripya ghyan dejiye
    start=88000 # 88000 milisecond means ( 88 = 60+28 )seconds = 1 min :28 seconds
    finish=90200
    audioprocessed=audio[start:finish]
    audioprocessed.export("1_hindi.mp3",format="mp3")

# 2 from city

#3 generate--> se chl kar
    start=91000
    finish=92200
    audioprocessed=audio[start:finish]
    audioprocessed.export("3_hindi.mp3",format="mp3")

#4 via city

#5 generate--> ke raaste
    start=94000
    finish=95000
    audioprocessed=audio[start:finish]
    audioprocessed.export("5_hindi.mp3",format="mp3")

#6 to-city

#7 generate--> ko jaane wali gaadi sankhya
    start = 96000
    finish = 98900
    audioprocessed = audio[start:finish]
    audioprocessed.export("7_hindi.mp3", format="mp3")

#8 train number and name

# 9 generate--> kuch he samay me platform sankhaya
    start = 105500
    finish = 108200
    audioprocessed = audio[start:finish]
    audioprocessed.export("9_hindi.mp3", format="mp3")

#10 platform number

#11 generate--> par aa rhi h
    start = 109000
    finish = 112250
    audioprocessed = audio[start:finish]
    audioprocessed.export("11_hindi.mp3", format="mp3")

def generateannoucment(filename):
    df=pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows(): # ye xls file mese generate kregi
        #2 Generate from city
        texttospeech(item['from'],'2_hindi.mp3') # means xls fil me from wale colume me jo bhi tha uski audio banao or 2_hindi.mp3 generate kr k texttospeech() k pass bhej do

        #4 Generate via city
        texttospeech(item['via'], '4_hindi.mp3')

        #6 Generate to-city
        texttospeech(item['to'], '6_hindi.mp3')

        #8 Generate train number and name
        texttospeech(item['train_no']+" "+item['train_name'], '8_hindi.mp3')

        #10 Generate platform number
        texttospeech(item['platform'], '10_hindi.mp3')

        audios=[f"{i}_hindi.mp3" for i in range(1,12)] #jo 2_hidi.m3,4_hidi.m3,6_hidi.m3...etc file generate hui thi texttospeech() ki madad se un sbko hum ab chronologcly add krenge
        announcement=mergeaudios(audios)
        announcement.export(f"train_{item['train_no']}_{index+1}.mp3',format='mp3'")

#this functions returns pydubs audio segment
def mergeaudios(audios):
    combined=AudioSegment.empty()#it helps to make empty audio
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)

    return combined

def texttospeech(text,filename):
    mytext=str(text)
    language='hi'#hindi language
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename) # jo 2_hidi.m3,4_hidi.m3,6_hidi.m3...etc file generate kr k save bhi hui hai

if __name__ == '__main__':
    print("Generating Skeleton..")
    generteskeleton()
    print("Now Generating Annoucemnt..")
    generateannoucment("announce_hindi.xlsx")

