import time

from selenium import webdriver

driver = webdriver.Chrome() # Directly refer to this instead
driver.get('https://google.com')
time.sleep(5)
print(driver.title)

""" Updated using drivers on Selenium. Normally would have to install a chrome driver to use chrome application.
Now this included in Selenium so there's no need to refer to any external file.
 """
