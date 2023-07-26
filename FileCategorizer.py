import tkinter as tk
from tkinter import messagebox
import webbrowser
import os 
import shutil
from tkinter import filedialog

def orgnized(path):
    if path!='':
        os.chdir(path=path)

        extensions = {
            ".txt": "Documents",
            ".doc": "Documents",
            ".docx": "Documents",
            ".pdf": "Documents",
            ".xls": "sheet",
            ".xlsx": "sheet",
            ".ppt": "PPTs",
            ".pptx": "PPTs",
            ".csv": "sheet",
            ".jpg": "Images",
            ".jpeg": "Images",
            ".png": "Images",
            ".gif": "Images",
            ".bmp": "Images",
            ".mp3": "Music",
            ".wav": "Music",
            ".mp4": "Videos",
            ".avi": "Videos",
            ".mkv": "Videos",
            ".zip": "Archive File",
            ".rar": "Archive File",
            ".7z": "Archive File",
            ".exe": "system",
            ".dmg": "system",
            ".app": "system",
            ".py": "codes",
            ".json": "codes",
            ".xml": "codes",
            ".html": "codes",
            ".css": "codes",
            ".js": "codes",
            ".cpp": "codes",
            ".java": "codes",
            ".c": "codes",
            ".h": "codes",
            ".txt": "Documents",
            ".md": "Documents",
            ".log": "Documents",
            ".ppt": "PPTs",
            ".pptx": "PPTs",
            ".key": "PPTs",
            ".pages": "Documents",
            ".numbers": "sheet",
        }

        def createorgetfolder(name):

            if name != None:
                if os.path.exists(name):
                    print('isalresy present')
                else:
                    os.makedirs(name)
                    print('file craeted')
            else:
                print('something went wrrong')

        files = os.listdir()

        for file in files:
            
            if os.path.isfile(file):
                filename,filextension = os.path.splitext(file)
                
                foldername  = extensions.get(filextension)
                if foldername != None:
                    createorgetfolder(foldername)  
                
                    shutil.move(file,foldername)

                else:
                    foldername = 'others'
                    createorgetfolder(foldername)
                    shutil.move(file,foldername)
                    

                
            else:
                print('no files is exists')
            
        
        messagebox.showinfo("Message", "your folder was organized")
    else:
        messagebox.showinfo("Message", "No folder is selected")

def callback(url):
    webbrowser.open_new(url)

def get_folder_path():
    folder_path = filedialog.askdirectory()
    print("Selected folder path:", folder_path)
    orgnized(folder_path)


def main():
    root = tk.Tk()
    root.title("FileCategorizer")
    root.geometry("500x200")
    text = tk.Label(root,text="Welcome to FileCategorizer by John francis",font=('Helvetica',18,'bold'),foreground='red')
    text.pack(pady=5)
    text = tk.Label(root,text="Choose a folder to organize")
    text.pack(pady=10)
    button = tk.Button(root, text="Select Folder", command=lambda:[get_folder_path()])
    button.pack(pady=10)

    
    feedback = tk.Label(root,text="If you have faced any bug, report it here.",foreground='blue',cursor="hand")
    feedback.pack(side=tk.BOTTOM,pady=3)
    feedback.bind("<Button-1>",lambda e:callback("https://www.instagram.com/francis.exe/"))
    

    root.mainloop()

if __name__ == "__main__":
    main()