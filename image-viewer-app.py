from tkinter import *
from PIL import Image,ImageTk

# trials for image viewer

root = Tk()
root.title("Image Viewer")
root.iconbitmap('E:\Joshua/Personal/Joshua Pics/python image viewer photographs/literally-just-me.ico')

# the images

my_img1 = ImageTk.PhotoImage(Image.open("E:\Joshua/Personal/icons n stuff/Drawings/boy.png"))
my_img2 = ImageTk.PhotoImage(Image.open("E:\Joshua/Personal/icons n stuff/Drawings/surp.png"))
my_img3 = ImageTk.PhotoImage(Image.open("E:\Joshua/Personal/icons n stuff/Drawings/heart.png"))
my_img4 = ImageTk.PhotoImage(Image.open("E:\Joshua/Personal/icons n stuff/Drawings/smile.png"))
my_img5 = ImageTk.PhotoImage(Image.open("E:\Joshua/Personal/icons n stuff/Drawings/sob.png"))

# variable, image list

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# status bar
status = Label(root, text="Image 1 of" + str(len(image_list)), bd=1, relief=SUNKEN)

# label 1
my_Label = Label(image=my_img1)
my_Label.grid(row=0, column=0, columnspan=3)

# functions


def forward(image_number):
    global my_Label
    global button_forward
    global button_back

    my_Label.grid_forget()
    my_Label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>",command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_Label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text="Image "+ str(image_number) +" of" + str(len(image_list)), bd=1, relief=SUNKEN)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global my_Label
    global button_forward
    global button_back

    my_Label.grid_forget()
    my_Label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>",command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_Label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text="Image "+ str(image_number) +" of" + str(len(image_list)), bd=1, relief=SUNKEN)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)



# buttons

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="CLOSE", command= root.quit)
button_forward = Button(root, text=">>",command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# fin

root.mainloop()

