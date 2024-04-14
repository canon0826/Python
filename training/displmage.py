import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()