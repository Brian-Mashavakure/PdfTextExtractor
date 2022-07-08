from argparse import FileType
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

from matplotlib.pyplot import text

root = tk.Tk()
#all elements of the interface should be inbetween the root declarations
canvas = tk.Canvas(root, width=600, height = 300)
canvas.grid(columnspan=3, rowspan=3)

#logo

unsized_logo = Image.open('logo2.png')
logo = unsized_logo.resize((200,100), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)#adding logo into a tkinter widget
logo_label.image = logo
logo_label.grid(column=1, row = 0)#column from when columnspan was declared with the canvas


#Instructions
instructions = tk.Label(root, text="Select A Pdf File On Your Computer To Extract Its Text",font='static/Raleway-Black.ttf')
#placing label on the grid
instructions.grid(columnspan=3, column = 0, row=1)



def open_file():
    browseText.set("Loading.......")
    file = askopenfile(parent=root, mode="rb",title="Choose A File",filetypes=[("Pdf","*.pdf")])
    if file == True:
        readPdf = PyPDF2.PdfFileReader(file)
        page = readPdf.getPage(0)
        pageContent = page.extract_text()
        print(pageContent)

        #text box
        textBox = tk.Text(root, height=10,width=50,padx=15,pady=15)
        textBox.insert(1.0,pageContent)
        textBox.tag_configure('center',justify='center')
        textBox.tag_add('center',1.0,'end')
        textBox.grid(column=1,row=3)

        browseText.set("Browse")


    

#Browse Button
#should open a browse dialog box
browseText = tk.StringVar()
browseBtn = tk.Button(root, textvariable=browseText,command=lambda:open_file(),font='static/Raleway-Black.ttf', bg='#1919ff',fg='#fff',height=2, width=15)
browseText.set("Browse")

browseBtn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height = 250)
canvas.grid(columnspan=3)


root.mainloop()

