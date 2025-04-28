import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):

        node = HTMLNode(
            tag = "a",
            value = "click me",
            children=None,
            props={"href" :"https://www.example.com", "target" : "_blank"}    
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com" target="_blank"')
    
    def test_props_to_html_without_props(self):
        # Test with no properties
        node = HTMLNode(tag="p", value="Hello, world!", children=None, props=None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_empty_props(self):
        # Test with empty properties dictionary
        node = HTMLNode(tag="div", value="", children=None, props={})
        self.assertEqual(node.props_to_html(), "")