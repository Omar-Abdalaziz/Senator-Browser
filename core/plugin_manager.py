# core/plugin_manager.py
import os
import importlib
import json
from ..plugins.base import BrowserPlugin

class PluginManager:
    def __init__(self, browser_instance):
        self.browser = browser_instance
        self.plugins = {}
        self.plugin_dir = "plugins/default"
        self.enabled_plugins = set()
        
    def load_plugins(self):
        """Load all available plugins"""
        for plugin_file in os.listdir(self.plugin_dir):
            if plugin_file.endswith(".py") and not plugin_file.startswith("__"):
                self._load_plugin(plugin_file)
                
    def _load_plugin(self, plugin_file):
        """Load a single plugin"""
        try:
            module_name = plugin_file[:-3]
            module = importlib.import_module(f"plugins.default.{module_name}")
            
            for item in dir(module):
                item_obj = getattr(module, item)
                if (isinstance(item_obj, type) and 
                    issubclass(item_obj, BrowserPlugin) and 
                    item_obj != BrowserPlugin):
                    plugin = item_obj()
                    self.plugins[plugin.name] = plugin
                    
        except Exception as e:
            print(f"Error loading plugin {plugin_file}: {str(e)}")
            
    def enable_plugin(self, plugin_name):
        """Enable a specific plugin"""
        if plugin_name in self.plugins and plugin_name not in self.enabled_plugins:
            plugin = self.plugins[plugin_name]
            plugin.initialize(self.browser)
            self.enabled_plugins.add(plugin_name)
            
    def disable_plugin(self, plugin_name):
        """Disable a specific plugin"""
        if plugin_name in self.enabled_plugins:
            plugin = self.plugins[plugin_name]
            plugin.cleanup()
            self.enabled_plugins.remove(plugin_name)
