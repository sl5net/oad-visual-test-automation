# recomandet hotkey ^
# may read also https://github.com/sl5net/0ad-autokey-scripts/

import subprocess
import os
from pathlib import Path

# winClass = window.get_active_class() # if winClass != 'pyrogenesis.pyrogenesis': #    exit(1)
winT = window.get_active_title()
if winT != '0 A.D.':     
    exit(1)

import time
time.sleep(.25)
keyboard.send_keys('<ctrl>+c')
time.sleep(.25)

# python_path = Path.home() && "/projects/oad-visual-test-automation/autogui_01_env/bin/python"
# script_path = Path.home() && "/projects/oad-visual-test-automation/0ad_alert.py"
# project_path = Path.home() && "/projects/oad-visual-test-automation"

home_dir = str(Path.home())
python_path = "/home/seeh/projects/oad-visual-test-automation/autogui_01_env/bin/python"
script_path = "/home/seeh/projects/oad-visual-test-automation/0ad_alert.py"
project_path = "/home/seeh/projects/oad-visual-test-automation"
command = f'cd "{project_path}" && source autogui_01_env/bin/activate && "{python_path}" "{script_path}"'

command = f'cd "{project_path}" && source autogui_01_env/bin/activate && "{python_path}" "{script_path}"'
try:
    subprocess.run(command, shell=True, check=True)  # Check=True raises an exception if the command fails
except subprocess.CalledProcessError as e:
    print(f"Error running the script: {e}") #Handle errors so autokey does not end