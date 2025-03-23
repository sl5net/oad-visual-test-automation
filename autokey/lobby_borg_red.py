# recomandet hotkey ^
# may read also https://github.com/sl5net/0ad-autokey-scripts/
import subprocess
import os
from pathlib import Path
import time

# winClass = window.get_active_class() # if winClass != 'pyrogenesis.pyrogenesis': #    exit(1)
winT = window.get_active_title()
# if winT != '0 A.D.':     
#    exit(1)

time.sleep(.25)
keyboard.send_keys('<ctrl>+c')
time.sleep(.25)

home_dir = str(Path.home())
project_path = os.path.join(home_dir, "projects", "oad-visual-test-automation")
python_path = os.path.join(project_path, "autogui_01_env", "bin", "python")
script_path = os.path.join(project_path, "0ad_clickButton.py")

button_name = "lobby_borg_red"

final_status_img = "lobby_borg_green"
command = f'cd "{project_path}" && source autogui_01_env/bin/activate && "{python_path}" "{script_path}" "{button_name}"'
try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running the script: {e}")


time_max_to_wait  = 60*40
time_max_total    = 0

file_image        = "images/0ad/lobby_borg_green.png"

exit

end_is_here       = False
while (time_max_total < time_max_to_wait) and (end_is_here==False): #Test 10 sec max
    
    checkPathCommand  = "ls" + str(Path.home())
    try:
        # I check what file are there
        process      = subprocess.run(checkPathCommand , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Then check if file exists
        result = process.stdout

        if "lobby_borg_green.png" in result:
            end_is_here=True #End the cycle, so then can work

    except subprocess.CalledProcessError as e:
        print ("There is another error: ",e) #Check at files all is ok :o, if happens a second time then say
        #And break; the program if fails, then you will need see with what

    #Every seconds wait to test
    #You also can copy and edit another script to launch instead :O or force kill but what program has errors? ahahahah 11:11 here :D
    delaySecond = 3
    time.sleep(delaySecond)
    time_max_total+=delaySecond #It is also ok here to check total time
#When it all ends

final_status_img = "lobby_borg_green"
command = f'cd "{project_path}" && source autogui_01_env/bin/activate && "{python_path}" "{script_path}" "{button_name}"'
try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running the script: {e}")
