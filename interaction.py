from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "/home/bctech/Desktop/chrome//chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#driver.get("https://en.wikipedia.org/wiki/Main_Page")
#figure = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
#print(figure.text)


#driver.get("https://en.wikipedia.org/wiki/Main_Page")
#portal = driver.find_element(By.LINK_TEXT, "Content portals")
#portal.click()

#driver.get("https://stackoverflow.com/questions/33287847/python-selenium-input-textbox-send-keys-not-working")
#python = driver.find_element(By.NAME, "q")
#python.send_keys("boy")
#python.send_keys(Keys.ENTER)
#python.send_keys(Keys.ENTER)


driver.get("https://sso.teachable.com/secure/37913/identity/login/password")
form = driver.find_element(By.CLASS_NAME, ".email")
form.send_keys("essublessing1@gmail.com")

# driver.get("https://www.google.com/")
# form = driver.find_element(By.NAME, "q")
# form.send_keys("Blessing")
# form.send_keys(Keys.ENTER)




driver.quit()