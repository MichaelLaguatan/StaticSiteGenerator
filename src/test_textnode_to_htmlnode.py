import unittest

from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        ...
    
    def test_italic(self):
        ...

    def test_code(self):
        ...

    def test_link(self):
        ...

    def test_image(self):
        ...

    def test_unsupported_text_type(self):
        ...
        
if __name__ == "__main__":
    unittest.main()