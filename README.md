# Appium Mobile Automation with Facebook App

This project demonstrates how to use Appium for mobile automation on an Android device. The script automates logging into the Facebook app, navigating to the menu, and changing the device orientation.

## Prerequisites

- Python 3.x
- `Appium-Python-Client` library
- Appium server installed and running
- An Android device

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/tinmaungzin/appium-mobile-automation.git
    cd appium-mobile-automation
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    

4. **Start the Appium Server:**

    Ensure that the Appium server is running. You can start it from the command line using:

    ```bash
    appium
    ```

## Usage

1. **Configure Desired Capabilities:**

    Edit the `desired_caps` dictionary in the script to match your device and app settings.

    - `platformName`: Platform name (e.g., "Android").
    - `deviceName`: Your device ID or name.
    - `appPackage`: The package name of the app.
    - `appActivity`: The activity name of the app.
    - `automationName`: Automation engine to use (e.g., "UiAutomator2").
    - `noReset`: Whether to reset app state before running (set to `True` to keep the app data).

2. **Run the Script:**

    Execute the script to start the automation process:

    ```bash
    python app.py
    ```


## Script Behavior

- **Login Automation:** Logs into the Facebook app using provided email and password.
- **Element Interaction:** Clicks on specified elements before and after login.
- **Menu Navigation:** Navigates to the menu tab in the app.
- **Orientation Change:** Toggles between portrait and landscape orientations.
- **Error Handling:** Attempts to handle the case where the "Skip" button might appear.

## Code Overview

- **Desired Capabilities:** Configures the connection to the Appium server and specifies app details.
- **Element Interaction:** Uses XPath to locate and interact with elements.
- **Orientation Management:** Changes the device orientation based on the current state.

## Troubleshooting

- **Appium Issues:** Ensure that the Appium server is running and configured correctly.
- **Device Connection:** Verify that the device or emulator is connected and accessible.
- **Element Locators:** Update XPath locators if the app's UI changes.
- **Authentication:** Make sure to replace `"your_username"` and `"password"` with valid credentials.

