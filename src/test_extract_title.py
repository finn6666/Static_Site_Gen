import unittest
from src.gen_page import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_extract_title_basic(self):
        markdown = "# Hello World"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello World")

    def test_extract_title_multiline(self):
        markdown = """
Some text here.

# My Title

More content.
"""
        result = extract_title(markdown)
        self.assertEqual(result, "My Title")

    def test_extract_title_with_spaces(self):
        markdown = "#   Title with spaces   "
        result = extract_title(markdown)
        self.assertEqual(result, "Title with spaces")

    def test_extract_title_no_heading_raises_exception(self):
        markdown = "No heading here\nJust some text"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title_ignores_h2(self):
        markdown = """
## This is h2

# This is h1
"""
        result = extract_title(markdown)
        self.assertEqual(result, "This is h1")


if __name__ == "__main__":
    unittest.main()