import cv2

import socket
import threading
from threading import Event
import subprocess as sp
import numpy as np

# 
# Settings ip-camera (Gembird, ICAM-WRHD-01).
myCamera_Name = "Gembird"
myCamera_Link = "rtsp://admin:Konak1515@192.168.1.105:554/onvif2"
myCamera_Height = 360
myCamera_Width = 640

FFMPEG_BIN = "ffmpeg"  # Works with Windows when ffmpeg.exe is in the path.
ffmpeg_cmd = [FFMPEG_BIN,
              '-nostdin',
              '-rtsp_transport', 'udp',
              '-max_delay', '30000000',  # 30 seconds
              '-i', myCamera_Link,
              '-f', 'rawvideo',
              '-pix_fmt', 'bgr24',
              '-vcodec', 'rawvideo', '-an', 'pipe:']

# Open sub-process that gets in_stream as input and uses stdout as an output PIPE.
process = sp.Popen(ffmpeg_cmd, stdout=sp.PIPE)
# 


# raspberry 
host = "192.168.1.101"
port = 12345

cap=cv2.VideoCapture(0)
mycascade = cv2.CascadeClassifier("myhaar.xml")
font1=cv2.FONT_HERSHEY_SIMPLEX

global var
var=False
global deger
# 

# 
# 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket oluşturuldu")

    s.bind((host, port))
    print("socket {} nolu porta bağlandı".format(port))

    s.listen(5)
    print("socket dinleniyor")

except socket.error as msg:
    print("Hata:", msg)
#




    
    
def ss(event):
    
    while True:
        
            c, addr = s.accept()
            print('Gelen bağlantı:', addr) 
    
            mesaj = 'Bağlantı sağlandı'
            if var:
                c.send(mesaj.encode('utf-8'))
                print("başarılı")
                
                
            c.close()
            
            if event.is_set():
                break
            

event=Event() 
               
# t2 = threading.Thread(target=zamanlayici, args=()) 
# t2.start()          
    
t1 = threading.Thread(target=ss, args = (event,))  
t1.start()

while True:

    
    raw_frame = process.stdout.read(myCamera_Width * myCamera_Height * 3)
     

    if len(raw_frame) != (myCamera_Width * myCamera_Height * 3):
        print('Error reading frame!')  # Break the loop in case of an error (too few bytes were read).
        break

    # Transform the byte read into a numpy array, and reshape it to video frame dimensions
    frame = np.frombuffer(raw_frame, dtype=np.uint8).reshape((myCamera_Height, myCamera_Width, 3))
    # frame = cv2.resize(frame,(1920,1080))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    pencils=mycascade.detectMultiScale(gray,1.5,1)
    for(x,y,w,h) in pencils:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,"MAVİ kalem",(x,y),font1,1,(255,0,0),cv2.LINE_4)
        # 
        
        var=True
        # 
    cv2.imshow("ff",frame)
    
    
    
    cv2.waitKey(50)
    var=False
    
    
        
 
    
    
    if cv2.waitKey(1) & 0xFF==ord("q"):
        event.set()
        t1.join()
        break

process.stdout.close()
process.wait()
cap.release()
cv2.destroyAllWindows()