from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import queries as DB
import datetime

#import bs4 as bs




print("Scrapping...")

opts = webdriver.ChromeOptions()

#Cambiar la ruta para el ejecutable de chrome
opts.binary_location = "D:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";



browser = webdriver.Chrome(chrome_options=opts)
browser.get("https://www.titicupon.com/titicupon?term_node_tid_depth=All&tid_1=7361")
elements = browser.find_elements_by_class_name('grid-item')
e = [x.text for x in elements[:-6]]

cupons = []

def scrap():
    getnode = browser.find_element_by_class_name('node')
    node = getnode.get_attribute("id")
    title = browser.find_element_by_xpath("//*[@id='" + node +"']/div[1]/h1")
    subtitle = browser.find_element_by_xpath("//*[@id='" + node +"']/div[1]/h2")
    img = browser.find_element_by_xpath('//*[@id="views_slideshow_singleframe_div_cupones-block_14_0"]/div/img')
    imgSrc = img.get_attribute("src")
    price = browser.find_element_by_xpath('//*[@id="' + node +'"]/div[1]/div[2]/div/h3')
    normalPrice = browser.find_element_by_xpath('//*[@id="' + node +'"]/div[1]/div[2]/div/h4')
    save = browser.find_element_by_xpath("//*[@id='" + node + "']/div[1]/div[2]/div/div[2]/div[1]/p")
    save = browser.find_element_by_xpath('//*[@id="' + node + '"]/div[1]/div[2]/div/div[1]/span')    
    sold = browser.find_element_by_xpath("//*[@id='" + node +"']/div[1]/div[2]/div/div[2]/div[1]/p")
    hour = browser.find_element_by_xpath('//*[@id="' + node +'"]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/span[1]')
    minutes = browser.find_element_by_xpath('//*[@id="' + node +'"]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span[1]')
    seconds = browser.find_element_by_xpath('//*[@id="' + node +'"]/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/span[1]')
    exactHour = hour.text + ":" + minutes.text + ":" + seconds.text
    city = browser.find_element_by_xpath('//*[@id="' + node +'"]/div[2]/div[2]/ul/li[1]')
    period = browser.find_element_by_xpath('//*[@id="' + node +'"]/div[2]/div[2]/ul/li[2]/span[2]')
    horary = browser.find_element_by_xpath('//*[@id="' + node +'"]/div[2]/div[2]/ul/li[3]')
    direction = browser.find_element_by_xpath('//*[@id="' + node +'"]/div[2]/div[2]/ul/li[4]')
    location = browser.find_element_by_xpath('//*[@id="gmap-auto1map-gmap0"]/div/div/div[2]/a')
    locationSrc = location.get_attribute("href")

    
    cuponData = [title.text, subtitle.text, imgSrc, price.text, normalPrice.text, save.text, sold.text, exactHour,
                 city.text, period.text, horary.text, direction.text, locationSrc]
    try:
        website = browser.find_element_by_xpath('//*[@id="' + node +'"]/div[3]/div[1]/ul/li[1]/a')
        websiteSrc = website.get_attribute("href")
        cuponData.append(websiteSrc)
    except NoSuchElementException:
        cuponData.append("null")

    try:
        facebook = browser.find_element_by_xpath('//*[@id="' + node +'"]/div[3]/div[1]/ul/li[2]/a')
        facebookSrc = facebook.get_attribute("href")
        cuponData.append(facebookSrc)
    except:
        cuponData.append("null")
    
    cupons.append(cuponData)


row = 1
column = 1
for i in range(len(e)):
    browser.find_element_by_xpath("//*[@id='page']/div[4]/div/div[1]/div[3]/div[3]/div/div[" + str(row) + "]/div[" + str(column) + "]/div/div[3]/a").click()
    
    scrap()
    browser.back()
    if column == 4: 
        column = 1
        row += 1
    else:
        column += 1



DB.insertAuditoria(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Sin errorres", "Finalizado", len(cupons))

DB.insertCuponInfo(cupons)





