import pygame
class Screw(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.sheet = pygame.image.load("jerrygame/dominio/spritesdesign/screw.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 42, 42))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        # MOVIMIENTOS
        self.movement = {0: (0, 0, 42, 42), 1: (0, 42, 42, 42), 2: (0, 84, 42, 42),
                         3: (42, 0, 42, 42), 4: (42, 42, 42, 42), 5: (42, 84, 42, 42),
                         6: (84, 0, 42, 42), 7: (84, 42, 42, 42)}

    # Este metodo es el encargado de hacer que la bolsa se sacuda sin parar
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self,  clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        return clipped_rect

    def update(self, direction):
        if direction == True:
            self.clip(self.movement)
        self.image = self.sheet.subsurface(self.sheet.get_clip())