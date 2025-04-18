#Enter script code
# mod-auswahl_button.png
# recomandet hotkey m
keyboard.send_keys("m")
if store.get_global_value("autokeypause") == True:
    exit(1)    

# may read also https://github.com/sl5net/0ad-autokey-scripts/
import subprocess
import os
from pathlib import Path
import time

# winClass = window.get_active_class() # if winClass != 'pyrogenesis.pyrogenesis': #    exit(1)
winT = window.get_active_title()
# if winT != '0 A.D.':     
#    exit(1)

home_dir = str(Path.home())
project_path = os.path.join(home_dir, "projects", "oad-visual-test-automation")
python_path = os.path.join(project_path, "autogui_01_env", "bin", "python")
script_path = os.path.join(project_path, "0ad_clickButton.py")

button_name = "mod-auswahl_button"

command = f'cd "{project_path}" && source autogui_01_env/bin/activate && "{python_path}" "{script_path}" "{button_name}"'

try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running the script: {e}")
