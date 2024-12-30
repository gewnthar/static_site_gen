#!/usr/bin/env python3
from textnode import TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")

    def props_to_html(self):
        return ' ' + ' '.join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children},  props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if not value and tag != "img":  # If no value is provided, raise ValueError
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if not self.value and self.tag != "img":  # Allow empty value for img tags
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value
    
        props_str = self.props_to_html() if self.props else ""
    
        if self.tag == "img":
            return f"<{self.tag}{props_str}>"
        
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("A tag is required")
        if not children:
            raise ValueError("Children are required")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        # Initialize the HTML string with the opening tag
        html = f"<{self.tag}"

        # Add the properties as HTML attributes (if any)
        if self.props:
            html += self.props_to_html()

        # Add the closing '>'
        html += ">"

        # Recursively call to_html on each child and append it to the html
        for child in self.children:
            html += child.to_html()

        # Close the tag
        html += f"</{self.tag}>"

        return html

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.PLAIN:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")

