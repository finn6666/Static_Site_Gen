import unittest
from src.textnode import TextNode, TextNodeType
from src.split_img_and_links import split_nodes_img, split_nodes_link


class TestSplitNodesImg(unittest.TestCase):

    def test_split_images_multiple(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextNodeType.PLAIN,
        )
        new_nodes = split_nodes_img([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNodeType.PLAIN),
                TextNode("image", TextNodeType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextNodeType.PLAIN),
                TextNode("second image", TextNodeType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode("This is text with no images", TextNodeType.PLAIN)
        new_nodes = split_nodes_img([node])
        self.assertListEqual([node], new_nodes)

    def test_split_images_only_image(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextNodeType.PLAIN)
        new_nodes = split_nodes_img([node])
        self.assertListEqual(
            [TextNode("image", TextNodeType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")],
            new_nodes,
        )

    def test_split_images_non_plain_node(self):
        node = TextNode("This is ![image](https://i.imgur.com/zjjcJKZ.png)", TextNodeType.BOLD)
        new_nodes = split_nodes_img([node])
        self.assertListEqual([node], new_nodes)


class TestSplitNodesLink(unittest.TestCase):

    def test_split_links_multiple(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)",
            TextNodeType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNodeType.PLAIN),
                TextNode("link", TextNodeType.LINK, "https://boot.dev"),
                TextNode(" and ", TextNodeType.PLAIN),
                TextNode("another link", TextNodeType.LINK, "https://blog.boot.dev"),
            ],
            new_nodes,
        )

    def test_split_links_no_links(self):
        node = TextNode("This is text with no links", TextNodeType.PLAIN)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_links_only_link(self):
        node = TextNode("[link](https://boot.dev)", TextNodeType.PLAIN)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("link", TextNodeType.LINK, "https://boot.dev")],
            new_nodes,
        )

    def test_split_links_non_plain_node(self):
        node = TextNode("This is [link](https://boot.dev)", TextNodeType.BOLD)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)


if __name__ == "__main__":
    unittest.main()