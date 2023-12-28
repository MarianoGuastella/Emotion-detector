"""
Tests for the emotion_detection module.
"""
import unittest
from emotion_detection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    ''' Test class '''
    def test_emotion_detector(self):
        ''' Test function '''
        self.assertEqual(emotion_detector("I am very happy").get('score_tag', ''), "P+")
        self.assertEqual(emotion_detector("I am happy").get('score_tag', ''), "P")
        self.assertEqual(emotion_detector("My house is green").get('score_tag', ''), "NONE")
        self.assertEqual(emotion_detector("I am angry").get('score_tag', ''), "N")
        self.assertEqual(emotion_detector("I am really angry").get('score_tag', ''), "N+")

if __name__ == '__main__':
    unittest.main()
