#  .py  file --- " main_the_run_one.py "
import function_DICT
import os.path

path_output = function_DICT.get_USB_path()
print(path_output)

while True:
    file_path_indexNum = int(input("Enter your desire file path (ex:0,1,2....): "))
    file_name = str(input("Enter your file name (ex:aaa.txt): "))

    if len(path_output) < file_path_indexNum:
        print("error path, shut down")
        break

    file_path = (str(path_output[file_path_indexNum]) +"/" + file_name)

    if os.path.exists(file_path) == False:
        print("error file path, no such file")
        break

    added_data = str(input("type ur added data : "))  
    
    
    error_info1  =  function_DICT.File_write(file_path, added_data)
    if (os.path.exists(file_path)) == True:
      	correct_file_path = file_path

contents = function_DICT.File_read(correct_file_path)
print(contents)
        

# sudo python '/home/joy/fe_dir/main_the_run_one.py'
# /media/joy/Data/aaa.txt
