import pygame
import Player

class Inventory(object):
    def __init__(self):
        self.current_slot = 0
        self.slots = [False] * 6
        self.button_use = False
        self.use_text = '* ...'

    def inventory_update(self, keys, prev_keys):
        # Обновление наличия предметов в слотах
        for idx in range(len(self.slots)):
            if idx < len(Player.player.inventory) and Player.player.inventory[idx] is not None:
                self.slots[idx] = True
            else:
                self.slots[idx] = False

        # Перемещение по слотам
        if not self.button_use:
            if keys[pygame.K_UP] and not prev_keys[pygame.K_UP]:
                if self.current_slot > 0:
                    self.current_slot -= 1
            if keys[pygame.K_DOWN] and not prev_keys[pygame.K_DOWN]:
                if self.current_slot < 5:
                    self.current_slot += 1
            if keys[pygame.K_RIGHT] and not prev_keys[pygame.K_RIGHT]:
                if 0 <= self.current_slot <= 2:
                    self.current_slot += 3
            if keys[pygame.K_LEFT] and not prev_keys[pygame.K_LEFT]:
                if 3 <= self.current_slot <= 5:
                    self.current_slot -= 3

        # Использование предмета
        if keys[pygame.K_z] and not prev_keys[pygame.K_z] and not self.button_use:
            self.button_use = True
        elif self.button_use:
            if self.slots[self.current_slot]:
                item = Player.player.inventory[self.current_slot]
                self.use_text = item.usage
                if item.heal != 0:
                    self.slots[self.current_slot] = False
                    Player.player.inventory.pop(self.current_slot)
            self.button_use = False
            Player.player.freeze = False
            Player.player.in_inv = False
            Player.player.textbox = True


main_inventory = Inventory()


