import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)


    def test_url_presence(self):
    # Same text and text_type, but one has a URL and one doesn't
        node = TextNode("Same text", TextType.LINK, "http://example.com")
        node2 = TextNode("Same text", TextType.LINK)  # url defaults to None
        self.assertNotEqual(node, node2)

    def test_for_None(self):
        node = TextNode("Test text", TextType.LINK)

        self.assertIsNone(node.url)
    

if __name__ == "__main__":
    unittest.main()
