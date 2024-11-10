# core/renderer.py
from typing import Dict, List, Any
from .parser import DOMNode

class Renderer:
    def __init__(self):
        self.style_modifiers: List[callable] = []
        
    def render(self, dom: DOMNode) -> str:
        # Apply style modifiers
        styles = self._generate_styles(dom)
        for modifier in self.style_modifiers:
            styles = modifier(styles)
            
        # Generate HTML with applied styles
        return f"""
        <html>
        <head>
            <style>{styles}</style>
        </head>
        <body>
            {self._render_node(dom)}
        </body>
        </html>
        """
        
    def _render_node(self, node: DOMNode) -> str:
        if node.tag == "text":
            return node.text_content
            
        attrs_str = " ".join([f'{k}="{v}"' for k, v in node.attrs.items()])
        if attrs_str:
            attrs_str = " " + attrs_str
            
        inner_html = "".join(self._render_node(child) for child in node.children)
        return f"<{node.tag}{attrs_str}>{inner_html}</{node.tag}>"
        
    def _generate_styles(self, dom: DOMNode) -> str:
        # Basic styles for better readability
        return """
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }
        a {
            color: #007AFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        """
        
    def register_style_modifier(self, modifier: callable):
        self.style_modifiers.append(modifier)
        
    def unregister_style_modifier(self, modifier: callable):
        if modifier in self.style_modifiers:
            self.style_modifiers.remove(modifier)