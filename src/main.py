from textnode import TextNode, TextNodeType

print("hello, world")

def main():
    text_node1 = TextNode("This is a link", TextNodeType.LINK, "http://example.com")
    print(text_node1)
main()