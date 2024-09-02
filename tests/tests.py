import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
import data_scraper
import emotion_detector

class Tests(unittest.TestCase):

    def AssureAPIConnection(self):
        self.assertIsNotNone(data_scraper.reddit.me())

    def AssureModelConnection(self):
        self.assertIsNotNone(emotion_detector.pipeline)

if __name__ == '__main__':
    unittest.main()