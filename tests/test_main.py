import sys
import unittest
from src.main import hello_world  # Ensure import is at the top

print("Current sys.path:", sys.path)

class TestMain(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
