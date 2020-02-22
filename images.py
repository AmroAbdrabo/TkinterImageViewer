from tkinter import *
from PIL import ImageTk, Image 
from os import listdir
from os.path import isfile, join

thumbX = 700
thumbY = 700
labelY = 600
mypath = "/Users/amroa/Downloads"
files = [f for f in listdir(mypath) if isfile(join(mypath, f)) and (f[-3:].lower() == 'jpg' or f[-4:].lower() == 'jpeg' or f[-3:].lower() == 'png' )]
img_index = 0

root = Tk() 
root.title('Learn to code at Codemy.com')
my_label = Label()

status = Label(root, text = "Image 1 of " + str(len(files)), bd = 3, relief = SUNKEN, anchor = E)

def forward():
    global img_index
    global my_label
    global img  # important otherwise img is local and garbage collected
    global button_forth
    global button_back

    img_index = min(len(files)-1, img_index + 1)

    my_label.grid_forget()

    img_pre = Image.open(join(mypath, files[img_index]))
    img_pre.thumbnail((thumbX, thumbY))
    img = ImageTk.PhotoImage(img_pre)

    my_label = Label(image = img, width  = 700, height = labelY)
    my_label.grid(row = 0, column = 0, columnspan = 3)

    if img_index == (len(files) - 1):
        button_forth.config(state = 'disabled')

    button_back.config(state = 'normal')
    status.config(text = "Image " + str(img_index+1)+ " of " + str(len(files)))
    
    return

def back():
    global img_index
    global my_label
    global img # important otherwise img is local and garbage collected
    global button_back
    global button_forth

    img_index = max(0, img_index - 1)
    my_label.grid_forget()
    
    img_pre = Image.open(join(mypath, files[img_index]))
    img_pre.thumbnail((thumbX, thumbY))
    img = ImageTk.PhotoImage(img_pre)

    my_label = Label(image = img, width = 700, height = labelY)
    my_label.grid(row = 0, column = 0, columnspan = 3)

    if img_index == 0:
        button_back.config(state = 'disabled')

    button_forth.config(state = 'normal')
    status.config(text = "Image " + str(img_index+1)+ " of " + str(len(files)))

    return


#root.iconbitmap("/Users/amroa/Qt/5.14.1/Src/qtbase/tests/benchmarks/gui/image/qimagereader/images/teapot.ppm")
img_pre = Image.open(join(mypath, files[0]))
img_pre.thumbnail((thumbX, thumbY))
img = ImageTk.PhotoImage(img_pre)
my_label = Label(image = img, width  = 700, height = labelY)
my_label.grid(row = 0, column = 0, columnspan = 3)

button_back = Button(root, text = "<<", command = back)
button_quit = Button(root, text = "Exit Program", command  = root.quit)
button_forth = Button(root, text = ">>", command = forward)

button_back.grid(row=1, column = 0)
button_quit.grid(row=1, column = 1)
button_forth.grid(row=1, column = 2, pady = 8)
status.grid(row=2, column =0, pady=11, columnspan = 3, sticky = W+E)

root.mainloop()