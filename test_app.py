import unittest

from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.testing = True

    def test_app(self):
        reg = self.app.get("/",)
        self.assertEqual(reg.status_code, 200)

if __name__ == "__main__":
    unittest.main()