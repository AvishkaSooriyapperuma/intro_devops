import sys
import unittest
from src.main import hello_world  # Absolute import

print("Current sys.path:", sys.path)

from src.main import hello_world

class TestMain(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
