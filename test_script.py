import unittest  # Import testing framework
import send_email

class TestCodeStability(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)  # Basic test: check if 1 + 1 equals 2

if __name__ == '__main__':
    unittest.main()  # Run the test
    send_email.check_test_results()
    send_email.send_email()
