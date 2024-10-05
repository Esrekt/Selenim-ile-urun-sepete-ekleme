from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import fonku

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
mailim="bulutesreferen@gmail.com"
sifre="Trabzon0661."
mailim=""
sifre=""
driver=webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.trendyol.com/giris?cb=%2F")

driver.find_element(By.ID,"login-email").send_keys(mailim)
driver.find_element(By.ID,"login-password-input").send_keys(sifre)

driver.find_element(By.XPATH, '//button[@type="submit"]').click()

driver.get("https://www.trendyol.com/fobun/jbl-kulaklik-pedi-jbl-450bt-460-500bt-510bt-tune-600-t250-jbl-kulaklik-sungeri-jbl-kulaklik-yastigi-p-381596081?boutiqueId=61&merchantId=400943&sav=true")
sleep(5)
driver.find_element(By.XPATH, "//button[@class='onboarding-popover__default-renderer-primary-button']").click()
a=fonku.fonkum()
a=int(a)
print(a)
if a > 0:
    driver.find_element(By.CLASS_NAME, "add-to-basket-button-text").click()

sleep(400)






