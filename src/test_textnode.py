import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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
    
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
    
    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://example.com"})
        self.assertEqual(html_node.value, "This is a link node")
    
    def test_image(self):
        url = "https://example.com"
        node = TextNode("This is a image node", TextType.IMAGE, url)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img") 
        self.assertEqual(html_node.props, {"src": url, "alt": "This is a image node"})
        self.assertEqual(html_node.value, "")

   
if __name__ == "__main__":
    unittest.main()
