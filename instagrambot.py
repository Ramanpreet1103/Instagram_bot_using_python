from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.ie.webdriver import DEFAULT_SERVICE_LOG_PATH



def openinsta():
    driver = webdriver.Firefox()

    driver.get("https:\\www.instagram.com")

    time.sleep(5)

    username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")

    #<------USERNAME HERE ----------------------------------------------------------------------------------------->                                         
    username.send_keys("ENTER YOUR USERNAME HERE")

    password = driver.find_element_by_css_selector("div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")

    #<------PASSWORD HERE ------------------------------------------------------------------------------------------>
    password.send_keys("ENTER YOUR PASSWORD HERE")
    password.send_keys(Keys.ENTER)
    time.sleep(5)
    saveinfo = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    saveinfo.send_keys(Keys.ENTER)
    time.sleep(5)
    # notification = driver.find_element_by_css_selector("button.aOOlW:nth-child(2)")
    # notification = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    notification = driver.find_element_by_css_selector("button.aOOlW:nth-child(2)")
    notification.send_keys(Keys.ENTER)
    time.sleep(5)
    search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    search.send_keys("#pythonprojects")
    search.send_keys(Keys.ENTER)

    time.sleep(4)

    search.send_keys(Keys.ENTER)

    search.send_keys(Keys.ENTER)
    likeandcommentposts(driver)

def likeandcommentposts(driver):         
    # driver = webdriver.Firefox()
    time.sleep(5)
            # post = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]").click()

    driver.find_elements_by_css_selector("article > div > div >div >div > div")[0].click()

    while True:
        time.sleep(3)
        post = driver.find_element_by_css_selector("div[role='button'] img[srcset]")
            # post = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[3]/div[3]")
        action_chains = ActionChains(driver)
        action_chains.double_click(post).perform()
            # nextpost
        driver.find_element_by_css_selector(".Ypffh").click()
        comment = driver.find_element_by_css_selector(".Ypffh")
        comment.send_keys("Hey! Nice Post")
        time.sleep(0.5)
        comment.send_keys(Keys.ENTER)
        time.sleep(2)
            #next post 
        driver.find_element_by_css_selector("._65Bje").click()
if __name__ == "__main__":
    openinsta()
    
