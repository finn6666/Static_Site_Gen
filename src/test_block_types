import unittest
from src.block_types import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):

    def test_paragraph(self):
        block = "This is a normal paragraph of text."
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_paragraph_multiline(self):
        block = "This is a paragraph\nwith multiple lines\nof text."
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_heading_h1(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.heading)

    def test_heading_h6(self):
        block = "###### This is an h6"
        self.assertEqual(block_to_block_type(block), BlockType.heading)

    def test_heading_invalid_no_space(self):
        block = "#This is not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_heading_invalid_too_many_hashes(self):
        block = "####### This is not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_code_block(self):
        block = "```\nprint('hello world')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.code)

    def test_code_block_single_line(self):
        block = "```code```"
        self.assertEqual(block_to_block_type(block), BlockType.code)

    def test_code_block_invalid_no_closing(self):
        block = "```\nprint('hello world')"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_quote_single_line(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.quote)

    def test_quote_multiline(self):
        block = "> This is a quote\n> with multiple lines\n> of text"
        self.assertEqual(block_to_block_type(block), BlockType.quote)

    def test_quote_invalid_missing_gt(self):
        block = "> This is a quote\nThis line doesn't start with >"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_unordered_list_dash(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.unordered_list)

    def test_unordered_list_asterisk(self):
        block = "* Item 1\n* Item 2\n* Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.unordered_list)

    def test_unordered_list_plus(self):
        block = "+ Item 1\n+ Item 2\n+ Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.unordered_list)

    def test_unordered_list_invalid_no_space(self):
        block = "-Item 1\n-Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_unordered_list_invalid_mixed(self):
        block = "- Item 1\n* Item 2\n+ Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_ordered_list_valid(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.ordered_list)

    def test_ordered_list_single_item(self):
        block = "1. Single item"
        self.assertEqual(block_to_block_type(block), BlockType.ordered_list)

    def test_ordered_list_invalid_wrong_start(self):
        block = "2. Item 1\n3. Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_ordered_list_invalid_skip_number(self):
        block = "1. Item 1\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_ordered_list_invalid_no_space(self):
        block = "1.Item 1\n2.Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_ordered_list_invalid_no_period(self):
        block = "1 Item 1\n2 Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)


if __name__ == "__main__":
    unittest.main()