import os
import shutil
from pathlib import Path
from colorama import Fore, Back, Style

## Downloads Directory
print(Fore.LIGHTMAGENTA_EX + """
 

    _______ __                                                   
   / ____(_) /__     ____ ___  ____ _____  ____ _____ ____  _____
  / /_  / / / _ \   / __ `__ \/ __ `/ __ \/ __ `/ __ `/ _ \/ ___/
 / __/ / / /  __/  / / / / / / /_/ / / / / /_/ / /_/ /  __/ /    
/_/   /_/_/\___/  /_/ /_/ /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                                              /____/          V 1.0  

    
Find me on X :_TurkI0S

""")

print("""1- Orgnize Downloads Folder
2- Coming Soon""")
User = input()
if int(User) != 1:
    print("Other Futures Coming Soon ^_^")
else:
    print(Fore.LIGHTGREEN_EX)
## Creating Documents Folder (Documents)
    current_dir = Path.home() / 'Downloads'
    os.chdir(current_dir)

    for filename in os.listdir(current_dir):

        if filename.lower().endswith((".pdf",".doc",".docx",".pptx",".ppt",".xls",".xlsx",".txt")):
        ## Creating folder "Documents" to hold files
            if not os.path.exists(Path.home() / 'Downloads' / 'Documents'):
                os.mkdir(Path.home() / 'Downloads' / 'Documents')
            shutil.copy2(filename, "Documents")
            os.remove(filename)
    print("Documents Folder Created")

    ## Creating other folders (PDF)

    documents_dir =  Path.home() / 'Downloads' / 'Documents'
    os.chdir(documents_dir)

    for filename in os.listdir(documents_dir):
        if filename.lower().endswith((".pdf")):
            if not os.path.exists(Path.home() / 'Downloads' / 'Documents' / 'PDF'):
                os.mkdir(Path.home() / 'Downloads' / 'Documents' / 'PDF')
            shutil.copy2(filename, "PDF")
            os.remove(filename)
            print(filename, "--> Done (PDF)")
    print("PDF Folder complete")

## Creating other folders (Text)

    for filename in os.listdir(documents_dir):
        if filename.lower().endswith((".txt")):
            if not os.path.exists(Path.home() / 'Downloads' / 'Documents' / 'Text'):
                os.mkdir(Path.home() / 'Downloads' / 'Documents' / 'Text')
            shutil.copy2(filename, "Text")
            os.remove(filename)
            print(filename, "--> Done (Text)")
    print("Text Folder complete")


