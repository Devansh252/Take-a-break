import time
import webbrowser
t=0
while(t<10):
    time.sleep(5)
    print("Listen to music")
    webbrowser.open("https://www.spotify.com/in/")
    t+=1
