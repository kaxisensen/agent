from selenium import webdriver

from time import sleep


class login_lgagent():
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def loginon(self, username, psw):
        self.driver.get('https://test.lgagent.lggame.co/#/login')
        sleep(2)
        self.driver.find_element_by_css_selector(
            '#login_form > div > div.login-body > ul > li:nth-child(1) > input').send_keys(username)
        self.driver.find_element_by_css_selector(
            '#login_form > div > div.login-body > ul > li:nth-child(2) > input').send_keys(psw)
        self.driver.find_element_by_css_selector(
            '#login_form > div > div.login-body > ul > li.clear > input').send_keys('66666')
        sleep(1)
        self.driver.find_element_by_css_selector('#login_form > div > div.login-body > button').click()


# if __name__ == "__main__":
#     # unittest.main()
#     driver = webdriver.Chrome()
#     a = login_lgagent(driver)
#     a.loginon('huanghh', '123456')
#     # driver.quit()
