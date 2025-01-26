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

    file_mappings = {
        'Documents': {
            'Word': [".doc", ".docx", ".dot", ".dotx", ".dotm", ".docm", ".wps", ".wpd", ".wp", ".sdw", ".sdx"],
            'PDF': [".pdf", ".xps"],
            'Presentations': [".ppt", ".pptx", ".key"],
            'Spreadsheets': [".xls", ".xlsx", ".csv", ".xlt", ".xltx"],
            'Text': [".txt", ".rtf", ".md", ".log", ".asciidoc"],
            'Other': [".odt", ".xml", ".epub", ".pages", ".eml", ".msg", ".odf", ".tex", ".hwp", ".mobi", ".xmind"]
        },
        'Images': {
            'JPEG': [".jpg", ".jpeg", ".jfif", ".jpe", ".jif"],
            'PNG': [".png"],
            'GIF': [".gif"],
            'BMP': [".bmp"],
            'TIFF': [".tiff"],
            'SVG': [".svg", ".svgz"],
            'RAW': [".raw", ".cr2", ".nef", ".dng", ".arw", ".orf"],
            'WebP': [".webp"],
            'HEIC': [".heic"],
            'Vector': [".ai", ".eps"],
            'Other': [".indd", ".pbm", ".pgm", ".ppm", ".ico", ".cur", ".tga", ".exif", ".wdp", ".apng", ".avif", ".fpx", ".sct", ".dcm", ".pcx", ".wbmp"]
        },
        'Audio': {
            'MP3': [".mp3"],
            'WAV': [".wav", ".wavs"],
            'AAC': [".aac", ".m4a", ".m4b", ".m4p"],
            'FLAC': [".flac"],
            'Other': [".ogg", ".wma", ".aiff", ".aif", ".mid", ".midi", ".opus", ".ra", ".ram", ".dsf", ".wv", ".mka", ".3gp", ".3gpp", ".mpa", ".au", ".snd", ".cda", ".dss", ".dts", ".m3u", ".m3u8", ".pls", ".cue", ".dff", ".aax", ".m4r"]
        },
        'Video': {
            'MP4': [".mp4", ".m4v"],
            'MKV': [".mkv"],
            'AVI': [".avi"],
            'MOV': [".mov"],
            'WMV': [".wmv"],
            'FLV': [".flv"],
            'WebM': [".webm"],
            'Other': [".mpg", ".mpeg", ".3gp", ".3gpp", ".f4v", ".rm", ".vob", ".ts", ".divx", ".xvid", ".m2ts", ".mxf", ".drc", ".pk", ".srt", ".ass", ".sub", ".ogv", ".dvr-ms", ".iso", ".h264", ".h265", ".rmvb", ".mpv", ".f4p", ".f4a", ".mjpeg", ".m4s"]
        },
        'Archives': {
            'ZIP': [".zip", ".zipx"],
            'RAR': [".rar", ".rar5"],
            '7Z': [".7z"],
            'Tar': [".tar", ".tar.gz", ".tar.bz2", ".tar.xz"],
            'GZ': [".gz"],
            'BZ2': [".bz2"],
            'XZ': [".xz"],
            'Other': [".cab", ".lz", ".z", ".ace", ".apk", ".arj", ".dmg", ".sitx", ".tgz", ".lzip", ".pax", ".zpaq", ".cbr", ".cbz", ".ar", ".cpio", ".wim", ".vhd", ".ico", ".bzip", ".cpgz", ".p7zip", ".lzma", ".zst"]
        },
        'Designs': {
            'Adobe': [".ai", ".psd", ".indd", ".fla"],
            'CAD': [".dwg", ".dxf"],
            'Vector': [".svg", ".eps"],
            '3D': [".fbx", ".3ds", ".blend", ".max", ".obj", ".stl", ".gcode", ".c4d", ".mmd", ".3dm", ".3dml"],
            'Other': [".pdf", ".cdr", ".sketch", ".dgn", ".sai", ".rvt", ".3dmf", ".kmz", ".dae", ".lwo"]
        },
        'Database': {
            'SQL': [".sql", ".dbs", ".pql", ".ql"],
            'SQLite': [".sqlite", ".sqlitedb"],
            'Access': [".mdb", ".accdb", ".acc"],
            'Other': [".db", ".csv", ".dbf", ".par", ".pdb", ".fdb", ".ndb", ".ora", ".dmp", ".tde", ".myd", ".myi", ".cvs", ".fbf", ".tsv", ".xql", ".4d"]
        },
        'Web': {
            'HTML': [".html", ".htm", ".xhtml", ".phtml"],
            'CSS': [".css", ".scss", ".less"],
            'JavaScript': [".js", ".mjs"],
            'JSON': [".json"],
            'XML': [".xml", ".dtd"],
            'Other': [".svg", ".asp", ".jsp", ".php", ".woff", ".woff2", ".webmanifest", ".rss", ".atom", ".yaml", ".yml", ".svgz", ".wasm", ".map", ".txt", ".pl", ".md", ".webp"]
        },
        'Miscellaneous': {
            'Executables': [".exe", ".bin"],
            'System': [".dll", ".sys", ".ini", ".cfg"],
            'Disk Images': [".iso", ".img", ".dmg"],
            'Logs': [".log"],
            'Temporary': [".tmp", ".crdownload", ".part"],
            'Backup': [".bak", ".sav", ".bkp", ".old"],
            'Other': [".settings", ".srt", ".nfo", ".crx", ".pkg", ".flp", ".wim", ".cpl", ".hqx", ".msi", ".qbb", ".bqi", ".dmp", ".lock", ".swp", ".con", ".pdb", ".o"]
        },
        'Fonts': {
            'TrueType': [".ttf"],
            'OpenType': [".otf"],
            'Web': [".woff", ".woff2"],
            'Other': [".fnt", ".fon", ".eot", ".svg", ".ttc", ".pfa", ".pfb", ".bmap", ".dfont", ".bitmap", ".pf", ".so"]
        },
        'Programming': {
            'C/C++': [".c", ".cpp", ".h", ".hpp"],
            'C#': [".cs"],
            'Go': [".go"],
            'Java': [".java"],
            'JavaScript': [".js"],
            'Kotlin': [".kt"],
            'Python': [".py"],
            'Ruby': [".rb"],
            'Rust': [".rs"],
            'Other': [".pl", ".sh", ".bat", ".php", ".sql"],
            'JavaScript': [".js", ".mjs"],
            'PHP': [".php"],
            'Ruby': [".rb"],
            'Shell': [".sh", ".batch"],
            'Perl': [".pl"],
            'Batch': [".bat"],
            'PowerShell': [".ps1"],
            'HTML': [".html", ".htm"],
            'CSS': [".css", ".scss", ".less"],
            'Other': [".json", ".xml", ".asp", ".jsp", ".sql", ".vbs", ".go", ".swift", ".r", ".lua", ".ts", ".coffee", ".d", ".vb", ".f", ".clj", ".scad", ".dart",".pl", ".sh", ".bat", ".php", ".sql"]
        }
    }

    category_dirs = {
        'Documents': Path("Documents"),
        'Images': Path("Images"),
        'Audio': Path("Audio"),
        'Video': Path("Video"),
        'Archives': Path("Archives"),
        'Scripts': Path("Scripts"),
        'Designs': Path("Designs"),
        'Database': Path("Database"),
        'Web': Path("Web"),
        'Miscellaneous': Path("Miscellaneous"),
        'Fonts': Path("Fonts"),
        'Programming': Path("Programming"),
    }

    files_to_move = []

    for file_path in current_dir.iterdir():
        if file_path.is_file():
            file_extension = file_path.suffix.lower()
            subdir_name = None

            for category, subcategories in file_mappings.items():
                for subcategory, extensions in subcategories.items():
                    if file_extension in extensions:
                        subdir_name = category_dirs[category] / subcategory
                        break
                if subdir_name:
                    break

            if subdir_name:
                files_to_move.append((file_path, subdir_name))

    progress_window = Toplevel(window)
    progress_window.title("Processing Files")
    progress_bar = ttk.Progressbar(progress_window, length=300, mode='determinate')
    progress_bar.pack(pady=20)
    progress_label = Label(progress_window, text="Moving files...")
    progress_label.pack()

    total_files = len(files_to_move)

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

# Button for selecting directory and moving files
bg_image_1 = PhotoImage(file=r"assets/button.png")
submit_button = Button(window, image=bg_image_1, bg="#000000", fg="white",
                       borderwidth=0, relief="flat", cursor="hand2", activebackground="#000000",
                       command=run_async_task)
submit_button.place(x=90, y=290, width=220, height=40)

# Exit button
bg_image_3 = PhotoImage(file=r"assets/Exit.png")
exit_button = Button(window, image=bg_image_3, text="Exit", bg="#000000", fg="white",
                     borderwidth=0, relief="flat", cursor="hand2", activebackground="#000000", command=quit)
exit_button.place(x=140, y=420, width=110, height=40)

window.resizable(False, False)
window.mainloop()
