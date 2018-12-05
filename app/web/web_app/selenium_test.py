from django.test import TestCase
from django.core.urlresolvers import reverse
import selenium
from selenium import webdriver
import requests
from .views import search_drivers

Class SeleniumTests(TestCase):
    
    def setUp(self):
        driver=webdriver.Chrome()
    
    def test_drivers_list_page(self):
        driver.get("localhost:8000//list_drivers")
        self.assertEquals(driver.find_element_by_css_selector('title').text, 'Drivers')
        self.assertTrue(len(driver.find_elements_by_css_selector('ul')) > 0)
    
    def test_create_driver_link(self):
        driver.get("localhost:8000//list_drivers")
        drivers=driver.find_elements_by_css_selector('a')
        new_driver_button=drivers[-1]
        new_driver_button.click()
        self.assertEquals(driver.get_element_by_css_selector('title').text, "Driver Information")
    
    def test_update_driver_link(self):
        driver.get("localhost:8000//list_drivers")
        drivers=driver.find_elements_by_css_selector('a')
        update_button=drivers[0]
        update_button.click()
        self.assertEquals(driver.get_element_by_css_selector('title').text, "Driver Information")     
    
    def test_404_page(self):
        driver.get("localhost:8000//list_drive")
        self.assertEquals(driver.get_element_by_xpath('//h1[./a]').text, 'warning')
                          
    def test_search_page(self):
        driver.get("localhost:8000//search")
        self.assertEquals(driver.get_element_by_css_selector('title').text, " Search Results ")
    
    def test_products_list_html(self):
        driver.get("localhost:8000//list_products")
        self.assertEquals(driver.find_element_by_css_selector('title').text, 'Product List')
        self.assertTrue(len(driver.find_elements_by_class_name)>0)
    
    def test_create_user_page(self):
        driver.get("localhost:8000//register")
        self.assertEquals(driver.find_element_by_css_selector('h1').text, 'Register')
        self.assertEquals(driver.find_element_by_class_name("mdl-button mdl-js-button mdl-js-ripple-effect"), 'Login to existing account') 
        
    
