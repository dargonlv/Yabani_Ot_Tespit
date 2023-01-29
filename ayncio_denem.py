import cv2
import asyncio
import nest_asyncio
nest_asyncio.apply()

cap=cv2.VideoCapture(0)

async def main():
    
        print("tim")
        
        
        await asyncio.sleep(1)
    
async def foo():
    
        ret, frame = cap.read()#frame sayııyor varsa devam ediyor
        frame=cv2.flip(frame,1)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        
        if ret == True:
            
            cv2.imshow("video",frame)
            task = asyncio.create_task(main())
        
    
while True:    
    asyncio.get_event_loop().run_until_complete(foo())
    if cv2.waitKey(1) & 0xFF == ord("b"):
        break    
    
cap.release()
cv2.destroyAllWindows()