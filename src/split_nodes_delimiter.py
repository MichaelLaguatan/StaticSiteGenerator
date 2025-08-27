from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        texts = node.text.split(delimiter)
        for index, text in enumerate(texts):
            if index % 2 == 0:
                if text: new_nodes.append(TextNode(text, TextType.TEXT))
            else: new_nodes.append(TextNode(text, text_type))
    return new_nodes
        


if __name__ == "__main__":
    node = TextNode("`code block` This is text with a `code block` text", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)