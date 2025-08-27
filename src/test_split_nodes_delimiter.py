import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_split_nodes_with_middle_code_block(self):
        node = TextNode("This is text with a `code block` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode('This is text with a ', TextType.TEXT),
            TextNode('code block', TextType.CODE),
            TextNode(' text', TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_with_beginning_bold_text(self):
        node = TextNode("**This is bold text** at the beginning of regular text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode('This is bold text', TextType.BOLD),
            TextNode(' at the beginning of regular text', TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_with_multiple_inline_text(self):
        node = TextNode("**This is bold text** and _this is italic text_", TextType.TEXT)
        first_split = split_nodes_delimiter([node], "**", TextType.BOLD)
        second_split = split_nodes_delimiter(first_split, '_', TextType.ITALIC)
        expected_nodes = [
            TextNode("This is bold text", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("this is italic text", TextType.ITALIC)
        ]
        self.assertEqual(second_split, expected_nodes)

    def test_split_nodes_with_multiple_nodes(self):
        first_node = TextNode("This is text with a `code block` text", TextType.TEXT)
        second_node = TextNode("`This is a code block` at the beginning of regular text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([first_node, second_node], '`', TextType.CODE)
        expected_nodes = [
            TextNode('This is text with a ', TextType.TEXT),
            TextNode('code block', TextType.CODE),
            TextNode(' text', TextType.TEXT),
            TextNode('This is bold text', TextType.BOLD),
            TextNode(' at the beginning of regular text', TextType.TEXT)
        ]
    
if __name__ == "__main__":
    unittest.main()