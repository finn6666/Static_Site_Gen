from enum import Enum

class TextNodeType(Enum):
    PLAIN = 'plain'
    BOLD = '**text**'
    ITALIC = '*text*'
    CODE = '`code`'
    LINK = '[link](http://example.com)'
    IMAGE = '![alt text](http://example.com/image.png)'

class TextNode:
    def __init__(self, text: str, text_type: TextNodeType, url: str = None):
        self.text = text
        self.node_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.node_type == other.node_type and
                self.url == other.url)

    def __repr__(self):
        return f"TextNode(text={self.text}, type={self.node_type}, url={self.url})"
