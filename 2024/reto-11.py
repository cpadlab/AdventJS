
# Reto: https://adventjs.dev/es/challenges/2024/11

import re

def decode_filename(filename: str) -> str:
    match = re.search(r'(\d+_)([\w_-]+\.[a-zA-Z]+)', filename)
    if match:return match.group(2)