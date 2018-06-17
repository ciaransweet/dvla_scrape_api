from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.PhantomJS()

driver.get('https://vehicleenquiry.service.gov.uk')


def wait_for_presence_and_get_element_by_id(id_to_find):
    element_present = EC.presence_of_element_located((By.ID, id_to_find))
    WebDriverWait(driver, 10).until(element_present)
    return driver.find_element_by_id(id_to_find)


def wait_for_presence_and_get_element_by_xpath(xpath_to_find):
    element_present = EC.presence_of_element_located((By.ID, xpath_to_find))
    WebDriverWait(driver, 20).until(element_present)
    return driver.find_element_by_id(xpath_to_find)


def enter_car_reg(car_reg):
    element = wait_for_presence_and_get_element_by_id('Vrm')
    element.send_keys(car_reg)
    element.submit()


def confirm_reg():
    element = wait_for_presence_and_get_element_by_id('Correct_True')
    element.click()


def check_is_taxed():
    element = wait_for_presence_and_get_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[1]/h2')
    print(element.text)


enter_car_reg('ET53 LKK')
confirm_reg()
check_is_taxed()
