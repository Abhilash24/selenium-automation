from selenium import webdriver

driver = webdriver.Chrome('/home/abhilash/Downloads/chromedriver_new/chromedriver')
driver.get('http://codepad.org')

# click radio button
python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
python_button.click()

# type text
text_area = driver.find_element_by_id('textarea')
text_area.send_keys("print('Hello World')")

# click submit button
submit_button = driver.find_elements_by_xpath('//*[@id="editor-form"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/button')[0]
submit_button.click()