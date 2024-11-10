# main.py
import sys
import os
from ui.mainwindow import BrowserWindow
from core.engine import BrowserEngine
from utils.config import Config

def main():
    config = Config()
    engine = BrowserEngine(config)
    browser = BrowserWindow(engine)
    browser.run()

if __name__ == "__main__":
    main()