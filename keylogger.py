
import time
from pynput import keyboard

words=""
sentence=""
counter=0
def printer(key):
     global words
     global sentence
     global counter
     words+=key.char
     sentence += str(words)
     local_time = time.ctime()
     if "show" in sentence :
       print(words)
       print(local_time)
       words=""
       sentence=""
     if key.char=='.':
       l.stop()
l = keyboard.Listener(printer)
# if __name__=="__main__":
l.start()
l.join()
