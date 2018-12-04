from django.test import TestCase
from django.core.urlresolvers import reverse
import selenium
from selenium import webdriver
import requests

Class SeleniumTests:
    
    def test_drivers_list_html:
        driver=webdriver.chrome()
        driver.get("localhost:8000//list_drivers")
        self.assertEquals(driver.find_element_by_css_selector('title').text, 'Drivers')
        self.assertTrue(len(driver.find_elements_by_css_selector('ul')) > 0)
    
    def test_products_list_html:
        driver=webdriver.chrome()
        driver.get("localhost:8000//list_products")
        self.assertEquals(driver.find_element_by_css_selector('title').text, 'Product List')
        self.assertTrue(len(driver.find_elements_by_class_name)>0)
    
    def test_create_user_page:
        driver=webdriver.chrome()
        driver.get("localhost:8000//register")
        self.assertEquals(driver.find_element_by_css_selector('h1').text, 'Register')
        self.assertEquals(driver.find_element_by_class_name("mdl-button mdl-js-button mdl-js-ripple-effect"), 'Login to existing account') 
        
    
