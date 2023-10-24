import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, BOOST_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER, RUNNING_BOOST, JUMPING_BOOST, DUCKING_BOOST

X_POS = 80
Y_POS = 330
Y_POS_DUCK = 350
JUMP_VEL = 8.5

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, BOOST_TYPE : DUCKING_BOOST}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, BOOST_TYPE : JUMPING_BOOST}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, BOOST_TYPE : RUNNING_BOOST}


class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.index = 0
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_sprite_index = 0
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.power_up_time = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False 
        elif not self.dino_duck and not self.dino_jump:
            self.dino_run = True
            self.dino_jump = False 
            self.dino_duck = False

        if self.step_index >= 9:
            self.step_index = 0

    def run(self):
        if self.dino_run:
            sprite_index = (self.index // 2) % 8
            self.image = RUN_IMG[self.type][sprite_index]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_POS
            self.index += 1

    def jump(self):
        if self.dino_jump:
            if self.jump_vel > 0:
                sprite_index = self.jump_sprite_index
            else:
                sprite_index = self.jump_sprite_index + 2

            self.image = JUMP_IMG[self.type][sprite_index]
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

            if self.jump_vel < -JUMP_VEL:
                self.dino_rect.y = Y_POS
                self.dino_jump = False
                self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1
        self.dino_duck = False

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))