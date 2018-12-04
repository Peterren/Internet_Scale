from django.test import TestCase
from django.core.urlresolvers import reverse
import selenium
from selenium import webdriver
import requests


class TestLoads(TestCase):
    """Test suite for the web front-end."""
    def setUp(self):
        pass

    def test_homepage_loads(self):
        """Verify the homepage loads"""
        resp = requests.get('http://localhost:8000/')
        self.assertEquals(resp.status_code, 200)

    def test_lottery_main_loads(self):
        """Verify the main lottery page loads"""
        resp = requests.get('http://localhost:8000/lotteries')
        self.assertEquals(resp.status_code, 200)

    def test_lottery_detail_loads(self):
        """Verify the lottery detail pages load"""
        resp = requests.get('http://localhost:8000/lotteries/1')
        self.assertEquals(resp.status_code, 200)

    def test_card_main_loads(self):
        """Verify the main card page loads"""
        resp = requests.get('http://localhost:8000/cards')
        self.assertEquals(resp.status_code, 200)

    def test_card_detail_loads(self):
        """Verify the card detail pages load"""
        resp = requests.get('http://localhost:8000/cards/1')
        self.assertEquals(resp.status_code, 200)

    def test_login_loads(self):
        """Verify the login page loads"""
        resp = requests.get('http://localhost:8000/login')
        self.assertEquals(resp.status_code, 200)

    def test_register_loads(self):
        """Verify the register page loads"""
        resp = requests.get('http://localhost:8000/register')
        self.assertEquals(resp.status_code, 200)

    def test_bad_url(self):
        """Verify that an invalid URL returns the 404 page, not an error."""
        resp = requests.get('http://localhost:8000/asdf')
        self.assertEquals(resp.status_code, 200)

    def tearDown(self):
        pass
    
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
        
    