## Creating other folders (Word)

    for filename in os.listdir(documents_dir):
        if filename.lower().endswith((".doc",".docx")):
            if not os.path.exists(Path.home() / 'Downloads' / 'Documents' / 'Word'):
                os.mkdir(Path.home() / 'Downloads' / 'Documents' / 'Word')
            shutil.copy2(filename, "Word")
            os.remove(filename)
            print(filename, "--> Done (Word)")
    print("Word Folder complete")

    ## Creating other folders (PowerPoint)

    for filename in os.listdir(documents_dir):
        if filename.lower().endswith((".ppt",".pptx")):
            if not os.path.exists(Path.home() / 'Downloads' / 'Documents' / 'PowerPoint'):
                os.mkdir(Path.home() / 'Downloads' / 'Documents' / 'PowerPoint')
            shutil.copy2(filename, "PowerPoint")
            os.remove(filename)
            print(filename, "--> Done (PowerPoint)")
    print("PowerPoint Folder complete")

    ## Creating other folders (Excel)

    for filename in os.listdir(documents_dir):
        if filename.lower().endswith((".xls",".xlsx")):
            if not os.path.exists(Path.home() / 'Downloads' / 'Documents' / 'Excel'):
                os.mkdir(Path.home() / 'Downloads' / 'Documents' / 'Excel')
            shutil.copy2(filename, "Excel")
            os.remove(filename)
            print(filename, "--> Done (Excel)")
    print("Excel Folder complete")

    ## Creating Images Folder (Images)

    os.chdir(current_dir)

    for filename in os.listdir(current_dir):

        if filename.lower().endswith((".jpeg",".jpg",".gif",".tiff",".raw","png")):
        ## Creating folder "Images" to hold files
            if not os.path.exists(Path.home() / 'Downloads' / 'Images'):
                os.mkdir(Path.home() / 'Downloads' / 'Images')
            shutil.copy2(filename, "Images")
            os.remove(filename)
    print("Images Folder Created")

    ## Creating Videos Folder (Videos)

    for filename in os.listdir(current_dir):

        if filename.lower().endswith((".mp4",".mov",".avi",".wmv",".avchd",".webm","flv")):
        ## Creating folder "Videos" to hold files
            if not os.path.exists(Path.home() / 'Downloads' / 'Videos'):
                os.mkdir(Path.home() / 'Downloads' / 'Videos')
            shutil.copy2(filename, "Videos")
            os.remove(filename)
    print("Videos Folder Created")

    ## Creating Applications Folder (Applications)

    for filename in os.listdir(current_dir):

        if filename.lower().endswith((".exe",".bat","rmskin")):
        ## Creating folder "Applications" to hold files
            if not os.path.exists(Path.home() / 'Downloads' / 'Applications'):
                os.mkdir(Path.home() / 'Downloads' / 'Applications')
            shutil.copy2(filename, "Applications")
            os.remove(filename)
    print("Applications Folder Created")
    print(Fore.LIGHTYELLOW_EX)
    print("Processing.... it may take a few minutes")
    print(Fore.LIGHTGREEN_EX)
    ## Creating Archive Folder (Archive)

    for filename in os.listdir(current_dir):

        if filename.lower().endswith((".tar",".rar",".zip",".genozip",".sfark",".7z",".ace",".apk")):
        ## Creating folder "Archive" to hold files
            if not os.path.exists(Path.home() / 'Downloads' / 'Archive'):
                os.mkdir(Path.home() / 'Downloads' / 'Archive')
            shutil.copy2(filename, "Archive")
            os.remove(filename)
    print("Archive Folder Created")

    ## Creating Codes Folder (Codes)

    for filename in os.listdir(current_dir):

        if filename.lower().endswith((".java",".c",".c++",".cpp",".html",".py")):
        ## Creating folder "Codes" to hold files
            if not os.path.exists(Path.home() / 'Downloads' / 'Codes'):
                os.mkdir(Path.home() / 'Downloads' / 'Codes')
            shutil.copy2(filename, "Codes")
            os.remove(filename)
    print("Codes Folder Created")

    ## Creating other folders (Python)

    Codes_dir =  Path.home() / 'Downloads' / 'Codes'
    os.chdir(Codes_dir)

    for filename in os.listdir(Codes_dir):
        if filename.lower().endswith((".py")):
            if not os.path.exists(Path.home() / 'Downloads' / 'Codes' / 'Python'):
                os.mkdir(Path.home() / 'Downloads'/ 'Codes' / 'Python')
            shutil.copy2(filename, "Python")
            os.remove(filename)
            print(filename, "--> Done (Python)")
    print("Python Folder complete")

    ## Creating other folders (WEB)

    for filename in os.listdir(Codes_dir):
        if filename.lower().endswith((".html")):
            if not os.path.exists(Path.home() / 'Downloads' / 'Codes' / 'WEB'):
                os.mkdir(Path.home() / 'Downloads' / 'Codes' / 'WEB')
            shutil.copy2(filename, "WEB")
            os.remove(filename)
            print(filename, "--> Done (WEB)")
    print("WEB Folder complete")

    ## Creating other folders (C++)

    for filename in os.listdir(Codes_dir):
        if filename.lower().endswith((".c++","cpp")):
            if not os.path.exists(Path.home() / 'Downloads' / 'Codes' / 'C++'):
                os.mkdir(Path.home() / 'Downloads' / 'Codes' / 'C++')
            shutil.copy2(filename, "C++")
            os.remove(filename)
            print(filename, "--> Done (C++)")
    print("C++ Folder complete")

    ## Creating other folders (C)

    for filename in os.listdir(Codes_dir):
        if filename.lower().endswith((".c")):
            if not os.path.exists(Path.home() / 'Downloads' / 'Codes' / 'C'):
                os.mkdir(Path.home() / 'Downloads' / 'Codes' / 'C')
            shutil.copy2(filename, "C")
            os.remove(filename)
            print(filename, "--> Done (C)")
    print("C Folder complete")

    ## Creating other folders (Java)

    for filename in os.listdir(Codes_dir):
        if filename.lower().endswith((".java")):
            if not os.path.exists(Path.home() / 'Downloads' / 'Codes' / 'Java'):
                os.mkdir(Path.home() / 'Downloads' / 'Codes' / 'Java')
            shutil.copy2(filename, "Java")
            os.remove(filename)
            print(filename, "--> Done (Java)")
    print("Java Folder complete")
    print(Fore.LIGHTMAGENTA_EX)
    print("""
Exiting Program...

Done good to go 
          
          
          """)
print(Style.RESET_ALL)

