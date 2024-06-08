from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/place/KFC+Mirpur/@23.8148686,90.3636178,17z/data=!3m1!4b1!4m6!3m5!1s0x3755c12f4d8798b9:0x4fb662d896d1a4c3!8m2!3d23.8148637!4d90.3661927!16s%2Fg%2F1tg2j0m1?entry=ttu")

# review = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[41]/div/div/div[4]/div[2]/div/span[1]').text()
reviews = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[40]/div/div/div[4]/div[2]/div/span')))
print(reviews.text)
time.sleep(10)
time.sleep(10)