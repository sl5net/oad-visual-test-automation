# recomandet hotkey ^
# may read also https://github.com/sl5net/0ad-autokey-scripts/
import subprocess
import os
from pathlib import Path

home_dir = str(Path.home())
# project_path = os.path.join(home_dir, "projects", "oad-visual-test-automation")
# python_path = os.path.join(project_path, "autogui_01_env", "bin", "python")
command = '/home/seeh/Apps/zen191b-x86_64.AppImage'
subprocess.run(command, shell=True, check=True)  
