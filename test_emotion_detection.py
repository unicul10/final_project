import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_valid_input(self):
        text = "I love my life"
        result = emotion_detector(text)
        self.assertIsNotNone(result['dominant_emotion'])
        self.assertTrue(all(isinstance(value, float) for value in result.values() if value is not None))

    def test_blank_input(self):
        text = ""
        result = emotion_detector(text)
        self.assertIsNone(result['dominant_emotion'])
        self.assertTrue(all(value is None for value in result.values()))

    def test_specific_emotion(self):
        text = "I am so happy I am doing this"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_error_handling_for_invalid_text(self):
        text = None  # Simulating invalid input
        result = emotion_detector(text)
        self.assertIsNone(result['dominant_emotion'])
        self.assertTrue(all(value is None for value in result.values()))

if __name__ == '__main__':
    unittest.main()
