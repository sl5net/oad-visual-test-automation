import pyautogui
import time
import subprocess
import os
import json

# IMPORTANT: The image file names in this script are deliberately chosen and
# should NOT be changed without a very specific reason and explicit
# confirmation from the user.
#
# This is especially important for me (Gemini, an AI language model) to remember.
# I have a tendency to suggest "helpful" changes, including renaming files, but
# in this context, consistency is paramount. Unnecessary renaming can break
# the script, so I must resist that urge.

DEFAULT_SLEEP = 0.2 #Changed to 0.2   # Sleep duration in seconds
IMAGE_LOCATIONS_FILE = 'image_locations.json' # New config file

def focus_window_xdotool(window_title="Google AI Studio"):
    try:
        # Find the window ID using xdotool
        command = f"xdotool search --name '{window_title}'"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        window_id, errors = process.communicate()

        if window_id:
            window_id = window_id.strip()
            # Activate the window using xdotool
            activate_command = f"xdotool windowactivate {window_id}"
            subprocess.run(activate_command, shell=True)

            # Use window focus as well.
            focus_command = f"xdotool windowfocus {window_id}"
            subprocess.run(focus_command, shell=True)

            print(f"Focused window with ID: {window_id}")
            time.sleep(DEFAULT_SLEEP)  # Allow time to focus
            return True
        else:
            print(f"Window with title '{window_title}' not found using xdotool.")
            return False

    except Exception as e:
        print(f"Error focusing window with xdotool: {e}")
        return False

def speak(text):
    try:
        subprocess.run(['espeak-ng', text])
    except FileNotFoundError:
        print("Error: espeak-ng is not installed. Please install it.")
    except Exception as e:
        print(f"An error occurred during TTS: {e}")

def launch_0ad():
    return
    appimage_path = os.path.expanduser("~/Apps/zen-x86_64.AppImage ")
    try:
        subprocess.Popen(f"{appimage_path} -quickstart -autostart-speed=2", shell=True, start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(10 * DEFAULT_SLEEP)  # Allow the game time to start (adjust as needed)
        return True
    except FileNotFoundError:
        speak("Error: AppImage not found. Please check the path.")
        print(f"Error: AppImage not found. {appimage_path}.")
        return False
    except Exception as e:
        speak(f"Error launching: {e}")
        print(f"Error launching: {e}")
        return False

def load_image_locations():
    """Loads image locations from the JSON file."""
    try:
        with open(IMAGE_LOCATIONS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist
    except json.JSONDecodeError:
        print("Error decoding image locations JSON file. Starting with empty locations.")
        return {}

def save_image_locations(locations):
    """Saves image locations to the JSON file."""
    try:
        with open(IMAGE_LOCATIONS_FILE, 'w') as f:
            json.dump(locations, f, indent=4)  # Pretty print the JSON
    except Exception as e:
        print(f"Error saving image locations to JSON file: {e}")

def locate_button(image_files, confidence=0.7, last_location=None, tolerance=50):  # Added the code
    """
    Tries to locate a button using a list of image files, first near the last known location.
    Returns the bounding box (left, top, width, height) of the button if found, otherwise None.
    """
    for image_file in image_files:
        try:
            # First, try searching near the last known location (if available)
            if last_location:
                left, top, width, height = last_location
                search_region = (left - tolerance, top - tolerance, width + 2 * tolerance, height + 2 * tolerance)
                try:
                    button_location = pyautogui.locateOnScreen(image_file, confidence=confidence, region=search_region)
                    if button_location:
                        print(f"Found button (near last location) using image: {image_file}")
                        return button_location  # Return the entire Box object
                except pyautogui.ImageNotFoundException:
                    print(f"Button not found (near last location) using image: {image_file}")

            # If not found near the last location, try searching the entire screen
            button_location = pyautogui.locateOnScreen(image_file, confidence=confidence)  # Locate entire image
            if button_location:
                print(f"Found button (full screen search) using image: {image_file}")
                return button_location  # Return the entire Box object

        except pyautogui.ImageNotFoundException:
            print(f"Button not found using image: {image_file}")

    return None

def end_0ad():
    return

def click_button(button_image, button_name, confidence=0.7, sleep_after=DEFAULT_SLEEP):
    """
    Locates and clicks a button on the screen, handling single images or lists.
    Terminates the script if the button is not found.
    """
    global image_locations  # Access to top

    image_key = button_image if not isinstance(button_image, list) else button_image[0]

    if isinstance(button_image, list):
        # It's a list of images, use locate_button
        button_location = locate_button(button_image, last_location=image_locations.get(image_key), confidence=confidence)  # Use the function to check
    else:
        # It's a single image, find it directly
        button_location = pyautogui.locateOnScreen(button_image, confidence=confidence)

    if button_location:
        # click the button
        pyautogui.click(pyautogui.center(button_location))
        speak(f"{button_name} clicked")
        time.sleep(sleep_after)

        # Save the location now
        if isinstance(button_image, list):
            # For image lists use the first image file name as the key
            x, y, width, height = button_location #To fix

            image_locations[button_image[0]] = (int(x), int(y), int(width), int(height))
        else:
            # It was the one
            x, y, width, height = button_location #To fix

            image_locations[button_image] = (int(x), int(y), int(width), int(height)) # save all info to the JSON

        save_image_locations(image_locations)  # save this location.
    else:
        print(f"{button_name} not found!")
        # speak(f"{button_name} not found")
        # time.sleep(1 * DEFAULT_SLEEP)  # Longer wait for it to initialize
        # end_0ad()
        # exit()

# Main Script:
if __name__ == "__main__":

    global image_locations  # Use it here in global

    image_locations = load_image_locations()  # Load image locations at script start

    if not focus_window_xdotool():
        if launch_0ad():
            time.sleep(15 * DEFAULT_SLEEP)  # Longer wait for it to initialize
            if not focus_window_xdotool():  # Try again
                speak("Failed to focus after launching. Aborting.")
                print("Failed to focus after launching. Aborting.")
                exit()
        else:
            print("Failed to launch Aborting.")
            speak("Failed to launch Aborting.")
            end_0ad()  # End
            exit()

    while True:
        click_button(['googleAIstudio/TypeSomething_not_focused.png'], "TypeSomething", confidence=0.9, sleep_after=9)
        time.sleep(15)

# The End
