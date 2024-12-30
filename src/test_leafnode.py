#!/usr/bin/env python3

import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        # Test with a simple tag
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
        
        # Test with a tag and properties
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

        # Test with no tag, should return the value as raw text
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_value_required(self):
        # Test that ValueError is raised when no value is provided
        with self.assertRaises(ValueError):
            LeafNode("p", "")

if __name__ == "__main__":
    unittest.main()

