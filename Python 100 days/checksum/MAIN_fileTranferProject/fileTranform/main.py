import hashlib
import os
import time
import tkinter
from pathlib import Path
import logging
from time import sleep
import json
import threading
from tkinter import Tk, Canvas, Label, Button, PhotoImage, filedialog, ttk, messagebox
import shutil
import platform

# ---------------------------- CONFIGURATION ------------------------------- #
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
Complicated = '✔'
failed = "✖"

# Folder to store checksum and log data
folder_name = Path("./md5Records")
main_name = "checksum_data.txt"

if platform.system() != 'Windows':
    import fcntl

# ---------------------------- LOGGING SETUP ------------------------------- #
def logging_process():
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    count1 = sum(len(files) for _, _, files in os.walk(log_folder))
    if count1 > 20:
        for filename in os.listdir(log_folder)[:1]:
            file_path = os.path.join(log_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted old log: {file_path}")

    log_filename = os.path.join(log_folder, f"log_{time.strftime('%Y-%m-%d_%H-%M-%S')}.log")
    logging.basicConfig(
        filename=log_filename,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )
    logging.info("Logging process initialized.")

logging_process()

# ---------------------------- CHECKSUM UTILITIES -------------------------- #
def md5_checksum(file_path, chunk_size=8192):
    if not os.path.isfile(file_path):
        logging.error(f"File not found for checksum: {file_path}")
        return f"Error: File '{file_path}' not found."
    md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(chunk_size), b""):
                md5.update(chunk)
        return md5.hexdigest()
    except Exception as e:
        logging.exception(f"Error while generating MD5: {e}")
        return f"Error: {str(e)}"

def get_folder_checksum(folder_path):
    list_of_files = []
    for root, dirs, files in sorted(os.walk(folder_path)):
        for data in files:
            if data.startswith('.'):
                continue
            full_path = Path(root) / data
            list_of_files.append(str(full_path))
    logging.info(f"Total files found in {folder_path}: {len(list_of_files)}")
    return list_of_files

def check_files_in_directory(directory):
    try:
        files = get_folder_checksum(directory)
        if not files:
            logging.info(f"No files found in directory: {directory}")
            return 0
        dict_checksum = {}
        for file_name in files:
            mb5_checksum_result = md5_checksum(file_name)
            main_file_name = os.path.relpath(file_name, directory)
            dict_checksum[main_file_name] = mb5_checksum_result
        logging.info(f"Checksum dictionary created for {directory}")
        return dict_checksum
    except Exception as e:
        logging.exception(f"Exception in check_files_in_directory: {e}")

# ---------------------------- MISMATCH HANDLING -------------------------- #
def update_mismatch(value, mismatch_file=None):
    with open(mismatch_file, 'a') as file:
        file.write(json.dumps(value) + "\n")
    logging.warning(f"Mismatch recorded: {value}")

def compare_dictionaries(dict1, dict2):
    count = 0
    match = 0
    folder_path = "md5Records/mismatches"
    os.makedirs(folder_path, exist_ok=True)
    mismatch_file = os.path.join(folder_path, f"Mismatch_data_{time.strftime('%Y-%m-%d_%H-%M-%S')}.txt")
    all_keys = dict1.keys() | dict2.keys()
    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if value1 != value2:
            logging.critical(f"Difference in {key}: {value1} != {value2}")
            update_mismatch({key: [value1, value2]}, mismatch_file)
            count += 1
        else:
            match += 1
    summary = (f"Checking process complete.\nTotal mismatches: {count}\nTotal matches: {match}")
    logging.info(summary)
    messagebox.showinfo("Comparison Result", summary)

# ---------------------------- FILE COPY + COMPARE ------------------------ #
def compare_records(checksum_dict, file_path):
    with open(file_path, 'r') as file:
        old_checksum_dict = file.readlines()[0]
    compare_dictionaries(checksum_dict, json.loads(old_checksum_dict))

def copy_file_to_destination(checksum_folder_path,file_folder):
    location = select_folder()
    new_folder = get_folder_checksum(location)
    if len(new_folder) != 0:
        logging.info("Destination folder is not empty. Prompting user.")
        messagebox.showinfo("showinfo", "Please select empty folder to copy....")
        copy_file_to_destination(checksum_folder_path)
        return

    start_process_bar()
    logging.info(f"Starting copy to destination: {location}")
    shutil.copytree(checksum_folder_path, location, dirs_exist_ok=True)
    # shutil.copytree(file_folder, location, dirs_exist_os_exist_ok=True)#-------------new added
    logging.info("Copy complete.")
    messagebox.showinfo("Copy Complete", f"Copied files to: {location}")

    if messagebox.askyesno("Compare", "Do you want to compare checksum now?"):
        print(folder_name,'\n',main_name,'\n',location)
        start_process(folder_name, main_name, location)

        stop_process_bar()
        status_label.config(text=Complicated)

