import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    ''' Test class '''
    def test_emotion_detector(self):
        ''' Test function '''
        self.assertEqual(emotion_detector("I am very happy"), "P+")
        self.assertEqual(emotion_detector("I am happy"), "P")
        self.assertEqual(emotion_detector("My house is green"), "None")
        self.assertEqual(emotion_detector("I am angry"), "N")
        self.assertEqual(emotion_detector("I am really angry"), "N+")

unittest.main()
        