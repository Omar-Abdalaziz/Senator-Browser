# utils/cache.py
import os
import json
import time
from typing import Optional, Any
from datetime import datetime, timedelta

class Cache:
    def __init__(self, cache_dir: str = "cache"):
        self.cache_dir = cache_dir
        self.cache: Dict[str, Any] = {}
        self.max_age = timedelta(hours=24)
        self.setup_cache_dir()
        
    def setup_cache_dir(self):
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
            
    def _get_cache_file(self, key: str) -> str:
        # Create a safe filename from the key
        safe_key = "".join(c for c in key if c.isalnum())
        return os.path.join(self.cache_dir, f"{safe_key}.cache")
        
    def get(self, key: str) -> Optional[Any]:
        # Check memory cache first
        if key in self.cache:
            data = self.cache[key]
            if datetime.now() - data["timestamp"] < self.max_age:
                return data["content"]
            else:
                del self.cache[key]
                
        # Check file cache
        cache_file = self._get_cache_file(key)
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    data = json.load(f)
                    if datetime.fromisoformat(data["timestamp"]) + self.max_age > datetime.now():
                        self.cache[key] = {
                            "content": data["content"],
                            "timestamp": datetime.fromisoformat(data["timestamp"])
                        }
                        return data["content"]
                    else:
                        os.remove(cache_file)
            except Exception:
                pass
                
        return None
        
    def set(self, key: str, content: Any):
        # Update memory cache
        self.cache[key] = {
            "content": content,
            "timestamp": datetime.now()
        }
        
        # Update file cache
        cache_file = self._get_cache_file(key)
        try:
            with open(cache_file, 'w') as f:
                json.dump({
                    "content": content,
                    "timestamp": datetime.now().isoformat()
                }, f)
        except Exception as e:
            print(f"Error writing to cache: {str(e)}")
            
    def clear(self):
        self.cache.clear()
        for file in os.listdir(self.cache_dir):
            if file.endswith(".cache"):
                os.remove(os.path.join(self.cache_dir, file))
