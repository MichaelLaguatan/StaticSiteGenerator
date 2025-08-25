class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None or self.props == {}: return ""
        pairs = [f'{attribute}="{value}"' for attribute, value in self.props.items()]
        return f' {" ".join(pairs)}'
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None: raise ValueError("Leaf Node must contain a value")
        if self.tag == None or self.tag == "": return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None or self.tag == "": raise ValueError("Parent Node must contain a tag")
        if self.children == None or self.children == []: raise ValueError("Parent Node must contain children")
        children_html = [html.to_html() for html in self.children]
        return f'<{self.tag}{self.props_to_html()}>{"".join(children_html)}</{self.tag}>'
