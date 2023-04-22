from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "/home/bctech/Desktop/chrome//chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#driver.get("https://www.python.org/")
#logo = driver.find_element(By.CLASS_NAME, "python-logo")
#print(logo.size)

#find_element_by_css_selector
#driver.get("https://www.python.org/")
#documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget")
#print(documentation_link.text)

#find_element_by_xpath
#driver.get("https://www.python.org/")
#bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
#print(bug_link.text)

#find-elements
#driver.get("https://www.python.org/")
#event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
#event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
#events = {}

#for n in range(len(event_time)):
  #  events[n] = {
   #     "time": event_time[n].text,
   #     "name": event_name[n].text,
    #}
#print(events)



#driver.close()





driver.quit()
