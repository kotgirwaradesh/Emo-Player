from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import  EmoDetect
# Create your views here.
emotion= []
gender= []
age= []

def index(request):
    return render(request, 'index.html')


def gen(camera):
    while True:
        frame2 = camera.get_frame()

        frame=frame2[0]
        #print("in views:")
        #print(frame2[1])
        if(len(frame2[1])==3):
            emotion.append(frame2[1][0])
            gender.append(frame2[1][1])
            age.append(frame2[1][2])

        
        
        
        #print("in views emo:")
        #print(emotion)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')




def Emo_feed(request):
    return StreamingHttpResponse(gen(EmoDetect()),
                    content_type='multipart/x-mixed-replace; boundary=frame')
                    

def rend(request):
        #emotion=request.GET["Emotion"]
        #gender=request.GET["Gender"]
        #print("....")
        #print(emotion[-1])
        #print("....")
        if(emotion[-1]=='Happy' and gender[-1]=='Male' and '(0-8)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:0-8!'})        
        elif(emotion[-1]=='Happy' and gender[-1]=='Male' and '(8-20)' in age[-1] ):
            return render(request,"happy8-20.html",{'name':'Age:8-20!'})
        elif(emotion[-1]=='Happy' and gender[-1]=='Male' and '(20-32)' in age[-1] ):
            return render(request,"happy20-32.html",{'name':'Age:20-32!'})
        elif(emotion[-1]=='Happy' and gender[-1]=='Male' and '(32-50)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:32-50!'})
        elif(emotion[-1]=='Happy' and gender[-1]=='Male' and '(50-100)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:50-100!'})

        if(emotion[-1]=='Angry' and gender[-1]=='Male' and '(0-8)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:0-8!'})        
        elif(emotion[-1]=='Angry' and gender[-1]=='Male' and '(8-20)' in age[-1] ):
            return render(request,"angry8-20.html",{'name':'Age:8-20!'})
        elif(emotion[-1]=='Angry' and gender[-1]=='Male' and '(20-32)' in age[-1] ):
            return render(request,"angry20-32.html",{'name':'Age:20-32!'})
        elif(emotion[-1]=='Angry' and gender[-1]=='Male' and '(32-50)' in age[-1] ):
            return render(request,"angry20-32.html",{'name':'Age:32-50!'})
        elif(emotion[-1]=='Angry' and gender[-1]=='Male' and '(50-100)' in age[-1] ):
            return render(request,"angry20-32.html",{'name':'Age:50-100!'})

        if(emotion[-1]=='Surprise' and gender[-1]=='Male' and '(0-8)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:0-8!'})        
        elif(emotion[-1]=='Surprise' and gender[-1]=='Male' and '(8-20)' in age[-1] ):
            return render(request,"suprise8-20.html",{'name':'Age:8-20!'})
        elif(emotion[-1]=='Surprise' and gender[-1]=='Male' and '(20-32)' in age[-1] ):
            return render(request,"suprise20-32.html",{'name':'Age:20-32!'})
        elif(emotion[-1]=='Surprise' and gender[-1]=='Male' and '(32-50)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:32-50!'})
        elif(emotion[-1]=='Surprise' and gender[-1]=='Male' and '(50-100)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:50-100!'})
        
        if(emotion[-1]=='Sad' and gender[-1]=='Male' and '(0-8)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:0-8!'})        
        elif(emotion[-1]=='Sad' and gender[-1]=='Male' and '(8-20)' in age[-1] ):
            return render(request,"sad8-20.html",{'name':'Age:8-20!'})
        elif(emotion[-1]=='Sad' and gender[-1]=='Male' and '(20-32)' in age[-1] ):
            return render(request,"sad20-32.html",{'name':'Age:20-32!'})
        elif(emotion[-1]=='Sad' and gender[-1]=='Male' and '(32-50)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:32-50!'})
        elif(emotion[-1]=='Sad' and gender[-1]=='Male' and '(50-100)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:50-100!'})

        if(emotion[-1]=='Neutral' and gender[-1]=='Male' and '(0-8)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:0-8!'})        
        elif(emotion[-1]=='Neutral' and gender[-1]=='Male' and '(8-20)' in age[-1] ):
            return render(request,"neutral8-20.html",{'name':'Age:8-20!'})
        elif(emotion[-1]=='Neutral' and gender[-1]=='Male' and '(20-32)' in age[-1] ):
            return render(request,"neutral20-32.html",{'name':'Age:20-32!'})
        elif(emotion[-1]=='Neutral' and gender[-1]=='Male' and '(32-50)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:32-50!'})
        elif(emotion[-1]=='Neutral' and gender[-1]=='Male' and '(50-100)' in age[-1] ):
            return render(request,"playlist.html",{'name':'Age:50-100!'})
        
        else:
            return render(request,"playlist.html",{'name':'Hey Preety Woman!'})