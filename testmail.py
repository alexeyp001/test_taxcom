# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestOtchetnost():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_otchetnost(self):
    self.driver.get("https://cluster-test.taxcom.ru/")
    self.driver.set_window_size(1920, 1080)
    self.driver.find_element(By.LINK_TEXT, "Отчетность через интернет").click()
    self.driver.find_element(By.XPATH, "//div[4]/span[3]").click()
    self.driver.find_element(By.CSS_SELECTOR, "#col1 .btn-connect").click()
    self.driver.find_element(By.ID, "byPhone").click()
    self.driver.find_element(By.NAME, "form_text_792").click()
    self.driver.find_element(By.NAME, "form_text_792").send_keys("test")
    self.driver.find_element(By.NAME, "form_text_793").click()
    self.driver.find_element(By.NAME, "form_text_793").send_keys("1111111111")
    self.driver.find_element(By.ID, "submitOtchConnect").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Заявка принята!"


