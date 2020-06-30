from selenium import webdriver
import os
import config as conf
import time


class surf(object):
    
    def __init__(self):
        driver_path = './chromedriver' 
        self.driver = webdriver.Chrome(driver_path)
        
    
    def login(self):
        # Get user informations
        EMAIL = conf.email
        PASS = conf.password

        self.driver.get("https://www.facebook.com/")

        # Get xpaths
        email_xpath = '//*[@id="email"]' 
        pass_xpath = '//*[@id="pass"]'
        login_button_xpath = '//*[@id="u_0_b"]' 

        # Get elements
        email_element = self.driver.find_element_by_xpath(email_xpath)
        pass_element = self.driver.find_element_by_xpath(pass_xpath)
        login_button_element = self.driver.find_element_by_xpath(login_button_xpath)

        # Send data
        email_element.send_keys(EMAIL)
        pass_element.send_keys(PASS)
        login_button_element.click()

        time.sleep(5) # seconds
        # self.driver.quit()


    def follow(self, url, fbtype):
        
        try:
            if str(fbtype) == 'follow1.txt':
                follow_button_xpath = '//*[@id="u_ps_0_0_2"]' # for facebook profle
            else:
                follow_button_xpath = '//*[@id="u_0_z"]/div/div/div[2]/button' # for facebook page
                
            self.driver.get(url)
            follow_button_element = self.driver.find_element_by_xpath(follow_button_xpath)
            self.driver.execute_script("arguments[0].click();", follow_button_element)
        except:
            print("[INFO] Already followed / Not found follow button xpath")
            
        # follow_button_element.click()
        # self.driver.quit()
        
    
if __name__ == "__main__":
    
    s1 = surf()
    logged_in = False
    
    with open(conf.filename) as f:
        lines = list(line for line in (l.strip() for l in f) if line)
        
        for line in lines:
            line = line.strip()
            
            if len(line) > 0:
                url = line.split(' - ')[1]
                print(url)
                
                if logged_in == False:
                    s1.login()
                    logged_in = True

                s1.follow(url, conf.filename)
                