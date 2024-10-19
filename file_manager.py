import os
import shutil
from pathlib import Path
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import asyncio

async def move_file(file_path, target_dir):
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.move(file_path, target_dir / file_path.name)

async def manage_directory():
    directory_path = filedialog.askdirectory(title="Select Directory")
    if not directory_path:
        return

    current_dir = Path(directory_path)
    os.chdir(current_dir)

    # File type mappings to destination directories
    file_mappings = {
        'PDFs': [".pdf"],
        'Excel': [".xls", ".xlsx"],
        'Word': [".doc", ".docx"],
        'PowerPoint': [".ppt", ".pptx"],
        'Text': [".txt", ".rtf"],
        'Codes': [".py", ".java", ".cpp", ".c", ".html", ".css", ".js"],
        'Archive': [".zip", ".rar", ".tar", ".gz"],
        'Applications': [".exe", ".dmg", ".pkg", ".rmskin"],
        'Images': [".jpg", ".jpeg", ".png", ".gif"],
        'Videos': [".mp4", ".avi", ".mov", ".wmv"]
    }

    # Directories for different categories
    category_dirs = {
        'Documents': current_dir / 'Documents',
        'Text': current_dir / 'Documents' / 'Text',
        'Word': current_dir / 'Documents' / 'Word',
        'PowerPoint': current_dir / 'Documents' / 'PowerPoint',
        'Excel': current_dir / 'Documents' / 'Excel',
        'PDFs': current_dir / 'Documents' / 'PDFs',
        'Codes': current_dir / 'Codes',
        'Archive': current_dir / 'Archive',
        'Applications': current_dir / 'Applications',
        'Images': current_dir / 'Images',
        'Videos': current_dir / 'Videos'
    }

    files_to_move = []

    # Iterate over the files in the current directory
    for file_path in current_dir.iterdir():
        if file_path.is_file():
            file_extension = file_path.suffix.lower()
            subdir_name = next((category for category, extensions in file_mappings.items() if file_extension in extensions), None)

            if subdir_name:
                subdirectory_path = category_dirs[subdir_name]
                files_to_move.append((file_path, subdirectory_path))

    # Progress bar setup
    progress_window = Toplevel(window)
    progress_window.title("Processing Files")
    progress_bar = ttk.Progressbar(progress_window, length=300, mode='determinate')
    progress_bar.pack(pady=20)
    progress_label = Label(progress_window, text="Moving files...")
    progress_label.pack()

    total_files = len(files_to_move)

    # Move files asynchronously and update progress
    for index, (file_path, subdirectory_path) in enumerate(files_to_move):
        await move_file(file_path, subdirectory_path)
        progress_bar['value'] = (index + 1) / total_files * 100
        progress_window.update_idletasks()

    progress_window.destroy()
    messagebox.showinfo("File Manager", "Operation completed.")

def run_async_task():
    asyncio.run(manage_directory())

# Main window setup
window = Tk()
height = 480
width = 960
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry(f'{width}x{height}+{x}+{y}')

window.configure(bg="#000000")
window.overrideredirect(True)

# Background Image
backgroundImage = PhotoImage(file=r"assets/Background.png")
bg_image = Label(window, image=backgroundImage, bg="#000000")
bg_image.place(x=0, y=0)

# Using standard Button instead of ttk Button
bg_image_1 = PhotoImage(file=r"assets/button.png")
submit_button = Button(window, image=bg_image_1, text="Select Directory", bg="#000000", fg="white", borderwidth=0, relief="flat",
                       cursor="hand2", activebackground="#000000", command=run_async_task)
submit_button.place(x=90, y=290, width=220, height=40)

# Exit button
bg_image_2 = PhotoImage(file=r"assets/Exit.png")
exit_button = Button(window, image=bg_image_2, text="Exit", bg="#000000", fg="white", borderwidth=0, relief="flat",
                     cursor="hand2", activebackground="#000000", command=quit)
exit_button.place(x=140, y=420, width=110, height=40)

window.resizable(False, False)
window.mainloop()
