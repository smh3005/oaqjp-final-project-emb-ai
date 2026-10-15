
import unittest
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertIsNotNone(result)
        self.assertIn("anger", result)

    def test_joy(self):
        result = emotion_detector("I am very happy today")
        self.assertIsNotNone(result)
        self.assertIn("joy", result)

    def test_sadness(self):
        result = emotion_detector("I am feeling sad")
        self.assertIsNotNone(result)
        self.assertIn("sadness", result)


if __name__ == "__main__":
    unittest.main()
