# core/parser.py
from html.parser import HTMLParser
from typing import List, Dict, Optional
import re

class DOMNode:
    def __init__(self, tag: str, attrs: Dict[str, str] = None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children: List[DOMNode] = []
        self.parent: Optional[DOMNode] = None
        self.text_content = ""
        
    def add_child(self, child: 'DOMNode'):
        child.parent = self
        self.children.append(child)
        
    def to_html(self) -> str:
        attrs_str = " ".join([f'{k}="{v}"' for k, v in self.attrs.items()])
        if attrs_str:
            attrs_str = " " + attrs_str
            
        if self.tag == "text":
            return self.text_content
            
        inner_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{attrs_str}>{inner_html}</{self.tag}>"

class CustomHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = DOMNode("html")
        self.current_node = self.root
        
    def handle_starttag(self, tag: str, attrs: List[tuple]):
        attrs_dict = dict(attrs)
        new_node = DOMNode(tag, attrs_dict)
        self.current_node.add_child(new_node)
        self.current_node = new_node
        
    def handle_endtag(self, tag: str):
        if self.current_node.parent:
            self.current_node = self.current_node.parent
            
    def handle_data(self, data: str):
        if data.strip():
            text_node = DOMNode("text")
            text_node.text_content = data
            self.current_node.add_child(text_node)

class Parser:
    def __init__(self):
        self.html_parser = CustomHTMLParser()
        
    def parse(self, content: str) -> DOMNode:
        self.html_parser.__init__()  # Reset parser
        self.html_parser.feed(content)
        return self.html_parser.root
        
    def parse_css(self, css_content: str) -> List[Dict[str, Any]]:
        # Basic CSS parser
        rules = []
        # Remove comments
        css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
        
        # Split into rules
        for rule in re.findall(r'([^{]+){([^}]+)}', css_content):
            selector = rule[0].strip()
            styles = {}
            
            # Parse declarations
            for declaration in rule[1].split(';'):
                declaration = declaration.strip()
                if ':' in declaration:
                    property_, value = declaration.split(':', 1)
                    styles[property_.strip()] = value.strip()
                    
            rules.append({
                'selector': selector,
                'styles': styles
            })
            
        return rules
