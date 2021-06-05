import pygame
class Heart(pygame.sprite.Sprite):
    def __init__(self, position, player_life):
        super().__init__()
        self.sheet = pygame.image.load("jerrygame/dominio/spritesdesign/life.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 90, 30))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.life = player_life
        self.movement = {0: (0, 0, 90, 30), 1: (
            30, 0, 90, 30), 2: (60, 0, 90, 30)}

    # Este metodo es el encargado de vaciar/llenar los corazones de Jerry
    def get_frame(self, frame_set):
        if self.frame == 0 and self.life == 200:
            self.frame = 1
        if self.frame == 1 and self.life == 300:
            self.frame = 0
        if self.frame == 1 and self.life == 100:
            self.frame = 2
        if self.frame == 2 and self.life == 200:
            self.frame = 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self,  clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        return clipped_rect

    def update(self, direction):
        if direction == True:
            if self.life <= 300:
                self.clip(self.movement)
        self.image = self.sheet.subsurface(self.sheet.get_clip())