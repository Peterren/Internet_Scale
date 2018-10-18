from django.test import TestCase, Client
from django.urls import reverse
from .models import Driver

class ListdriverTestCase(TestCase):
    #setUp method is called before each test in this class
    def setUp(self):
        self.driver1 = Driver.objects.create(first_name = "first", last_name  = "last", car_model = "test model", rating = 3.5)


    def success_response(self):
        drivers_list =  self.client.get("list_drivers")
        self.assertContains(drivers_list, 'Success')
        self.assertEqual(drivers_list.status_code, 200)
        self.assertTrue(drivers_list)

    #user_id not given in url, so error
    def fails_invalid(self):
        pass


    #tearDown method is called after each test
    def tearDown(self):
        self.driver1.delete()

class createdriverTestCase(TestCase):
    # setUp method is called before each test in this class
    def setUp(self):
        self.driver1 = Driver.objects.create(first_name="first", last_name="last", car_model="test model",
                                             rating=3.5)

    def success_response(self):
        response = self.client.post("create_user",
                                    {"first_name": "first1", "last_name": "last1", "car_model": "test model1",
                                     "rating": 4.0})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Success')

        drivers_list = self.client.get("list_drivers")
        self.assertContains(drivers_list, 'Success')
        self.assertEqual(drivers_list.status_code, 200)
        self.assertTrue(drivers_list)

    # user_id not given in url, so error
    def fails_invalid(self):
        pass

    # tearDown method is called after each test
    def tearDown(self):
        self.driver1.delete()

class updatedriverTestCase(TestCase):
    # setUp method is called before each test in this class
    def setUp(self):
        self.driver1 = Driver.objects.create(first_name="first", last_name="last", car_model="test model",
                                             rating=3.5)

    def success_response(self):
        response = self.client.post("update_user/1",
                                    {"first_name": "first2", "last_name": "last2", "car_model": "test model2",
                                     "rating": 5.0})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Success')


    # user_id not given in url, so error
    def fails_invalid(self):
        response = self.client.post("update_user/12314",
                                    {"first_name": "first2", "last_name": "last2", "car_model": "test model2",
                                     "rating": 5.0})
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Fail')

    # tearDown method is called after each test
    def tearDown(self):
        self.driver1.delete()

class deletedriverTestCase(TestCase):
    # setUp method is called before each test in this class
    def setUp(self):
        self.driver1 = Driver.objects.create(first_name="first", last_name="last", car_model="test model",
                                             rating=3.5)

    def success_response(self):
        response = self.client.post("delete_user/1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Success')

    # user_id not given in url, so error
    def fails_invalid(self):
        response = self.client.post("delete_user/1212414")

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Fail')

    # tearDown method is called after each test
    def tearDown(self):
        self.driver1.delete()

