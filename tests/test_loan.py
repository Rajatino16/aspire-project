import unittest
import json
from app import app

class LoanTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_create_loan(self):
        response = self.app.post('/loan', json={"amount": 10000, "term": 3, "user_id": 1})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn('loan', data)
        self.assertEqual(data['loan']['amount'], 10000)
        self.assertEqual(data['loan']['term'], 3)

    def test_get_loans(self):
        response = self.app.get('/loans?user_id=1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('loans', data)
        self.assertIsInstance(data['loans'], list)

    def test_add_repayment(self):
        response = self.app.post('/loan', json={"amount": 10000, "term": 3, "user_id": 1})
        response = self.app.post('/repayment/1/0', json={"amount": 3333.33, "user_id": 1})
        data = json.loads(response.data.decode())
        print("test_add_repayment response --> ", response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Repayment added successfully!')

    def test_add_repayment_invalid_amount(self):
        response = self.app.post('/repayment/1/0', json={"amount": 2000, "user_id": 1})
        data = json.loads(response.data.decode())
        print(data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Repayment amount must be greater than or equal to the scheduled repayment.')

    def test_add_repayment_invalid_user(self):
        response = self.app.post('/repayment/1/0', json={"amount": 3333.33, "user_id": 2})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Loan not found or does not belong to the user.')

if __name__ == '__main__':
    unittest.main()
