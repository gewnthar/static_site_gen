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
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        # If text type is plain text, return a LeafNode with no tag (None).
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.IMAGE and text_node.url:
        # For images, ensure value is either empty string or a valid non-None value
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text}) if text_node.text else LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    elif text_node.text_type == TextType.LINK and text_node.url:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Non-text nodes are added as-is
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

        for i, part in enumerate(parts):
            if part:
                if i % 2 == 0:  # Even index: original text type
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:  # Odd index: new text type
                    new_nodes.append(TextNode(part, text_type))

    return new_nodes
