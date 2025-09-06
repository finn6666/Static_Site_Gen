from src.textnode import TextNode, TextNodeType


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self) -> str:
        raise NotImplementedError("Subclasses should implement this method")

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        props_str = ' '.join(f'{key}="{value}"' for key, value in self.props.items())
        return ' ' + props_str

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self) -> str:
        # List of self-closing tags
        self_closing = {"img", "br", "hr", "input", "meta", "link"}
        if not self.tag:
            if self.value is not None:
                return self.value
            raise ValueError("LeafNode must have a tag or value")
        if self.tag in self_closing:
            return f"<{self.tag}{self.props_to_html()} />"
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children=None, props=None):
        super().__init__(tag=tag, value=None, children=children or [], props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

# Needs to be outside class to avoid circular import
def text_node_to_html_node(text_node) -> str:
    if not isinstance(text_node, TextNode):
        raise Exception("Input must be a TextNode")
    if not isinstance(text_node.node_type, TextNodeType):
        raise Exception("Invalid TextNodeType")
    if text_node.node_type == TextNodeType.PLAIN:
        return LeafNode(tag=None, value=text_node.text).to_html()
    elif text_node.node_type == TextNodeType.BOLD:
        return LeafNode(tag="b", value=text_node.text).to_html()
    elif text_node.node_type == TextNodeType.ITALIC:
        return LeafNode(tag="i", value=text_node.text).to_html()
    elif text_node.node_type == TextNodeType.CODE:
        return LeafNode(tag="code", value=text_node.text).to_html()
    elif text_node.node_type == TextNodeType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url}).to_html()
    elif text_node.node_type == TextNodeType.IMAGE:
        return LeafNode(tag="img", props={"src": text_node.url, "alt": text_node.text}).to_html()
    else:
        raise Exception("Unhandled TextNodeType")