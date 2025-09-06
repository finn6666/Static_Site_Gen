import unittest
from htmlnode import LeafNode, ParentNode, text_node_to_html_node
from src.textnode import TextNode, TextNodeType

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello world!")
        self.assertEqual(node.to_html(), '<p>Hello world!</p>')

    def test_leaf_to_html_img(self):
        node = LeafNode("img", props={"src": "image.png", "alt": "An image"})
        self.assertEqual(node.to_html(), '<img src="image.png" alt="An image" />')

class TestParentNode(unittest.TestCase):
    def test_parent_to_html_div(self):
        child1 = LeafNode("p", "Paragraph 1")
        child2 = LeafNode("p", "Paragraph 2")
        node = ParentNode("div", children=[child1, child2])
        self.assertEqual(node.to_html(), '<div><p>Paragraph 1</p><p>Paragraph 2</p></div>')

    def test_parent_to_html_ul(self):
        li1 = LeafNode("li", "Item 1")
        li2 = LeafNode("li", "Item 2")
        node = ParentNode("ul", children=[li1, li2])
        self.assertEqual(node.to_html(), '<ul><li>Item 1</li><li>Item 2</li></ul>') 
    
    def test_parent_with_props(self):
        child = LeafNode("p", "Content")
        node = ParentNode("div", children=[child], props={"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><p>Content</p></div>')

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


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_plain(self):
        text_node = TextNode("Just some text", TextNodeType.PLAIN)
        html = text_node_to_html_node(text_node)
        self.assertEqual(html, "Just some text")    

    def test_text_node_to_html_bold(self):
        text_node = TextNode("Bold text", TextNodeType.BOLD)
        html = text_node_to_html_node(text_node)
        self.assertEqual(html, "<b>Bold text</b>")      

    def test_text_node_to_html_italic(self):
        text_node = TextNode("Italic text", TextNodeType.ITALIC)
        html = text_node_to_html_node(text_node)
        self.assertEqual(html, "<i>Italic text</i>")      

    def test_text_node_to_html_code(self):
        text_node = TextNode("Code text", TextNodeType.CODE)
        html = text_node_to_html_node(text_node)
        self.assertEqual(html, "<code>Code text</code>")      

    def test_text_node_to_html_link(self):      
        text_node = TextNode("Link text", TextNodeType.LINK, url="http://example.com")
        html = text_node_to_html_node(text_node)
        self.assertEqual(html, '<a href="http://example.com">Link text</a>')    

    def test_text_node_to_html_invalid_type(self):
        class FakeType:
            pass
        text_node = TextNode("Text", FakeType())
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception), "Invalid TextNodeType")
