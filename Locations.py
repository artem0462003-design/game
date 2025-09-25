import pygame
import textbox_settings
import Player
from resource_path import resource_path
import Choice
import NPC
pygame.init()

lc0 = [pygame.image.load(resource_path('pics/home.png')), pygame.image.load(resource_path('pics/home1.png')), pygame.image.load(resource_path('pics/home0.png'))]
lc1 = [pygame.image.load(resource_path('pics/lc1_0.png')), pygame.image.load(resource_path('pics/lc1_1.png'))]
lc2 = []
locations = []
current_lc = 0

lc_x = [[0, 1024], [0, -768]]

lc00_rect = pygame.Rect(225, 206, 545, 349)
lc01_rect = pygame.Rect(lc00_rect.right, 245, 630, 164)
lc02_rect = pygame.Rect(1260, 245, 100, 1)

lc10_rect = pygame.Rect(460, 750, 100, 4)
lc11_rect = pygame.Rect(215, -680, 578, 1408)
lc12_rect = pygame.Rect(369, 729, 278, 23)
lc13_rect = pygame.Rect(380, -680, 250, 50)
lc_cutscene_rect = pygame.Rect(0, -250, 1024, 2)

cutscenes = [True, True, True]
cutscene_pause = 0
cutscene_dialog = 0

lc_anim = 0
alpha = 255
light = False


def cutscene_room_1(player, npc, keys, prev_keys, surface):
    global cutscene_pause, cutscene_dialog
    if cutscenes[0]:
        player.freeze = True
        if cutscene_pause < 30:
            cutscene_pause += 1
        if cutscene_pause == 30:
            if lc_x[1][1] < 0:
                player.y += 6
                for i in range(len(lc_x[1])):
                    lc_x[1][i] += 6
                lc10_rect.y += 6
                lc11_rect.y += 6
                lc12_rect.y += 6
                lc13_rect.y += 6
                lc_cutscene_rect.y += 6
            else:
                cutscene_pause += 1
        if 31 <= cutscene_pause < 61:
            cutscene_pause += 6
        if cutscene_pause == 61:
            player.textbox = True
            textbox_settings.textbox_num = 1
            textbox_settings.text_full = NPC.tim_dlg[cutscene_dialog]
            if keys[pygame.K_z] and not prev_keys[pygame.K_z] and cutscene_dialog < len(npc.dialog) - 1:
                textbox_settings.current_text = ""
                textbox_settings.char_index = 0
                cutscene_dialog += 1
            if textbox_settings.current_text == textbox_settings.text_full and cutscene_dialog == len(npc.dialog) - 1 and not Choice.choice_end:
                Player.player.in_choice = True
                Choice.current_choice_count = 2
                Choice.current_choice_options = ['Том', 'Я хз']
            if Choice.choice_end:
                textbox_settings.textbox_num = 0
                player.textbox = False
                Choice.chouce_end = False
                cutscene_pause = 62
        if cutscene_pause == 62:
            if player.rect.y > player.playertrigger_u.y:
                player.y -= 6
                for i in range(len(lc_x[1])):
                    lc_x[1][i] -= 6
                lc10_rect.y -= 6
                lc11_rect.y -= 6
                lc12_rect.y -= 6
                lc13_rect.y -= 6
                lc_cutscene_rect.y -= 6
            else:
                cutscenes[0] = False
                player.freeze = False
                cutscene_pause = 0
                cutscene_dialog = 0


def location_0(surface, player, tp):
    global lc_anim, alpha, light, current_lc
    if lc_anim != 200:
        lc_anim += 5
    else:
        lc_anim = 0
    if 100 >= lc_anim >= 0:
        surface.blit(lc0[0], (lc_x[0][0], 0))
    else:
        surface.blit(lc0[2], (lc_x[0][0], 0))
    surface.blit(lc0[1], (lc_x[0][1], 0))
    if player.rect.colliderect(lc02_rect) and player.up:
        player.tp = True
        player.freeze = True
    if player.tp and alpha > 0 and not light:
        alpha -= 25
    elif alpha <= 0 and not light:
        light = True
        current_lc = 1
        player.x = 480
        player.y = 670
        player.up_facing = True
        player.left_facing = False
        player.right_facing = False
    if light and player.tp and alpha < 255:
        alpha += 25
    elif alpha >= 255 and player.tp and light:
        player.tp = False
        light = False
        player.freeze = False


def location_1(surface, player, tp):
    global alpha, light, current_lc
    surface.blit(lc1[0], (0, lc_x[1][0]))
    surface.blit(lc1[1], (0, lc_x[1][1]))
    if player.rect.colliderect(lc10_rect) and player.down:
        player.tp = True
        player.freeze = True
    if player.tp and alpha > 0 and not light:
        alpha -= 25
    elif alpha <= 0 and not light:
        light = True
        current_lc = 0
        player.x = 480
        player.y = 270
        player.down_facing = True
        player.left_facing = False
        player.right_facing = False
    if light and player.tp and alpha < 255:
        alpha += 25
    elif alpha >= 255 and player.tp and light:
        player.tp = False
        light = False
        player.freeze = False


def move_right(objects, obstacles, player):
    global current_lc
    if current_lc == 0:
        if lc_x[0][1] > 224:
            player.x = player.playertrigger_r.x - player.rect.width - 4
            for i in range(len(lc_x[0])):
                lc_x[0][i] -= 6
            lc00_rect.x -= 6
            lc01_rect.x -= 6
            lc02_rect.x -= 6
            for obj in objects:
                obj.x -= 6
            for o in obstacles:
                o.x -= 6


def move_left(objects, obstacles, player):
    global current_lc
    if current_lc == 0:
        if lc_x[0][0] < 0:
            player.x = player.playertrigger_l.right + 4
            for i in range(len(lc_x[0])):
                lc_x[0][i] += 6
            lc00_rect.x += 6
            lc01_rect.x += 6
            lc02_rect.x += 6
            for obj in objects:
                obj.x += 6
            for o in obstacles:
                o.x += 6


def move_up(objects, obstacles, player):
    global current_lc
    if current_lc == 1:
        if lc_x[1][1] < 0:
            player.y = player.playertrigger_u.y
            for i in range(len(lc_x[1])):
                lc_x[1][i] += 6
            lc10_rect.y += 6
            lc11_rect.y += 6
            lc12_rect.y += 6
            lc13_rect.y += 6
            lc_cutscene_rect.y += 6


def move_down(objects, obstacles, player):
    global current_lc
    if current_lc == 1:
        if lc_x[1][0] > 0:
            player.y = player.playertrigger_d.y - player.rect.height
            for i in range(len(lc_x[1])):
                lc_x[1][i] -= 6
            lc10_rect.y -= 6
            lc11_rect.y -= 6
            lc12_rect.y -= 6
            lc13_rect.y -= 6
            lc_cutscene_rect.y -= 6


def trigger_camera(player, objects, obstacles):
    if player.rect.colliderect(player.playertrigger_r):
        if player.right:
            move_right(objects, obstacles, player)
    if player.rect.colliderect(player.playertrigger_l):
        if player.left:
            move_left(objects, obstacles, player)
    if player.rect.colliderect(player.playertrigger_u):
        if player.up:
            move_up(objects, obstacles, player)
    if player.rect.colliderect(player.playertrigger_d):
        if player.down:
            move_down(objects, obstacles, player)
