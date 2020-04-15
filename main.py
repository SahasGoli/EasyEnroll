from selenium import webdriver
import datetime

# Hit run a couple minutes before enrollment starts.
# Uncomment this if you want it to activate exactly when enrollment begins
# while True:
#     current_hour = datetime.datetime.now()
#     if current_hour.hour == 7:  # This is set for 7 AM Vanderbilt time, change this digit to reflect your time-zone.
#         print("It's time to enroll!")
#         break;

# Fill in these with your username and password!
username = 'YOUR_VUNET_ID'
password = 'YOUR_PASSWORD'

# Opens up the browser and navigates to the my cart section of student registration
browser = webdriver.Chrome()
browser.get('http://yes.vanderbilt.edu/')

usernameInput = browser.find_element_by_xpath('//*[@id="username"]')
passwordInput = browser.find_element_by_xpath('//*[@id="password"]')

usernameInput.send_keys(username)
passwordInput.send_keys(password)

signOnButton = browser.find_element_by_xpath('/html/body/div/div[2]/div/form/div[6]/a')
signOnButton.click()

navToStudentRegistration = browser.find_element_by_xpath('//*[@title="Student Registration"]')
navToStudentRegistration.click()

browser.implicitly_wait(10)
termSelect = Select(browser.find_element_by_xpath('//*[@id="selectedTerm"]'))
termSelect.select_by_index(0)

navToCart = browser.find_element_by_xpath('//*[@id="savedClassesContextMenuItem"]/div[2]')
navToCart.click()

# We are waiting for the cart to load

browser.implicitly_wait(100000)
# Now select waitlist if enrolled for all the courses
# Note: THESE IDs are SPECIFIC to your classes. You must update them.

# Class 1
browser.find_element_by_xpath('//*[@id="yui-gen26-button"]').click()
browser.find_element_by_xpath('//*[@id="yui-gen52"]/a').click()

# Class 2
browser.find_element_by_xpath('//*[@id="yui-gen32-button"]').click()
browser.find_element_by_xpath('//*[@id="yui-gen55"]/a').click()

# Class 3
browser.find_element_by_xpath('//*[@id="yui-gen36-button"]').click()
browser.find_element_by_xpath('//*[@id="yui-gen58"]/a').click()

# Class 4
browser.find_element_by_xpath('//*[@id="yui-gen44-button"]').click()
browser.find_element_by_xpath('//*[@id="yui-gen61"]/a').click()

# Class 5
browser.find_element_by_xpath('//*[@id="yui-gen46-button"]').click()
browser.find_element_by_xpath('//*[@id="yui-gen64"]/a').click()

# Click enroll after everything is done running.
browser.find_element_by_xpath('//button[text()="Enroll"]').click()
