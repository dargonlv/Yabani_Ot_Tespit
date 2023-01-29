import cv2
import subprocess as sp
import numpy as np

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

while True:
    raw_frame = process.stdout.read(myCamera_Width * myCamera_Height * 3)
    

    if len(raw_frame) != (myCamera_Width * myCamera_Height * 3):
        print('Error reading frame!')  # Break the loop in case of an error (too few bytes were read).
        break

    # Transform the byte read into a numpy array, and reshape it to video frame dimensions
    frame = np.frombuffer(raw_frame, dtype=np.uint8).reshape((myCamera_Height, myCamera_Width, 3))
    # frame = cv2.resize(frame,(1920,1080))
    
    #telefon tespit
    framegray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    nesne = cv2.imread("telefon_foto.jpg",0)
    w,h = nesne.shape
    res = cv2.matchTemplate(framegray,nesne,cv2.TM_CCOEFF_NORMED)
    
    esikdegeri = 0.72
    
    loc = np.where(res > esikdegeri)
    
    for n in zip(*loc[::-1]):
        cv2.rectangle(frame,n,(n[0]+h,n[1]+w),(0,255,0),1)
            
    
    
    #telefon tespit
    
    
    # kalem tespit
    
    # kalemtespit
    
    # Show frame for testing
    cv2.imshow('frame', frame)
    
    # Check if user is pressing 'ESC'.
    k = cv2.waitKey(1)
    if k == 27:
        break

# Close process and window.
process.stdout.close()
process.wait()
cv2.destroyAllWindows()