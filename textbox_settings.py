import pygame
pygame.init()
from pygame import font
from settings import *
current_text = ""
text_full = "* ..."
char_index = 0
frame_counter = 0
mainfont = font.Font(FONT_PATH, 48)
max_chars_in_line = 40  # сколько символов в строке (можно настроить)
line_height = mainfont.get_height() + 5  # расстояние между строками

textbox_num = 0


def text_output(surface, text_full):
    global max_chars_in_line, line_height, mainfont, current_text, char_index, frame_counter
    if char_index < len(text_full):
        frame_counter += 1
        if frame_counter >= 1:
            current_text += text_full[char_index]
            char_index += 1
            frame_counter = 0
    lines = []
    words = current_text.split(" ")
    current_line = ""
    space = 0
    for word in words:
        if len(current_line + word) <= max_chars_in_line:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())

    for i, line in enumerate(lines):
        if lines.index(line) > 0:
            surface.blit(mainfont.render(line, True, (255, 255, 255)), (95, 534 + i * line_height))
        else:
            surface.blit(mainfont.render(line, True, (255, 255, 255)), (50, 534 + i * line_height))