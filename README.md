# This is an exercise in seeing how accessible I am able to make an automatic course enroller through both extensive documentation and simplistic code.

## Prerequisites 
**To correctly operate this program you will require both Python and Selenium, but I'll give links showing you how to install both of those here.**

Note: My version of this script uses chrome, so that should be installed.

**Python**

Here's a very straightforward link on how to install Python for windows: https://realpython.com/installing-python/#windows

**Selenium**

Once Python is installed, open command prompt (press the windows key and r at the same time, then type cmd and hit enter). 
Once command prompt has been opened, type `pip install selenium` and hit enter. This should, if Python is installed correctly, install selenium.

## Set-Up
Before your enrollment date, you will need to fill the Python file with your specific information so that it will work properly for you. This can be done in any text editor, including just Notepad.

1. Download the files provided and store that folder wherever is convenient.
2. Open main.py and populate the username and password fields.
3. This is the hard part, but I'll include some graphics to make it easier. We will need to use inspect element to give our Python program the buttons to click for each class.

    - Go to the my cart section of Student Registration.
    - Open up developer tools in chrome, this can be done by hitting f12.
    - For each class in your cart, inspect its source (check provided pictures) by clicking on the button in the top left of the        developer inspect element pane and then clicking on the button for the class.
    - Once this is done, right click on the part of the source code that will now be highlighted in the inspect element pane and click copy, then copy XPath and store the value somewhere. (You should get something that looks like this `//*[@id="yui-gen26-button"]`) 
    ![Instructions for Class Button](https://i.imgur.com/esbQRV4.png)
    - Now, we need to do the same thing but for the *Waitlist if Full* option for each class. Click on the little button for the enrollment options and then use developer tools to select the *Waitlist if Full* option for your chosen class. Then, right click and copy XPath as we did above. (You should get something like this: `//*[@id="yui-gen52"]/a`)
    ![Instructions for Waitlist If Full](https://i.imgur.com/a1F6Jxt.png)
    - Okay, almost done! Now our final step is to use the values we just got in our main.py file.
    - Open up main.py and scroll down, you will see a couple of code blocks like this:
    ```
    browser.find_element_by_xpath('//*[@id="yui-gen32-button"]').click()
    browser.find_element_by_xpath('//*[@id="yui-gen55"]/a').click()
    ```
    Simply replace the values inside the single quotes (') with the ones you got from the XPaths. Now, that code block should instead look like this:
    ```
    browser.find_element_by_xpath('//*[@id="yui-gen26-button"]').click()
    browser.find_element_by_xpath('//*[@id="yui-gen52"]/a').click()
    ```
    - And we're done! You need one of these code blocks for each of the classes you're enrolling in (in my case I was enrolling in five classes so I had five such code blocks.)
    - Now, when the time comes to enroll, simply run the script (which will open the enrollment page and click waitlist if full for all configured items), scroll down and hit enroll. 
    
    
 **Note: If you want the script to automatically run at 7 am (Vandy enrollment time) uncomment the designated part at the beginning of main.py. Now the script, once ran a bit before 7 AM, should open the web browser at exactly 7 am and select all your classes for you.**
    

    
    



