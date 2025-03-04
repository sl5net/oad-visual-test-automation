**Automates visual mod testing for the 0 A.D. game.**

This project provides a Python script to automate the process of launching 0 A.D., starting a single-player game, navigating the GUI, and exiting, primarily for testing visual modifications (mods). It leverages image recognition for GUI interaction and offers optional audio feedback using text-to-speech (TTS).

## Features

*   **Automated Visual Testing:** Streamlines the process of testing visual changes in 0 A.D. by automating game launch, GUI navigation, and exit.
*   **Image Recognition-Based GUI Interaction:** Uses `PyAutoGUI` to locate and interact with GUI elements, making the script adaptable to UI variations.
*   **Optimized Image Search:**  Stores the last known locations of GUI elements in `image_locations.json` to speed up image recognition by searching near those locations first.
*   **Audio Feedback (Optional):** Provides audio cues (using `espeak-ng`) to indicate script progress.
*   **Robust Process Termination:** Includes multiple methods to ensure clean termination of the 0 A.D. process.

## Technologies Used

*   **Python 3.6+**
*   **PyAutoGUI:** For cross-platform GUI automation and image recognition.
*   **xdotool (Linux):** For window management (focusing the 0 A.D. window).
*   **espeak-ng (Optional):** For text-to-speech audio feedback.
*   **JSON:** For storing last-known image locations (`image_locations.json`).

## Installation

1.  **Prerequisites:**
    *   Python 3.6 or higher
    *   0 A.D. AppImage (recommended) or a locally installed version.
    *   Linux-based operating system (for `xdotool` window management).  While `pyautogui` is cross-platform, `xdotool` is used for focus.

2.  **Install System Dependencies:**
    *   **xdotool (Linux):**
        ```bash
        sudo apt-get install xdotool  # Debian/Ubuntu
        # sudo yum install xdotool    # CentOS/RHEL/Fedora
        ```
    *   **espeak-ng (Optional - for audio feedback):**
        ```bash
        sudo apt-get install espeak-ng  # Debian/Ubuntu
        # sudo yum install espeak-ng    # CentOS/RHEL/Fedora
        ```

3.  **Clone the Repository:**

    ```bash
    git clone git@github.com:sl5net/oad-visual-test-automation.git
    cd oad-visual-test-automation
    ```

4.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
    ```

5.  **Install Python Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    (The `requirements.txt` file lists all necessary Python packages.)

## Configuration

*   **`image_locations.json`:**  This file is critical for adapting the script to different screen resolutions and UI variations in 0 A.D. It contains the coordinates of GUI elements used by the script.

    *   If the script fails to locate UI elements, you will need to manually update the coordinates in this file.
    *   The script attempts to save the locations as they are found, but manual adjustments may be needed.

*   **AppImage Path:**  Modify the `appimage_path` variable in the `launch_0ad()` function to point to the correct location of your 0 A.D. AppImage file. This path is currently set to `os.path.expanduser("~/Apps/0ad.AppImage")`.

## Usage

1.  **Run the Script:**

    ```bash
    python your_script_name.py  # Replace "your_script_name.py" with the actual script name
    ```

2.  **Observe the Script:** The script will automatically launch 0 A.D., navigate the GUI, and eventually exit. Audio feedback (if enabled) will provide status updates.

3.  **Troubleshooting Image Recognition:** If the script fails to locate GUI elements:

    *   Examine the script's output for error messages indicating which images could not be found.
    *   Use a screenshot tool to capture images of the GUI elements that the script is failing to find.  Ensure that the image files in the repository match the actual GUI elements in 0 A.D.
    *   Update the coordinates in `image_locations.json` accordingly.  Use tools like `xdotool getmouselocation` to precisely determine the coordinates of UI elements.

## Important Notes for Developers

*   **Image File Naming:** The names of the image files used for image recognition are deliberately chosen and should **not** be changed without careful consideration.  Changing these names will break the script.
*   **GUI Variations:** 0 A.D.'s GUI may change in future versions, requiring updates to the image files and `image_locations.json`.
*   **Customization:** The script is designed to be customized for specific testing scenarios.  Feel free to modify the script to suit your needs.
*    **Virtual Environment:**  Always work within a virtual environment to manage project dependencies.

## Contributing

Contributions are welcome! Please fork the repository, create a branch for your changes, and submit a pull request.
