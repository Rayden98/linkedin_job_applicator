from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set the path to your chromedriver executable
s = Service('C:/Users/MINED/Documents/Programs/chromedriver.exe')

# Create a ChromeOptions object to specify the profile
chrome_options = Options()

# Set the path to your custom Chrome profile
chrome_options.add_argument("user-data-dir=C:/Users/MINED/AppData/Local/Google/Chrome/User_Data/Profile_1")
chrome_options.add_argument("--profile-directory=Default")
# Pass the ChromeOptions object to the webdriver.Chrome constructor
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(5)

#email = driver.find_element(By.ID, "username")
#email.send_keys("rember98cjs@gmail.com")

#password = driver.find_element(By.ID, "password")
#password.send_keys("Alvara.Ju")

#button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
#button.click()

ease_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
ease_button.click()
time.sleep(4)
next_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
next_button.click()
time.sleep(4)
next_button2 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
next_button2.click()
time.sleep(4)
next_button3 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
next_button3.click()
time.sleep(4)
next_button4 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
next_button4.click()
time.sleep(4)
next_button5 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
next_button5.click()
time.sleep(4)
next_button6 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
next_button6.click()
time.sleep(4)
next_button7 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
next_button7.click()


time.sleep(12)

driver.quit()           # close the entire browser
print("It's Done")