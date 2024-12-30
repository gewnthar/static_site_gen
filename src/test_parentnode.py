#!/usr/bin/env python3

import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html_basic(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_props(self):
        node = ParentNode(
            "a",
            [LeafNode(None, "Click me!")],
            {"href": "https://www.example.com"}
        )
        self.assertEqual(node.to_html(), '<a href="https://www.example.com">Click me!</a>')

    def test_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode(None, "Some text")])

    def test_missing_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_nested_nodes(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "This is a paragraph."),
                ParentNode("span", [LeafNode("b", "Bold inside span")]),
            ]
        )
        self.assertEqual(node.to_html(), '<div><p>This is a paragraph.</p><span><b>Bold inside span</b></span></div>')

if __name__ == "__main__":
    unittest.main()

