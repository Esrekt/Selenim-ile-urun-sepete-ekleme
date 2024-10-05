from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
def fonkum():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    mailim="bulutesreferen@gmail.com"
    sifre="Trabzon0661."
    driver=webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    driver.get("https://www.trendyol.com/fobun/jbl-kulaklik-pedi-jbl-450bt-460-500bt-510bt-tune-600-t250-jbl-kulaklik-sungeri-jbl-kulaklik-yastigi-p-381596081/saticiya-sor?boutiqueId=61&merchantId=400943&sav=true&tag=stok")

    # 'KABUL ET' butonuna tıklama
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

    stok= driver.find_element(By.XPATH, "//button[@class='ps-tags__tag ps-tags__tag--active']")
    stoklar=stok.text
    stok_sayisi = stoklar.split("(")[-1].split(")")[0]

    return stok_sayisi

