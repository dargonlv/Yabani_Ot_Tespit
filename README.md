# Yabani_Ot_Tespit

-  ilk olarak Yoosse marklaı kameramızdan görüntü almamamız gerek bunun için bir pyton editörüne ihtiyacamız var.
-  Ben bu projede anaconda içinde bulunan spyder editörünü kullandım.
- kamerdan görüntüler onvif2 olarak alınacaktır bunu için gerekli dönüşüm işlemleri yapılmıştır
- Raspberry , kamera ve pc aynı ağda bulunmalı ve statik ipileri verilmelidir. Bu ipler kodlarda var olan  bölgelerde tekrardan güncellenmeli, aksi takdirde çalışmayacaktır.
- Bu uygulalmada Thread lar kullanımıştır aynı anda hem görüntü alarak hemde raspberrye veri göndermimi sağlanmıştı.
- İp kamera kod kısmında kullanılan ip kamera modeline ve markasına göre değişiklikler olabilir bu uygulamada görüntü alma işlemini uzun araştırma sonucu tekrar kodlayarak elde edilmiştir. Farklı tür kameralarda bu şekilde yürümeye bilir(daha basit olablir). Farklı bir model üzerinde uğraşıyoken bir sorun olursa bana gödünüş sağlaya bilirsiniz.


# Gereksinimler
####  Programlar
- Anaconda x.x
-  python 3.9
- spyder x.x

####Python Kütüphaneler
    import cv2 #opencv
	import socket
	import threading
	from threading import Event
	import subprocess as sp
	import numpy as 



##subprocess Hatası
**Python : FileNotFoundError [WinError 2] The system cannot find the file specified , subprocess.py:1582**

subprocess kütüphanesiyle ilgili  bu tarz bir hata alırsanız cözümü aşşağıdaki linktedir. 

`<link>` : <https://stackoverflow.com/questions/73193119/python-filenotfounderror-winerror-2-the-system-cannot-find-the-file-specifie>


## Mycascade

>  cv2.CascadeClassifier("/mycascade(eski)/classifier/cascade.xml")

Mavi kalem Veri setimiz

**birlesmis_hali.py**

	mycascade = cv2.CascadeClassifier("myhaar.xml") # görüntü verilerimzibu kısımda

Ayrı olarak Cascade uygulamasını kurup kendi veri.xml'nizi oluştura bilrisiniz uygulamanın kullanımı internette mevcuttur


##Raspberry

> /raspberry kod/rsperyy_Kod.txt

kodumuzu raspberryde otomatik başlıcak şekilde ayarlamamız gerikiyor.

`<link>` : <https://www.youtube.com/watch?v=5nQ4GcvQac4&list=WL&index=6>

##İp Kamera

ipden alının görüntünün FFmpeg olarak işlenme süreci burada önemli olan kameranızın Height ve Width değerlerinin doğru olması akasi takdirde bozuk görüntü elde etmiş olursunuz .
Bunu öğrenmenin bir yolu ip kameranızı bir program ile bağlanıp fotoğraf çekip öğrene bilirsiniz.

```python
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
```

##Threading

Raspberrye sinay göndermek için kesintisiz sürekli çalışan bir işlem olşturuldu.

```python
    
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
```

##İletişim

mail : faihmer0029@gmail.com

