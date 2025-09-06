import unittest

from textnode import TextNode, TextNodeType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextNodeType.BOLD)
        node2 = TextNode("This is a text node", TextNodeType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node1 = TextNode("Text A", TextNodeType.PLAIN)
        node2 = TextNode("Text B", TextNodeType.PLAIN)
        self.assertNotEqual(node1, node2)

    def test_not_equal_type(self):
        node1 = TextNode("Text", TextNodeType.PLAIN)
        node2 = TextNode("Text", TextNodeType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_url_equality(self):
        node1 = TextNode("Text", TextNodeType.LINK, url="http://a.com")
        node2 = TextNode("Text", TextNodeType.LINK, url="http://a.com")
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Text", TextNodeType.PLAIN)
        self.assertEqual(repr(node), "TextNode(text=Text, type=TextNodeType.PLAIN, url=None)")

    def test_not_equal_non_textnode(self):
        node = TextNode("Text", TextNodeType.PLAIN)
        self.assertFalse(node == "Not a TextNode")

if __name__ == "__main__":
    unittest.main()