#  .py  file --- " function_DICT.py "

import time
from usb.core import find
from usb.util import get_string
import usb.backend.libusb1
import re
import usb.core
import usb.util
import os
import numpy as np
import os.path
from os import path
import os
import subprocess

def get_USB_path():
    try:
        #use linus call by python
        a = subprocess.check_output(['lsblk'])

        # I split by "\n" cause that in erery line of str_a
        str_a_splited = a.decode().split("\n")

        # USB in linux usually in media file
        USB_info = [s for s in str_a_splited if "/media/" in s]
        found_path = []

        for x in USB_info:
            for s in x.split(" "):
                if "/media/" in s:
                    found_path.append(s)


    except Exception as e:   
        return "error in get_USB_path()" 

    return found_path


def File_write(input_User_path, user_content):
    try:
        error_info1 = ""
      
        if (os.path.exists(input_User_path)) == True:
            file = open(input_User_path , "a")
            file.write("\n" + user_content)
            file.close()
        else: 
            error_info1 =  "Path incorrect"

    except Exception as e:   
        return "error in File_write()"

    return error_info1


def File_read(input_file_path):
    try:
        with open(input_file_path) as f:
          contents = f.read()

    except Exception as e:   
        return "error in File_read()"

    return contents


# sudo python '/home/joy/fe_dir/main_the_run_one.py'
# /media/joy/Data/aaa.txt
