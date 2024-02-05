import customtkinter as ctk
from tkinter import messagebox
import os
import shutil
from pathlib import Path
from tkinter import filedialog


# Basic parameters and initializations
appWidth, appHeight = 700, 400

# Supported modes: Light, Dark, System
ctk.set_appearance_mode("Dark")


# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("dark-blue")

# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove title bar
        self.overrideredirect(True)

        screen_width = self.winfo_screenwidth() + 215
        screen_height = self.winfo_screenheight() + 50

        x = int((screen_width / 2) - (appWidth / 2))
        y = int((screen_height / 2) - (appHeight / 2))

        self.title("File Manager")
        self.geometry(f"{appWidth}x{appHeight}+{x}+{y}")

        # Set the transparency level of the window to 95%
        self.attributes("-alpha", 0.95)

        # File Manager Label
        self.FMLabel = ctk.CTkLabel(self, text="File Manager",text_color="#47CA86", font=("Ubuntu Medium",15))
        self.FMLabel.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        # Manage Label
        self.manageLabel = ctk.CTkLabel(self, text="Manage Your Directories",text_color="#bff8da", font=("Ubuntu",42))
        self.manageLabel.grid(row=1, column=0, columnspan=3, padx=20, pady=1, sticky="ew")

        # Author Label
        self.FMLabel = ctk.CTkLabel(self, text="By TurkIOS",text_color="#bff8da", font=("Ubuntu",20))
        self.FMLabel.grid(row=2, column=0, columnspan=3, padx=20, pady=1, sticky="ew")

        # Select directory Button
        self.desktop_directory_Button = ctk.CTkButton(self, width=120,height=40,hover_color="#72A088",text_color="#2E4639",fg_color="#b4f4d2", text="Select Directory",font=("Ubuntu",20), command=self.manage_directory)
        self.desktop_directory_Button.grid(row=3, column=0, columnspan=3, padx=250, pady=60, sticky="ew")

        # Quit Button
        self.quit_Button = ctk.CTkButton(self, text="Close", hover_color="#72A088", text_color="#2E4639", fg_color="#b4f4d2" ,command=self.quit)
        self.quit_Button.grid(row=4, column=1, padx=300, pady=70, sticky="ew")
        # Configure row and column to center the label and button
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(1, weight=1)
        # Configure row and column to center the label and button
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(1, weight=1)

    def manage_directory(self):
        root = ctk.CTk()
        root.withdraw()

        directory_path = filedialog.askdirectory(title="Select Directory")
        if not directory_path:
            return

        current_dir = Path(directory_path)
        os.chdir(current_dir)

        # Create directories
        documents_dir = current_dir / 'Documents'
        codes_dir = current_dir / 'Codes'
        archive_dir = current_dir / 'Archive'
        applications_dir = current_dir / 'Applications'
        images_dir = current_dir / 'Images'
        videos_dir = current_dir / 'Videos'

        for directory in [documents_dir, codes_dir, archive_dir, applications_dir, images_dir, videos_dir]:
            if not os.path.exists(directory):
                os.makedirs(directory)

        # Move supported documents to the Documents folder
        supported_documents = (".pdf", ".doc", ".docx", ".pptx", ".ppt", ".xls", ".xlsx", ".txt")
        for filename in os.listdir(current_dir):
            if filename.lower().endswith(supported_documents):
                file_extension = os.path.splitext(filename)[1].lower()

                if file_extension == '.pdf':
                    subdir = Path('PDFs')
                elif file_extension in ('.doc', '.docx'):
                    subdir = Path('Word')
                elif file_extension in ('.ppt', '.pptx'):
                    subdir = Path('PowerPoint')
                elif file_extension in ('.xls', '.xlsx'):
                    subdir = Path('Excel')
                elif file_extension == '.txt':
                    subdir = Path('Text')
                else:
                    continue  # Skip moving if the file extension is not supported

                # Create the subdirectory inside the Documents folder if it doesn't exist
                subdirectory_path = documents_dir / subdir
                if not os.path.exists(subdirectory_path):
                    os.makedirs(subdirectory_path)

                # Move the file to the subdirectory
                shutil.move(os.path.join(current_dir, filename), subdirectory_path)

        # Move code files to the Codes folder
        supported_code_files = (".py", ".java", ".cpp", ".c", ".html", ".css", ".js")
        for filename in os.listdir(current_dir):
            if filename.lower().endswith(supported_code_files):
                shutil.move(os.path.join(current_dir, filename), codes_dir)

        # Move compressed files to the Archive folder
        supported_archive_files = (".zip", ".rar", ".tar", ".gz")
        for filename in os.listdir(current_dir):
            if filename.lower().endswith(supported_archive_files):
                shutil.move(os.path.join(current_dir, filename), archive_dir)

        # Move executable files to the Applications folder
        supported_application_files = (".exe", ".dmg", ".pkg", "rmskin")
        for filename in os.listdir(current_dir):
            if filename.lower().endswith(supported_application_files):
                shutil.move(os.path.join(current_dir, filename), applications_dir)

        # Move image files to the Images folder
        supported_image_files = (".jpg", ".jpeg", ".png", ".gif")
        for filename in os.listdir(current_dir):
            if filename.lower().endswith(supported_image_files):
                shutil.move(os.path.join(current_dir, filename), images_dir)

        # Move video files to the Videos folder
        supported_video_files = (".mp4", ".avi", ".mov", ".wmv")
        for filename in os.listdir(current_dir):
            if filename.lower().endswith(supported_video_files):
                shutil.move(os.path.join(current_dir, filename), videos_dir)

        # Show "Done" message box
        messagebox.showinfo("File Manager", "Operation completed.")


# Create and run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
