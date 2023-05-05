import unittest
import requests
import pytest
import json


class TestQualityAssuranceAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost:5000/api/"

    def test_get_product_quality(self):
        url = self.base_url + "product_quality"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        product_quality = json.loads(response.content.decode('utf-8'))
        self.assertIsNotNone(product_quality)

    def test_post_defect(self):
        url = self.base_url + "defect"
        data = {'name': 'crack', 'severity': 'high',
                'description': 'A crack was found in the product.'}
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 200)
        defect = json.loads(response.content.decode('utf-8'))
        self.assertEqual(defect['name'], 'crack')
        self.assertEqual(defect['severity'], 'high')


if __name__ == '__main__':
    unittest.main()
