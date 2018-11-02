from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from datetime import datetime
from django.test import TestCase
from .models import Driver, Product
from django.core.exceptions import ObjectDoesNotExist

# import Driver

class productTestCase(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(description = "Ride to Nova", price = 20.00, quantity = 2, id = 1)


    def test_listproducts(self):
        products_list =  self.client.get("/product/list")
        self.assertEqual(products_list.status_code, 200)
        self.assertEqual(products_list.json()["state"], 'Success')
        self.assertEqual(products_list.json()["products"][0]["description"], "Ride to Nova")

    def test_createproduct(self):
        response = self.client.post("/product/create",{"description": "Ride to VT", "price": 33.33, "quantity": 3})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Success')
        product = Product.objects.get(description = "Ride to VT")
        self.assertTrue(product)


    def test_getproduct(self):
        product =  self.client.get("/product/get/1")
        self.assertContains(product, 'Success')
        self.assertEqual(product.status_code, 200)
        self.assertTrue(product)
        self.assertEqual(product.json()["product"]["id"], 1)


    def test_failgetproduct(self):
        product = self.client.get("/product/get/13114")
        self.assertEqual(product.status_code, 404)
        self.assertEqual(product.json()["state"], 'Fail')
        self.assertEqual(product.json()["error"], "Id doesn't exist!")

    def test_updateproduct(self):
        response = self.client.post("/product/update/1", {"description": "Ride to New York", "price": 40.00, "quantity": 4})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Success')
        product = Product.objects.get(description="Ride to New York")
        self.assertTrue(product)

    def test_failupdateproduct(self):
        response = self.client.post("/product/update/13114",{"description": "Ride to New York", "price": 40.00, "quantity": 4})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["state"], 'Fail')
#

    def test_deleteproduct(self):
        response = self.client.post("/product/delete/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["state"], 'Success')
        with self.assertRaises(ObjectDoesNotExist):
            p = Product.objects.get(id = 1)


    # user_id not given in url, so error
    def test_faildeleteproduct(self):
        response = self.client.post("/product/delete/1212414")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["state"], 'Fail')

class driverTestCase(TestCase):
    def setUp(self):
        self.driver1 = Driver.objects.create(first_name = "first", last_name  = "last", car_model = "test model", rating = 3.5, id = 1)


    def test_listdriver(self):
        drivers_list =  self.client.get("/list_drivers")
        self.assertEqual(drivers_list.status_code, 200)
        self.assertEqual(drivers_list.json()["state"], 'Success')
        self.assertEqual(drivers_list.json()["drivers"][0]["first_name"], "first")

    def test_create(self):
        response = self.client.post("/create_user",{"first_name": "first1", "last_name": "last1", "car_model": "test model1","rating": 4.0})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Success')
        driver = Driver.objects.get(first_name = "first1")
        self.assertTrue(driver)

    def test_getdriver(self):
        driver =  self.client.get("/get_driver/1")
        self.assertContains(driver, 'Success')
        self.assertEqual(driver.status_code, 200)
        self.assertEqual(driver.json()["driver"]["id"], 1)

    def test_failgetdriver(self):
        driver = self.client.get("/get_driver/13114")
        self.assertEqual(driver.status_code, 404)
        self.assertEqual(driver.json()["state"], 'Fail')
        self.assertEqual(driver.json()["error"], "Id doesn't exist!")

    def test_update(self):
        response = self.client.post("/update_user/1",{"first_name": "first2", "last_name": "last2", "car_model": "test model2","rating": 5.0})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Success')
        driver = Driver.objects.get(first_name="first2")
        self.assertTrue(driver)

    def test_failupdate(self):
        response = self.client.post("/update_user/13114",{"first_name": "first2", "last_name": "last2", "car_model": "test model2", "rating": 5.0})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["state"], 'Fail')
#

    def test_delete(self):
        response = self.client.post("/delete_user/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["state"], 'Success')
        with self.assertRaises(ObjectDoesNotExist):
            d = Driver.objects.get(id = 1)


    # user_id not given in url, so error
    def test_faildelete(self):
        response = self.client.post("/delete_user/1212414")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["state"], 'Fail')
