import pygame
from settings import *

alpha = 0
light = False
count = 0
intro_0 = pygame.image.load(INTRO_0)
intro_1 = pygame.image.load(INTRO_1)
intro_2 = pygame.image.load(INTRO_2)
intro_3 = pygame.image.load(INTRO_3)
intro_4 = pygame.image.load(INTRO_4)

menu = pygame.image.load(MAIN_MENU)
play_button_0 = pygame.image.load(PLAY_BUTTON_0)
play_button_1 = pygame.image.load(PLAY_BUTTON_1)
settings_button_0 = pygame.image.load(SETTINGS_BUTTON_0)
settings_button_1 = pygame.image.load(SETTINGS_BUTTON_1)
settings_screen = pygame.image.load(SETTINGS_SCREEN)

intro_spec = True
menu_spec = False
play_button = True
settings_button = False
in_settings = False

def main_intro(surface):
    global intro_spec, alpha, count, menu_spec
    if count < 51:
        surface.blit(intro_0, (0, 0))
        if alpha < 255 and count < 50:
            alpha += 5
        elif count < 50:
            count += 1
    if count == 50:
        alpha -= 5
        if alpha <= 0:
            count = 51
    if 100 > count >= 51:
        surface.blit(intro_1, (0, 0))
        if alpha < 255 and count < 100:
            alpha += 5
        elif count < 100:
            count += 1
    if count == 100:
        alpha -= 5
        if alpha <= 0:
            count = 101
    if 150 > count >= 101:
        surface.blit(intro_2, (0, 0))
        if alpha < 255 and count < 150:
            alpha += 5
        elif count < 150:
            count += 1
    if count == 150:
        alpha -= 5
        if alpha <= 0:
            count = 151
    if 200 > count >= 151:
        surface.blit(intro_3, (0, 0))
        if alpha < 255 and count < 200:
            alpha += 5
        elif count < 200:
            count += 1
    if count == 200:
        alpha -= 5
        if alpha <= 0:
            count = 201
    if 250 > count >= 201:
        surface.blit(intro_4, (0, 0))
        if alpha < 255 and count < 250:
            alpha += 5
        elif count < 250:
            count += 1
    if count == 250:
        alpha -= 5
        if alpha <= 0:
            intro_spec = False
            menu_spec = True
            count = 0


def main_menu(surface, keys, prev_keys):
    global menu_spec, alpha, in_settings, play_button, settings_button, count
    if count == 1:
        if alpha > 0:
            alpha -= 5
            if alpha == 0:
                menu_spec = False
    else:
        if alpha <= 255 and count == 0:
            alpha += 5
        if not in_settings:
            surface.blit(menu, (0, 0))
            if play_button:
                surface.blit(play_button_1, (57, 261))
                surface.blit(settings_button_0, (57, 380))
            else:
                surface.blit(play_button_0, (57, 261))
                surface.blit(settings_button_1, (57, 380))
            if keys[pygame.K_DOWN] and not prev_keys[pygame.K_DOWN]:
                if not settings_button:
                    settings_button = True
                    play_button = False
            if keys[pygame.K_UP] and not prev_keys[pygame.K_UP]:
                if not play_button:
                    settings_button = False
                    play_button = True
            if keys[pygame.K_z] and not prev_keys[pygame.K_z]:
                if play_button:
                    count = 1
                if settings_button:
                    in_settings = True
        else:
            surface.blit(settings_screen, (0, 0))
            if keys[pygame.K_x] and not prev_keys[pygame.K_x]:
                in_settings = False









