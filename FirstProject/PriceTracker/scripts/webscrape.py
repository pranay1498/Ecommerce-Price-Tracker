#functions to scrape different websites
from selenium import webdriver

# path for chromedriver.exe
PATH = r"C:\Users\verma\OneDrive\Desktop\woc3.0-ecommerce-price-tracker-PranayJoshi\FirstProject\PriceTracker\scripts\chromedriver.exe"

# to open browser without window
options = webdriver.ChromeOptions()
#options.add_argument("headless")
#options.add_argument('window-size=1920x1080')


# scrape amazon links and return product details in dictionary
def scrapeAmazon(link):
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.get(link)
    driver.implicitly_wait(10)
    title_element = driver.find_element_by_id("title")
    price_element = driver.find_element_by_xpath("//span[contains(@id,'priceblock_')]")
    stock_element = driver.find_element_by_id("availability")
    product_title = title_element.text
    product_price = int(''.join(filter(str.isdigit, (price_element.text).split('.')[0])))
    product_stock = stock_element.text
    datadict = {'title': product_title, 'price': product_price, 'availability': product_stock}
    driver.close()
    return datadict


# scrape flipkart links and return product details in dictionary

def scrapeFlipkart(link):
    driver = webdriver.Chrome(PATH, options=options)
    driver.get(link)
    driver.implicitly_wait(5)
    title_element = driver.find_element_by_xpath("//span[contains(@class,'B_NuCI')]")
    price_element = driver.find_element_by_xpath("//div[contains(@class,'_30jeq3 _16Jk6d')]")
    product_title = title_element.text
    product_price = int(''.join(filter(str.isdigit, (price_element.text).split('.')[0])))
    datadict = {'title': product_title, 'price': product_price, 'availability': ''}
    driver.close()
    return datadict

# scrape ebay links and return product details in dictionary

def scrapeEbay(link):
    driver = webdriver.Chrome(PATH, options=options)
    driver.get(link)
    driver.implicitly_wait(5)
    title_element = driver.find_element_by_id("itemTitle")
    price_element = driver.find_element_by_id("prcIsum")
    product_title = title_element.text
    product_price = int(''.join(filter(str.isdigit, (price_element.text).split('.')[0])))
    datadict = {'title': product_title, 'price': product_price, 'availability': ''}
    driver.close()
    return datadict
