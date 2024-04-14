import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()