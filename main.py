#!/usr/bin/env python3

from config import TITLE, WIDTH, HEIGHT, RESIZABLE
from ui.window import Window

if __name__ == '__main__':
    Window(TITLE, WIDTH, HEIGHT, RESIZABLE).render()