
import cv2
import asyncio
import socket
import nest_asyncio

nest_asyncio.apply()

host = "192.168.1.101"
port = 12345

cap=cv2.VideoCapture(0)
mycascade = cv2.CascadeClassifier("mycascade\classifier\\cascade.xml")
font1=cv2.FONT_HERSHEY_SIMPLEX


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
async def ss():
    c, addr = s.accept()
    print('Gelen bağlantı:', addr) 
    await asyncio.sleep(1)
    mesaj = 'Bağlantı sağlandı'
    c.send(mesaj.encode('utf-8'))
    c.close()
    
  

async def main():
    while True:
    
    
    
        ret,frame =cap.read()
        frame=cv2.flip(frame,1)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
        pencils=mycascade.detectMultiScale(gray,1.3,7)
        for(x,y,w,h) in pencils:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,"MAVİ kalem",(x,y),font1,1,(255,0,0),cv2.LINE_4)
            # 
            task = asyncio.create_task(ss())   
            # 
            cv2.imshow("ff",frame)
    
    
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
    
    cap.release()
    cv2.destroyAllWindows()
 
asyncio.run(main())