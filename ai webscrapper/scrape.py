from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By


def scrape_website(website):
    print("launching chrome browser..")
    
#AUTH = 'brd-customer-hl_5bd18b6c-zone-ai_scraper:6yt01xyg4msl'
#SBR_WEBDRIVER = "brd-customer-hl_5bd18b6c-zone-ai_scraper:6yt01xyg4msl@brd.superproxy.io:9515"
AUTH = 'brd-customer-hl_5bd18b6c-zone-ai_scraper:6yt01xyg4msl'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'
def main():
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
       driver.get(website)  
       print('Taking page screenshot to file page.png')
       driver.get_screenshot_as_file('./page.png')
       print('Navigated! Scraping page content...')
       html = driver.page_source
       return html
if __name__ == '__main__':
  main()

   # chrome_driver_path = "chromedriver.exe"
    #options = webdriver.ChromeOptions()
    #driver =  webdriver.Chrome(service=Service(chrome_driver_path),options=options)

    #try:
        #driver.get(website)
        #print("page loaded.....")
       # html=driver.page_source
      #  time.sleep(10)

     #   return html
    #finally:
     #   driver.quit()
