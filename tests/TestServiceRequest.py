import unittest
from unittest import TestCase


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestCase

    def test_service_request_encoded(self) -> None:

        dataset_dict = {"username": "",
                        "firstName": "John",
                        "lastName": "Doe",
                        "account_number": "",
                        "type": "1001",
                        "subtype": "1009",
                        "address": "0A, Beach Road, Muizenberg",
                        "street_number": "0A",
                        "street": "BeachRoad",
                        "suburb": "Muizenberg", "telephone": "0835559876",
                        "email": "j.doe@gmail.com",
                        "message": "Pleasecollect the whale carcass from Muizenberg beach before the wind direction changes.",
                        "latitude": "-34.108038128850701298",
                        "longitude": "18.471525907516479492", "comm": "EMAIL"}

        response = self.client.post('/books/', json=dataset_dict)

        self.assertEqual(200, response.status_code)
        self.assertEqual(dataset_dict, response.json())

if __name__ == '__main__':
    unittest.main()
