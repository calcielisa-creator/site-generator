class HTMLNode:
    def __init__(self, tag = None, value= None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        result = ""
        if self.props is None or self.props == {}:
            return result
        for key, prop in self.props.items():
            result += f' {key}="{prop}"'
        return result

    def __repr__(self):
        return f"HTMLNode({self})"