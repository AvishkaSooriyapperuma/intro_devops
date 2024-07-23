# tests/test_main.py

import unittest
from src.main import hello_world  # Use absolute import

class TestMain(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
