import pygame
import random
from Player import *
from Objects import *
import Locations
from Items import *
from Inventory import *
from settings import *
import textbox_settings
import NPC
import intro
import Choice

pygame.init()
background = pygame.image.load(BACKGROUND_PATH)
clock = pygame.time.Clock()

point = pygame.image.load(POINT)
inventory = pygame.image.load(INVENTORY_BG_PATH)
pygame.display.set_caption("Cranberry Pie")
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)
game_surface = pygame.Surface((ORIGINAL_WIDTH, ORIGINAL_HEIGHT))
screen = pygame.display.set_mode((ORIGINAL_WIDTH, ORIGINAL_HEIGHT))
is_fullscreen = False

textbox = pygame.image.load(TEXTBOX_PATH)
running = True
prev_keys = pygame.key.get_pressed()
while running:

    """___________________________________________________________________________
    Интро
    ___________________________________________________________________________"""

    if intro.intro_spec:
        clock.tick(FPS)
        game_surface.set_alpha(intro.alpha)
        intro.main_intro(game_surface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    is_fullscreen = not is_fullscreen
                    if is_fullscreen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((ORIGINAL_WIDTH, ORIGINAL_HEIGHT))
                if event.key == pygame.K_ESCAPE:
                    intro.alpha = 0
                    intro.count = 0
                    intro.intro_spec = False
                    intro.menu_spec = True

    elif intro.menu_spec:
        clock.tick(FPS)
        game_surface.set_alpha(intro.alpha)
        keys = pygame.key.get_pressed()
        intro.main_menu(game_surface, keys, prev_keys)
        prev_keys = keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    is_fullscreen = not is_fullscreen
                    if is_fullscreen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((ORIGINAL_WIDTH, ORIGINAL_HEIGHT))

    else:

        """___________________________________________________________________________
        Игровой цикл
        ___________________________________________________________________________"""
        clock.tick(60)
        game_surface.set_alpha(Locations.alpha)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    is_fullscreen = not is_fullscreen
                    if is_fullscreen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((ORIGINAL_WIDTH, ORIGINAL_HEIGHT))

                if event.key == pygame.K_z and not player.in_inv and not player.tp and not player.in_choice:
                    if not player.textbox:
                        if player.interact == 1:
                            for obj in objects:
                                if obj.inter == 1:
                                    if obj.cap != 0:
                                        player.inventory.append(obj.item)
                                        obj.cap -= 1
                                        textbox_settings.text_full = obj.desc
                                    else:
                                        textbox_settings.text_full = obj.desc2
                            player.freeze = True
                            player.textbox = True
                    else:
                        if main_inventory.use_text != '* ...':
                            main_inventory.use_text = '* ...'
                        if textbox_settings.textbox_num == 0:
                            player.textbox = False
                            player.freeze = False
                        textbox_settings.text_full = '* ...'
                        textbox_settings.current_text = ''
                        textbox_settings.char_index = 0

                if event.key == pygame.K_c and not player.textbox and not player.tp:
                    if not player.in_inv:
                        main_inventory.current_slot = 0
                        player.freeze = True
                        player.in_inv = True
                    else:
                        player.freeze = False
                        player.in_inv = False

        keys = pygame.key.get_pressed()
        player.update(keys, objects, obstacles)

        if Locations.current_lc == 0:
            Locations.location_0(game_surface, player, player.tp)
            for obj in objects:
                obj.draw(game_surface, obj.source)
            Locations.trigger_camera(player, objects, obstacles)
            player.draw(game_surface)
        elif Locations.current_lc == 1:
            Locations.location_1(game_surface, player, player.tp)
            NPC.tim.draw(game_surface, NPC.tim.sprites[0], 484, 84 + 768)
            Locations.trigger_camera(player, objects, obstacles)
            if player.rect.colliderect(Locations.lc_cutscene_rect):
                Locations.cutscene_pause = 1
            if Locations.cutscene_pause > 0 and Locations.cutscenes[0]:
                Locations.cutscene_room_1(player, NPC.tim, keys, prev_keys, game_surface)
                if not player.in_choice:
                    prev_keys = keys
            player.draw(game_surface)

        if player.in_inv:
            main_inventory.inventory_update(keys, prev_keys)
            prev_keys = keys
            game_surface.blit(inventory, (50, 100))
            game_surface.blit(point, (inventory_coords[main_inventory.current_slot][0] - 19, (inventory_coords[main_inventory.current_slot][1] + 15)))
            game_surface.blit(textbox_settings.mainfont.render(('HP:' + str(player.hp)), True, (255, 255, 255)), (70, 120))
            if len(player.inventory) != 0:
                for item in player.inventory:
                    game_surface.blit(textbox_settings.mainfont.render(item.name, True, (255, 255, 255)),
                                        (inventory_coords[player.inventory.index(item)]))
        print(textbox_settings.text_full)
        print(textbox_settings.current_text)
        if player.textbox:
            player.freeze = True
            game_surface.blit(textbox, (0, 504))
            if main_inventory.use_text != '* ...':
                textbox_settings.text_full = main_inventory.use_text
                main_inventory.use_text = '* ...'
            textbox_settings.text_output(game_surface, textbox_settings.text_full)
            if player.in_choice:
                Choice.choice(Choice.current_choice_count, Choice.current_choice_options, keys, prev_keys, game_surface)
                prev_keys = keys



    # pygame.draw.rect(game_surface, (255, 255, 0), player.rect, 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), player.playertrigger_r, 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), player.playertrigger_l, 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), player.playertrigger_u, 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), player.playertrigger_d, 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), Locations.lc11_rect, 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), Locations.lc13_rect, 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), Locations.lc_cutscene_rect, 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), Locations.lc01_rect, 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), Locations.lc02_rect, 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), obstacles[1], 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), obstacles[3], 2)
    # pygame.draw.rect(game_surface, (255, 0, 0), Locations.lc10_rect, 2)
    screen.fill((0, 0, 0))

    current_screen_width, current_screen_height = screen.get_size()
    aspect_ratio = ORIGINAL_WIDTH / ORIGINAL_HEIGHT
    scale_w = current_screen_width / ORIGINAL_WIDTH
    scale_h = current_screen_height / ORIGINAL_HEIGHT
    scale_factor = min(scale_w, scale_h)
    scaled_width = int(ORIGINAL_WIDTH * scale_factor)
    scaled_height = int(ORIGINAL_HEIGHT * scale_factor)
    scaled_game_surface = pygame.transform.smoothscale(game_surface, (scaled_width, scaled_height))
    offset_x = (current_screen_width - scaled_width) // 2
    offset_y = (current_screen_height - scaled_height) // 2
    screen.blit(scaled_game_surface, (offset_x, offset_y))
    pygame.display.flip()
