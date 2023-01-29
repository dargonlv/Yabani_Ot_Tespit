import socket
import _thread





host = "192.168.1.101"
port = 12345 
def oldu():
    print("oldu")

def baglanti(h,p):
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("socket oluşturuldu")

        s.bind((h, p))
        print("socket {} nolu porta bağlandı".format(p))

        s.listen(5)
        print("socket dinleniyor")

    except socket.error as msg:
        print("Hata:", msg)
# 

       
    while True:
         c, addr = s.accept()
         print('Gelen bağlantı:', addr) 
            
         mesaj = 'Bağlantı sağlandı'
         c.send(mesaj.encode('utf-8'))
         c.close()
        
_thread.start_new_thread(baglanti(host, port))    
_thread.start_new_thread(oldu())    

        
      