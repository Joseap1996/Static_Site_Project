from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url
	def __eq__(self, other):
		if isinstance(other, TextNode):
			return (
			self.text == other.text and
			self.text_type == other.text_type and
			self.url == other.url
			)
		return False

	def __repr__(self):
	    return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None,text_node.text, None)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b",text_node.text, None)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, None)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, None)
    elif text_node.text_type == TextType.LINK:
        props = {"href": text_node.url}
        return LeafNode("a", text_node.text, props)
    elif text_node.text_type == TextType.IMAGE:
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode("img","", props)
    else:
        raise Exception(f"Invalid text type: {text_node.text_type}")

