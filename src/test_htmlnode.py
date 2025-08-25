import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_none_props_to_html(self):
        node = HTMLNode("p", "text", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_empty_dict_props_to_html(self):
        node = HTMLNode("p", "text", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_filled_props_to_html(self):
        node = HTMLNode("p", "text", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

class TestLeafNode(unittest.TestCase):
    def test_none_value(self):
        node = LeafNode("p", None, None)
        self.assertRaises(ValueError, node.to_html)
    
    def test_none_tag(self):
        node = LeafNode(None, "raw text", None)
        self.assertEqual(node.to_html(), "raw text")
    
    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_empty_tag(self):
        parent_node = ParentNode("", [])
        self.assertRaises(ValueError, parent_node.to_html)
        
    
    def test_to_html_with_none_tag(self):
        parent_node = ParentNode(None, [])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        self.assertRaises(ValueError, parent_node.to_html)
    
    def test_to_html_with_none_children(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_children_and_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        child_node_2 = LeafNode("div", "leaf child", {"href": "https://www.google.com"})
        parent_node = ParentNode("div", [child_node, child_node_2])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b>grandchild</b></span><div href="https://www.google.com">leaf child</div></div>'
        )

if __name__ == "__main__":
    unittest.main()