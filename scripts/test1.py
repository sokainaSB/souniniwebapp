from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)  # Use 'Chrome' instead of 'chrome'
driver.maximize_window()
driver.get("https://yo.fan/cosmo")

page_title = driver.title
print(page_title)

driver.quit()
