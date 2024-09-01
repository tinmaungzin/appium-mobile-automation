from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    "platformName": "Android",   
    "deviceName": "R9AMB0XZMNJ",
    "appPackage": "com.facebook.katana",
    "appActivity": "com.facebook.katana.LoginActivity",
    "automationName": "UiAutomator2",   
    "noReset": True,
    "newCommandTimeout": 600,
    "orientation": "PORTRAIT"
}

driver = webdriver.Remote('http://127.0.0.1:4723', 
    options=AppiumOptions().load_capabilities(desired_caps))
wait = WebDriverWait(driver, 20)

def click_element_before_login(xpath):
    element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))
    element.click()
    time.sleep(5)   
    window_size = driver.get_window_size()
    # Tap at the center of the screen
    driver.tap([(window_size['width'] // 2, window_size['height'] // 2)])

def login(email, password):
    email_field = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.facebook.katana:id/(name removed)'])[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText")))
    email_field.send_keys(email)
    password_field = driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.facebook.katana:id/(name removed)'])[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText")
    password_field.send_keys(password)
    login_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Log in']")
    login_button.click()

    time.sleep(20)

    try:
        skip_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@text='Skip']"))
        )
        if skip_button:
            skip_button.click()
    except Exception as e:
        print("Skip button not found or already dismissed.")

    menu = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc='Menu, tab 6 of 6']")))
    menu.click()

def navigate_to_menu():
    menu = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc='Menu, tab 6 of 6']")))
    menu.click()

def change_orientation():
    if driver.orientation == "PORTRAIT":
        driver.orientation = "LANDSCAPE"
    else:
        driver.orientation = "PORTRAIT"

click_element_before_login("//android.view.View[@content-desc='Log into another account']")   
login("your_username", "password")
navigate_to_menu()
change_orientation()

driver.quit()