# ---------------------------- PROCESS RUNNER ----------------------------- #
def start_process(folder_path, file_name, new_location=None):
    file_path = folder_path / file_name
    try:
        progress.start(1)
        if file_path.exists():
            checksum_folder_path = new_location if new_location else select_folder()
            checksum_dict = check_files_in_directory(checksum_folder_path)
            if checksum_dict != 0:
                with open(folder_path / "checksum_all_records.txt", 'a') as file:
                    file.write(json.dumps(checksum_dict) + "\n")
                compare_records(checksum_dict, file_path)
                sleep(1)
                window.quit()
            else:
                stop_process_bar()
                status_label.config(text=failed)
                messagebox.showinfo("showinfo", "Please select folder that contains some files")
                window.quit()
        else:
            checksum_folder_path = select_folder()
            checksum_dict = check_files_in_directory(checksum_folder_path)
            folder_path.mkdir(parents=True, exist_ok=True)
            file_folder = folder_path / "checksum_data.txt"
            with open(file_folder, 'a') as file:
                file.write(json.dumps(checksum_dict))
            if isinstance(checksum_dict, dict):
                total_count = len(checksum_dict)
                stop_process_bar()
                status_label.config(text=Complicated)
                sleep(0.5)
                messagebox.showinfo("showinfo", f"Checksum file created with {total_count} entries.")
                if messagebox.askyesno("Copy", "Do you want to copy files to another location?"):
                    start_process_bar()
                    copy_file_to_destination(checksum_folder_path,file_folder)#----------added checksum file as well
            else:
                total_count = 0
                stop_process_bar()
                if os.path.exists(file_path):
                    os.remove(file_path)
                status_label.config(text=failed)
                messagebox.showinfo("showinfo", f"Invalid folder. Total count: {total_count}")
                window.quit()
        sleep(1)
        window.quit()
    except Exception as X:
        stop_process_bar()
        status_label.config(text=failed)
        if os.path.exists(file_path):
            os.remove(file_path)
        logging.exception("Exception during start_process")
        messagebox.showinfo("showinfo", f"Error occurred: {X}")

# ---------------------------- GUI SETUP ---------------------------------- #
window = Tk()
window.config(padx=50, pady=40, bg='#e6f2ff')
window.title('Checksum File Validator')


# img=tkinter.Image('photo',file='icons_checksum.icns')
# window.call('wm','iconphoto',window._w,img)
checksum_label = Label(text='Checksum Validator', fg='#1a1a1a', bg='#e6f2ff', font=("Segoe UI", 32, 'bold'))
checksum_label.grid(column=2, row=0, columnspan=3, pady=20)

canvas = Canvas(width=210, height=224, bg="#e6f2ff", highlightthickness=0)
checksum_img = PhotoImage(file='tomato_bg.png')
canvas.create_image(103, 112, image=checksum_img)
canvas.grid(column=2, row=1, columnspan=3, pady=10)

status_label = Label(window, text="", font=("Segoe UI", 16), fg="#27ae60", bg="#e6f2ff")
status_label.grid(column=2, row=4)
status_label.grid_remove()  # Hide initially

progress = ttk.Progressbar(window, orient="horizontal", length=250, mode="indeterminate")
progress.grid(column=2, row=4,padx=10, pady=10)
status_label.grid_remove()  # Hide initially


#progress Styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=10, background="#4CAF50", foreground="white")

def select_folder():
    return filedialog.askdirectory(title="Select a Folder")

def start_process_bar():
    status_label.grid_remove()
    progress.grid(column=2, row=4, padx=5, pady=5)
    # progress.grid()
    progress.start(1)

def stop_process_bar():
    progress.stop()
    progress.grid_remove()
    status_label.grid()

def start_task():
    generate_btn.config(state="disabled")
    threading.Thread(target=lambda: start_process(folder_name, main_name), daemon=True).start()

generate_btn_img = PhotoImage(file='generate.png')
generate_btn = Button(image=generate_btn_img,activeforeground="white",anchor="center" ,highlightbackground="#e6f2ff",highlightthickness=0,bd=0,justify="center",overrelief="raised",command=start_task)

generate_btn.grid(column=2, row=2, padx=90, pady=20)

window.mainloop()