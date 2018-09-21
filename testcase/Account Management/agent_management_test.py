from comon import login
from selenium import webdriver
from time import sleep
import unittest

driver = webdriver.Chrome()
userlogin = login.login_lgagent(driver)
userlogin.loginon('huanghh','123456')
sleep(3)


def open_agentpage(self):
    '''打开代理管理页'''
    driver.find_element_by_xpath('//*[@id="navLeftt"]/ul/li[2]/div/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="navLeftt"]/ul/li[2]/ul/li[1]/span').click()
    sleep(1)
    agent_title = self.driver.find_element_by_id('tab-agentManager').text
    print(agent_title)
    self.assertEqual(agent_title, '代理管理')

def search_agent(self):
    '''查询代理 kakaxi'''
    driver.find_element_by_css_selector(
        '#pane-agentManager > div.hall > div > div > form > div:nth-child(1) > div > div > input').send_keys('kakaxi')
    driver.find_element_by_css_selector(
        '#pane-agentManager > div.hall > div > div > form > div:nth-child(2) > div > div > div > input').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()
    driver.find_element_by_xpath('//*[@id="pane-agentManager"]/div[1]/div/div/form/div[3]/div/button').click()
    sleep(3)
    agent_number = driver.find_element_by_xpath('//*[@id="agentManager"]/div[2]/span[1]').text
    self.assertIn('1',agent_number)

class open_tab(unittest.TestCase):
    def setUp(self):
        '''点开详情'''
        self.driver.find_element_by_xpath('//*[@id="pane-agentManager"]/div[2]/div[3]/table/tbody/tr/td[1]/div/div').click()

    def edit_agent(self):
        '''编辑代理商'''
        driver.find_element_by_xpath(
            '/html/body/div/section/section/main/div[1]/div[1]/div[2]/div/div[2]/div[3]/table/tbody/tr[2]/td/button[1]').click()
        sleep(1)
        driver.find_element_by_css_selector(
            '#message > div.left.message-right > div:nth-child(3) > div > div > input').clear()
        sleep(1)
        driver.find_element_by_css_selector(
            '#message > div.left.message-right > div:nth-child(3) > div > div > input').send_keys('huang@34era.com')
        sleep(3)
        driver.find_element_by_css_selector('#message > div.save > button > span').click()

    def search_agent(self):
        '''查看代理商'''
        driver.find_element_by_xpath('//*[@id="pane-agentManager"]/div[2]/div[3]/table/tbody/tr[2]/td/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[4]/div/div[1]/div/div/i').click()
        '''查看代理商后没有关闭展开功能，下面修改密码执行会报错，待调整'''

    def change_pswsed(self):
        '''修改密码成功'''
        driver.find_element_by_css_selector(
            '#pane-agentManager > div.el-table.el-table--fit.el-table--enable-row-hover.el-table--enable-row-transition.el-table--small > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(2) > td > button:nth-child(3)').click()
        driver.find_element_by_css_selector(
            '#agentManager > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div > div > input').send_keys(
            '123456')
        driver.find_element_by_css_selector(
            '#agentManager > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div > div > input').send_keys(
            '123456')
        sleep(3)
        driver.find_element_by_css_selector(
            '#agentManager > div:nth-child(3) > div > div.el-dialog__footer > div > button').click()
        sleep(5)

    def change_status(self):
        '''修改状态'''
        driver.find_element_by_xpath('//*[@id="pane-agentManager"]/div[2]/div[3]/table/tbody/tr[2]/td/button[4]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[7]/div/div[2]/form/div[1]/div/div/div/input').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[7]/div/div[2]/form/div[2]/div/div/input').clear()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[7]/div/div[2]/form/div[2]/div/div/input').send_keys('自动化测试')
        sleep(3)
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[7]/div/div[3]/div/button').click()
        sleep(2)

    def change_EmailPhone(self):
        '''修改手机邮箱'''
        driver.find_element_by_xpath('//*[@id="pane-agentManager"]/div[2]/div[3]/table/tbody/tr[2]/td/button[5]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[8]/div/div[2]/form/div[1]/div/div/input').clear()
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[8]/div/div[2]/form/div[1]/div/div/input').send_keys('huanghh@34era.com')
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[8]/div/div[2]/form/div[2]/div/div[1]/input').clear()
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[8]/div/div[2]/form/div[2]/div/div[1]/input').send_keys('100')
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[8]/div/div[2]/form/div[2]/div/div[2]/input').clear()
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[8]/div/div[2]/form/div[2]/div/div[2]/input').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="agentManager"]/div[8]/div/div[3]/div/button').click()
        sleep(3)


