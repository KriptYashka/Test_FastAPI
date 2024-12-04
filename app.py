import json
import logging
import os.path

from config import path_to_json
from commands.task import app

def main():
    logging.basicConfig(level=logging.DEBUG)
    if not os.path.exists(path_to_json):
        with open(path_to_json, "w", encoding='utf-8') as f:
            json.dump(dict(), f)
    app()

if __name__ == '__main__':
    main()
