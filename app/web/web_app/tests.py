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
    
