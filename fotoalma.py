import ffmpeg

stream = ffmpeg.input("rtsp://admin:Konak1515@192.167.1.105:554/onvif1", ss=0)
file = stream.output("test.png", vframes=1)
testfile = file.run(capture_stdout=True, capture_stderr=True)