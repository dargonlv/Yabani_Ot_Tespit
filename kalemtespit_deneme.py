
import cv2
import time
import socket
import threading
from threading import Event

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

    
    ret,frame =cap.read()
    frame=cv2.flip(frame,1)
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


cap.release()
cv2.destroyAllWindows()