import unittest 

from src.split_delim import split_nodes_delimiter
from src.textnode import TextNode, TextNodeType
from htmlnode import LeafNode, ParentNode, text_node_to_html_node

class TestSplitDelim(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        nodes = [
            TextNode("Hello `code` world", TextNodeType.PLAIN),
            TextNode("Bold", TextNodeType.BOLD),
            LeafNode("p", "Paragraph"),
            TextNode("! `again`", TextNodeType.PLAIN)
        ]
        delimiter = "`"
        result = split_nodes_delimiter(nodes, delimiter, TextNodeType.CODE)
        expected = [
            TextNode("Hello ", TextNodeType.PLAIN),
            TextNode("code", TextNodeType.CODE),
            TextNode(" world", TextNodeType.PLAIN),
            TextNode("Bold", TextNodeType.BOLD),
            LeafNode("p", "Paragraph"),
            TextNode("! ", TextNodeType.PLAIN),
            TextNode("again", TextNodeType.CODE)
        ]
        self.assertEqual(result, expected)
