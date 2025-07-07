import hashlib
import os
import time
from pathlib import Path
import logging
from time import sleep
import json
import threading
from tkinter import Tk, Canvas, Label, Button,PhotoImage,filedialog,ttk,messagebox,simpledialog
import shutil

#-----for ac app
# from selenium import webdriver
# import codecs
# import sys
# import re
# import fcntl
# import signal

# ---------------------------- CONSTANTS ------------------------------- #
# Create the main window
window = Tk()


YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
Complicated= '✔'
failed="✖"

# -------
path = Path("./md5Records")  # File path
main_name = "checksum_data.txt" #file name


import platform

if platform.system() != 'Windows':
    import fcntl

def logging_process():
    log_folder = "logs"
    # Create the folder if it doesn't exist
    os.makedirs(log_folder, exist_ok=True)
    count1 = 0
    for root_dir, cur_dir, files in os.walk(log_folder):
        count1 += len(files)
    # print('file count:', count1)
    if count1>20:
        folder_path = os.path.join(os.getcwd(), log_folder)
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path)[:1]:
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
        else:
            messagebox.showinfo("showinfo",
                                f"LogFolder not found:{folder_path}")
            print("LogFolder not found:", folder_path)

    log_filename = os.path.join(log_folder, f"log_{time.strftime("%Y-%m-%d_%H-%M-%S")}.log")
    # Configure logging to write to a file
    logging.basicConfig(
        filename=log_filename,  # Log file name
        level=logging.DEBUG,  # Set the logging level
        format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    )
logging_process()

def select_folder():
    folder_path = filedialog.askdirectory(title="Select a Folder")
    if folder_path:
        return folder_path
    else:
        print("No folder selected.")

def start_process_bar():
    status_label.grid_forget()
    progress.grid(column=2, row=4, padx=5, pady=5)
    progress.start(1)

def stop_process_bar():
    progress.stop()
    progress.grid_forget()  # Remove progress bar


def md5_checksum(file_path, chunk_size=8192):
    # Check if the file exists
    if not os.path.isfile(file_path):
        return f"Error: File '{file_path}' not found."
    md5 = hashlib.md5()  # Create an MD5 hash object
    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(chunk_size), b""):
                md5.update(chunk)  # Update the hash with each chunk
        return md5.hexdigest()  # Return the hexadecimal MD5 checksum
    except Exception as e:
        return f"Error: {str(e)}"

def check_files_in_directory(directory, key=0):
    try:
        # files1 = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        # print(files1)
        files=get_folder_checksum(directory)
        if not files:
            print(f"No files found in the directory: {directory}")
            logging.info(f" No files found in the directory: {directory} \n")
            return 0
        # print(f"Files found in '{directory}':")
        dict_checksum = {}
        for file_name in files:
            print(file_name)
            # file_path = os.path.join(directory, file_name)
            mb5_checksum = md5_checksum(file_name)
            # print(f"{file_name} - MD5_Checksum: {mb5_checksum}")
            main_file_name = os.path.basename(file_name)
            print(main_file_name)
            dict_checksum[main_file_name] = mb5_checksum
        logging.info(f" dict_checksum created with key value \n")

        return dict_checksum
        # compair_value(file_name,mb5_checksum)
    except Exception as e:
        logging.info(f" exception occur : {e} \n")
        print(f"Error: {str(e)}")

def get_folder_checksum(folder_path):
    """Generate a combined checksum for all files in a folder"""
    list_of_files=[]
    for root,dirs,files in sorted(os.walk(folder_path)):
        print(root)
        for data in files:
            if type(data)==str and data!=[]:
                print("file name :",data)
                # print("inside..........",f"{root}/{data}")
                list_of_files.append(f"{root}/{data}")
    print(list_of_files)
    return list_of_files

def update_mismatch(value,mismatch_file):
    with open(mismatch_file, 'a') as file:
        file.write(json.dumps(value))
        file.write("\n")

def compare_dictionaries(dict1, dict2):
    count=0
    match=0
    folder_path="md5Records/mismatches"
    os.makedirs(folder_path, exist_ok=True)
    mismatch_file=os.path.join(folder_path,f"Mismatch_data_{time.strftime("%Y-%m-%d_%H-%M-%S")}.txt")
    # Use union of keys to ensure all are compared
    all_keys = dict1.keys() | dict2.keys()
    for key in all_keys:
        try:
            value1 = dict1[key]
        except KeyError:
            logging.warning(f"Key '{key}' not found in dict1.")
            update_mismatch(key,mismatch_file)
            count += 1
            continue
        try:
            value2 = dict2[key]
        except KeyError:
            logging.warning(f"Key '{key}' not found in dict2.")
            update_mismatch(key,mismatch_file)
            count += 1
            continue
        if value1 != value2:
            logging.critical(f"Difference found for key '{key}': \n"
                             f"  - Dict1: {value1}\n"
                             f"  - Dict2: {value2}\n"
                             f"-------------------\n")
            update_mismatch(key)
            count+=1
        else:
            match+=1
    summary = (f"Checking process is complete.\n"
               f"Total mismatches after comparison: {count}\n"
               f"Total matching records: {match}")

    logging.info(summary)
    messagebox.showinfo("Comparison Result", summary)

