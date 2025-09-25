import textbox_settings
import Player
import pygame

choice_current_text_1 = ""
choice_text_full_1 = ""
choice_char_index_1 = 0
choice_frame_counter_1 = 0

choice_current_text_2 = ""
choice_text_full_2 = ""
choice_char_index_2 = 0
choice_frame_counter_2 = 0

current_choice_count = 1
current_choice_options = []

final_answer = 0
current_choice = 0

choice_end = False

def choice(count, options, keys, prev_keys, surface):
    global choice_current_text_1, choice_char_index_1, choice_frame_counter_1, \
        choice_current_text_2, choice_char_index_2, choice_frame_counter_2, final_answer, \
        current_choice, choice_end
    if count == 1:
        if choice_char_index_1 < len(options[0]):
            choice_frame_counter_1 += 1
            if choice_frame_counter_1 >= 1:
                choice_current_text_1 += options[0][choice_char_index_1]
                choice_char_index_1 += 1
                choice_frame_counter_1 = 0
        surface.blit(textbox_settings.mainfont.render(choice_current_text_1, True, (255, 255, 255)), (512 - len(options[0]) * 16, 634))
        if choice_current_text_1 == options[0]:
            surface.blit(textbox_settings.mainfont.render(choice_current_text_1, True, (255, 255, 0)),
                         (512 - len(options[0]) * 16, 634))
            if keys[pygame.K_z] and not prev_keys[pygame.K_z]:
                final_answer = 0
                Player.player.in_choice = False
                choice_end = True

    if count == 2:
        if choice_char_index_1 < len(options[0]):
            choice_frame_counter_1 += 1
            if choice_frame_counter_1 >= 1:
                choice_current_text_1 += options[0][choice_char_index_1]
                choice_char_index_1 += 1
                choice_frame_counter_1 = 0
        elif choice_char_index_2 < len(options[1]):
            choice_frame_counter_2 += 1
            if choice_frame_counter_2 >= 1:
                choice_current_text_2 += options[1][choice_char_index_2]
                choice_char_index_2 += 1
                choice_frame_counter_2 = 0
        surface.blit(textbox_settings.mainfont.render(choice_current_text_1, True, (255, 255, 255)),
                     (512 - len(options[0]) * 16 - 200, 634))
        surface.blit(textbox_settings.mainfont.render(choice_current_text_2, True, (255, 255, 255)), (512 + 200, 634))
        if keys[pygame.K_LEFT] and not prev_keys[pygame.K_LEFT] and current_choice == 1:
            current_choice = 0
        if keys[pygame.K_RIGHT] and not prev_keys[pygame.K_RIGHT] and current_choice == 0:
            current_choice = 1
        if current_choice == 0 and choice_current_text_1 == options[0]:
            surface.blit(textbox_settings.mainfont.render(choice_current_text_1, True, (255, 255, 0)),
                         (512 - len(options[0]) * 16 - 200, 634))
        if current_choice == 1 and choice_current_text_2 == options[1]:
            surface.blit(textbox_settings.mainfont.render(choice_current_text_2, True, (255, 255, 0)),
                         (512 + 200, 634))
        if keys[pygame.K_z] and not prev_keys[pygame.K_z]:
            if current_choice == 0:
                final_answer = 0
            if current_choice == 1:
                final_answer = 1
            Player.player.in_choice = False
            choice_end = True
            textbox_settings.text_full = '* ...'
            textbox_settings.current_text = ''
            textbox_settings.char_index = 0