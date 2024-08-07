import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.tests = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

    def test_emotion_detection(self):
        for text, expected_emotion in self.tests.items():
            with self.subTest(text=text):
                result = emotion_detector(text)
                self.assertEqual(result['dominant_emotion'], expected_emotion)

if __name__ == "__main__":
    unittest.main()
