import os, sys

def resource_path(relative_path: str) -> str:
    """Возвращает путь к ресурсу внутри exe или при запуске из .py"""
    if hasattr(sys, "_MEIPASS"):  # если программа запущена как exe
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)