from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# ✅ Positive Test Case: Valid Login
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "logged-in-successfully" in driver.current_url:
    print("✅ Positive Test Passed: Login successful")
else:
    print("❌ Positive Test Failed: Login failed")

# ❌ Negative Test Case 1: Empty Fields
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "submit").click()
time.sleep(1)

try:
    error = driver.find_element(By.ID, "error").text
    print("❌ Negative Test Passed: Empty field error -", error)
except:
    print("❌ Negative Test Failed: No error for empty fields")

# ❌ Negative Test Case 2: Invalid Credentials
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

try:
    error = driver.find_element(By.ID, "error").text
    print("❌ Negative Test Passed: Invalid credentials -", error)
except:
    print("❌ Negative Test Failed: No error for invalid login")

# Close the browser
driver.quit()
