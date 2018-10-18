from django.test import TestCase, Client
from django.urls import reverse
from .models import Driver

class GetOrderDetailsTestCase(TestCase):
    #setUp method is called before each test in this class
    def setUp(self):
        self.client = Client()
        self.driver1 = Driver.objects.create(first_name = "first", last_name  = "last", car_model = "test model", rating = 3.5)


    def success_response(self):
        #assumes user with id 1 is stored in db
        # response = self.client.post("create_user", {"first_name" : "first1", "last_name"  : "last1", "car_model" : "test model1", "rating" : 4.0})

        #checks that response contains parameter order list & implicitly
        # self.assertContains(response, 'Success')
        # # checks that the HTTP status code is 200
        # self.assertEqual(response.status_code, 200)

        drivers_list =  self.client.get("list_drivers")
        self.assertContains(drivers_list, 'Success')
        self.assertEqual(drivers_list.status_code, 200)
        self.assertTrue(drivers_list)


    #user_id not given in url, so error
    # def fails_invalid(self):
        # response = self.client.get("create_user")
        # self.assertEquals(response.status_code, 404)

    #tearDown method is called after each test
    def tearDown(self):
        self.driver1.delete()