# crawler/spider.py
import threading
import queue
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

class WebSpider:
    def __init__(self):
        self.visited_urls = set()
        self.url_queue = queue.Queue()
        self.max_threads = 5
        
    def crawl(self, start_url, max_pages=100):
        self.url_queue.put(start_url)
        threads = []
        
        for _ in range(self.max_threads):
            t = threading.Thread(target=self._worker, args=(max_pages,))
            t.start()
            threads.append(t)
            
        for t in threads:
            t.join()
            
    def _worker(self, max_pages):
        while len(self.visited_urls) < max_pages:
            try:
                url = self.url_queue.get_nowait()
            except queue.Empty:
                break
                
            if url not in self.visited_urls:
                self._process_url(url)
                
    def _process_url(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            self.visited_urls.add(url)
            
            # Extract links
            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    absolute_url = urljoin(url, href)
                    if absolute_url not in self.visited_urls:
                        self.url_queue.put(absolute_url)
                        
        except Exception as e:
            print(f"Error crawling {url}: {str(e)}")