def compare_records(checksum_dict, file_path):
    # print(file_path)
    with open(file_path, 'r') as file:
        old_checksum_dict=file.readlines()[0]
        # print(old_checksum_dict)
    print(old_checksum_dict)
    logging.info(f" Previous file data is fetched ready to compair with new data \n")
    compare_dictionaries(checksum_dict,json.loads(old_checksum_dict))

def copy_file_to_destination(checksum_folder_path):
    #"select destination"
    location = select_folder()

    start_process_bar()

    logging.info(f"The file/ folder copying process has been started... \n")
    messagebox.showinfo("showinfo",
                        f"The file/ folder copying process has been started...")
    shutil.copytree(checksum_folder_path, location,dirs_exist_ok=True)
    logging.info(f" The file/folder copying process completed at location \nSource: {checksum_folder_path} \nDestination: {location}... \n")

    my_start = messagebox.askyesno("Copying process is completed",
                                 "Do you want to Start checksum checking and comparing process..?")
    if my_start:
        start_process(path,main_name,location)
        stop_process_bar()
        status_label.config(text=Complicated)  # Show checkmark after completion


# class StartProcess:
def start_process(folder_path,file_name,new_location=None):
    try:
        progress.start(1)
        file_path = folder_path / file_name
        # print(file_path)
        if file_path.exists():
            #--------------------"File exists!"
            if new_location is None:
                checksum_folder_path = select_folder()
            else:
                checksum_folder_path=new_location
            checksum_dict = check_files_in_directory(checksum_folder_path)
            print(checksum_dict)
            if checksum_dict!=0:
                with open(f"{folder_path}/checksum_all_records.txt",'a') as file:
                    file.write(json.dumps(checksum_dict))
                    file.write("\n")
                compare_records(checksum_dict, file_path)
            else:
                # print("Please select foder that contains some files")
                stop_process_bar()  # Remove progress bar
                status_label.config(text=failed)  # Show checkmark after completion
                messagebox.showinfo("showinfo",
                                    f"Please select foder that contains some files")
                window.quit()
        else:
            #-----------"File not found!"
            checksum_folder_path=select_folder()
            checksum_dict=check_files_in_directory(checksum_folder_path)
            folder_path.mkdir(parents=True, exist_ok=True)
            logging.info(f" File name with checksum values: \n{checksum_dict}")
            file_folder=f"{folder_path}/checksum_data.txt"
            with open(file_folder,'a') as file:
                file.write(json.dumps(checksum_dict))
            logging.info(f" New checksum file created with all scan data at location: {file_folder}")

            if type(checksum_dict) == dict:
                total_count = len(checksum_dict)
                stop_process_bar()  # stop progress bar
                # progress.grid_forget()  # Remove progress bar
                status_label.config(text=Complicated)  # Show checkmark after completion
                messagebox.showinfo("showinfo",
                                    f"New checksum file created with all scan data \n"
                                    f"total count: {total_count}")

                ##############################################################
                # If want to copy file at destination
                my_var = messagebox.askyesno("Copy Window",
                                             "Did you want to Copy all selected files to the other location?")
                print(my_var)
                if my_var:
                    copy_file_to_destination(checksum_folder_path)
            else:
                total_count = 0
                stop_process_bar()  # Remove progress bar
                status_label.config(text=failed)  # Show checkmark after completion
                messagebox.showinfo("showinfo",
                                    f"Please select foder that contains some files \n"
                                    f"total count: {total_count}")
        sleep(2)
        window.quit()

    except Exception as X:
        stop_process_bar()  # Remove progress bar
        status_label.config(text=failed)  # Show checkmark after completion
        print(X)
        logging.info(f"  Issue with the file or folder :{X}\n")
        messagebox.showinfo("showinfo",
                            f"Issue with the file or folder")

# start_process(path,main_name)

window.config(padx=60, pady=60, bg='white')
window.title('Checksum')


# ===== Title Label =====
checksum_label = Label(text='Checksum', fg='black', bg='white', font=("Arial", 40, 'bold'))
checksum_label.grid(column=2, row=0, columnspan=3, pady=20)  # Centering title

# ===== Canvas (Checksum Image & Text) =====
canvas = Canvas(width=210, height=224, bg="white", highlightthickness=0)
checksum_img = PhotoImage(file='tomato_bg.png')
canvas.create_image(103, 112, image=checksum_img)
checksum_text = canvas.create_text(103, 140, fill='black', font=("Arial", 30, 'bold'))
canvas.grid(column=2, row=1, columnspan=3, pady=10)  # Centering canvas

# Label for checkmark (Initially empty)
status_label = Label(window, text="", font=("Arial", 20), fg="green")
status_label.grid(column=2, row=4,)

# Create a progress bar (Determinate mode)
progress =ttk.Progressbar(window, orient="horizontal", length=200, mode="indeterminate")
progress.grid(column=2, row=4, padx=5, pady=5)
def start_task():
    threading.Thread(target=lambda: start_process(path,main_name), daemon=True).start()

# ===== Generate Button =====
generate_btn_img = PhotoImage(file='generate.png')
generate_btn = Button(image=generate_btn_img, borderwidth=0, highlightthickness=0, relief="flat",command=start_task)
generate_btn.grid(column=2, row=2, padx=10, pady=10)

window.mainloop()