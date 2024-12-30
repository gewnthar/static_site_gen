#!/usr/bin/env python3

import unittest
from textnode import TextNode, TextType
from htmlnode import text_node_to_html_node, LeafNode


class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text_node_to_html_node_text(self):
        text_node = TextNode("Some text", TextType.PLAIN)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Some text")
    
    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")
    
    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")
    
    def test_text_node_to_html_node_code(self):
        text_node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")
    
    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Google", TextType.LINK, url="https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">Google</a>')
    
    def test_text_node_to_html_node_image(self):
        text_node = TextNode("Image alt text", TextType.IMAGE, url="https://www.example.com/image.jpg")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.example.com/image.jpg" alt="Image alt text">')
    

if __name__ == "__main__":
    unittest.main()

