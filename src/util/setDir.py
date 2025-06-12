import os
from PyQt6.QtGui import QIcon

def load_icon(filename: str) -> QIcon:
    base_dir = os.path.dirname(os.path.abspath(__file__))  # icon_loader.py 기준
    icon_path = os.path.join(base_dir, "..", "..", "assets", "icons", filename)
    return QIcon(os.path.abspath(icon_path))
