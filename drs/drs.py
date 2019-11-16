import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading # to load another image at samae rate
import time
import imutils


SET_WIDTH = 650
SET_HEIGHT = 340


stream = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag



def pending(decision):
    '''
    1. Display Decision pending image
    2 wait for second 
    3 display sponsor image
    4 wait for 1.5 second
    5 Display out/notout image'''
    
    
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH , height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray( frame))
    canvas.image = frame
    canvas.create_image(0, 0 , image=frame , anchor = tkinter.NW)
    time.sleep(1)
    
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH , height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray( frame))
    canvas.image = frame
    canvas.create_image(0, 0 , image=frame , anchor = tkinter.NW)
    
    time.sleep(2.5)
    '''
    if decision == 'out':
        decision_img = 'out.png'
    else:
        decision_img = 'not_out.png'
   
    frame = cv2.cvtColor(cv2.imread(decision_img), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH , height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray( frame))
    canvas.image = frame
    canvas.create_image(0, 0 , image=frame , anchor = tkinter.NW)'''
    
    if decision == 'out':
        decisionImg = "out.png"
    else:
        decisionImg = "not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    
    

    
def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")
    
window = tkinter.Tk() # to make GUI window
window.title(" Third Umpire Decision Review Kit")
canvas = tkinter.Canvas(window, width = SET_WIDTH, height= SET_HEIGHT)

cv_img = cv2.cvtColor(cv2.imread('welcome.png'), cv2.COLOR_BGR2RGB)
cv_img = imutils.resize(cv_img, width =SET_WIDTH , height = SET_HEIGHT)
#to set image ingui
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
#to work allthis thing we need to pack in canvas we r packing in canvas
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()


#BUTTONS TO CONTRO PLAY BACK
btn = tkinter.Button(window, text="<<Previous (fast)", width=50,command = partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<<Previous (slow)",width=50, command = partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="GiveOut",width=50, command = out)
btn.pack()

btn = tkinter.Button(window, text="Give Not OUT",width=50, command = not_out)
btn.pack()

btn = tkinter.Button(window, text="Next (fast)>>",width=50, command = partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Next (slow)>>",width=50, command = partial(play, 2))
btn.pack()

window.mainloop()

