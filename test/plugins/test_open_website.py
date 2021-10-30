import unittest
from unittest.mock import MagicMock, patch

import sys
sys.path.append('../plugins')
import open_website

class TestOpenWebsite(unittest.TestCase):

    @patch('webbrowser.open')
    def test_link1(self, open):
        open_website.run(1, {'link': 'https://test.com'})
        open.assert_called_with('https://test.com')

