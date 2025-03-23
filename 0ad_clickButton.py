import pyautogui
import time
import subprocess
import os
import json
import sys
import logging

# Configure logging
logging.basicConfig(filename='debug.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Activate the Virtual Environment

# source autogui_01_env/bin/activate

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

def speak(text):
    try:
        subprocess.run(['espeak-ng', text])
    except FileNotFoundError:
        print("Error: espeak-ng is not installed. Please install it.")
        logging.error("Error: espeak-ng is not installed. Please install it.")
    except Exception as e:
        print(f"An error occurred during TTS: {e}")

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
            if button_name != "alertstop_button":
                print(f"Button not found using image: {image_file}")
                speak(f"Button not found using image: {image_file}")
                logging.warning(f"Button not found using image: {image_file}")
    return None

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
        if button_name != "alertstop_button":
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
        if button_name != "alertstop_button":
            speak(f"{button_name} not found 130")
        logging.warning(f"'{button_name}' not found 130")
        end_0ad()
        exit()

if __name__ == "__main__":

    button_name = sys.argv[1]

    button_name = sys.argv[1]
    logging.info(f"Button name received: {button_name}")

    global image_locations  # Use it here in global

    image_locations = load_image_locations()  # Load image locations at script start

    # single_player_images = ['images/0ad/alert_button.png'] # thats how it looks before
    image1 = f'images/0ad/{button_name}.png'
    #speak(f"{image1}")
    single_player_images = [image1]
    click_button(single_player_images, f'{button_name}')





















