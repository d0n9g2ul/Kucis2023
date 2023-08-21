#extract.py

import time
import subprocess
import os

file_script_path = "pyExtract/script/file/"
etc_script_path = "pyExtract/script/etc/"
system_script_path = "pyExtract/script/system/"
log_script_path = "pyExtract/script/log/"

result_directory_path = "pyExtract/result"

def history():
    print("[---] EXTRACT History LOGs !! [---]")
    try:
        subprocess.run(["bash", etc_script_path+'history.sh'], check=True)
        print("\n[*** SUCCESS *** ]\n")
    except subprocess.CalledProcessError:
        print("\n[*** FAILED *** ] Error executing the shell script.\n")
    time.sleep(2.5)

def access_time(directory_path=None):
    print("[---] EXTRACT File Access Time !! [---]")
    
    # Default directories to be used if none is provided
    default_directories = ["/etc", "/usr", "/var", "/home"]
    
    if directory_path is None:
        directory_path = ",".join(default_directories)
    
    # Get the script path
    try:
        subprocess.run(["bash", file_script_path+'access_time.sh', directory_path], check=True)
        print("\n[ !!! SUCCESS !!! ]\n")
    except subprocess.CalledProcessError:
        print("\n[*** FAILED ***] Error executing the shell script.\n")

    time.sleep(2.5)


def modify_time(directory_path=None):
    print("[---] EXTRACT File Modify Time !! [---]")
    # Default directories to be used if none is provided
    default_directories = ["/etc", "/usr", "/var", "/home"]
    
    if directory_path is None:
        directory_path = ",".join(default_directories)
    
    # Get the script path
    try:
        subprocess.run(["bash", file_script_path+'modify_time.sh', directory_path], check=True)
        print("\n[ !!! SUCCESS !!! ] [*** Done ***]\n")
        
        
    except subprocess.CalledProcessError:
        print("\n[*** FAILED ***] Error executing the shell script. [*** Error ***]\n")
    
    time.sleep(2.5)

def birth_time(directory_path=None):
    print("[---] EXTRACT File Birth Time !! [---]")
    
    # Default directories to be used if none is provided
    default_directories = ["/etc", "/usr", "/var", "/home"]
    
    if directory_path is None:
        directory_path = ",".join(default_directories)
    
    # Get the script path
    try:
        subprocess.run(["bash", file_script_path+'birth_time.sh', directory_path], check=True)
        print("\n[ !!! SUCCESS !!! ] [*** Done ***]\n")
        
        
    except subprocess.CalledProcessError:
        print("\n[*** FAILED ***] Error executing the shell script. [*** Error ***]\n")

    time.sleep(2.5)

def log():
    print("[---] EXTRACT Journal LOGs !! [---]")
    try:
        subprocess.run(["bash", etc_script_path+'journal.sh'], check=True)
        print("\n[ !!! SUCCESS !!! ] [*** Done ***]\n")
    except subprocess.CalledProcessError:
        print("\n[*** FAILED ***] Error executing the shell script. [*** Error ***]\n")
    time.sleep(2.5)

def login():
    print("[---] EXTRACT Login LOGs !! [---]")
    try:
        subprocess.run(["bash", etc_script_path+'login.sh'], check=True)
        print("\n[ !!! SUCCESS !!! ] [*** Done ***]\n")
        
        
    except subprocess.CalledProcessError:
        print("\n[*** FAILED ***] Error executing the shell script. [*** Error ***]\n")

    time.sleep(2.5)

def system():
    print("[---] EXTRACT SYSTEM INFORMATION !! [---]")
    try:
        print(("[*]\tEXTRACT Netstat LOGs !!\t[*]"))
        subprocess.run(["bash", system_script_path+'netstat.sh'], check=True)
        print("[*]\tEXTRACT Pstree LOGs !!\t[*]")
        subprocess.run(["bash", system_script_path+'pstree.sh'], check=True)
        print("[*]\tEXTRACT Top LOGs !!\t[*]")
        subprocess.run(["bash", system_script_path+'top.sh'], check=True)
        print("\n[ !!! SUCCESS !!! ] [*** Done ***]\n")
        
    except subprocess.CalledProcessError:
        print("\n[*** FAILED ***] Error executing the shell script. [*** Error ***]\n")

    time.sleep(2.5)

