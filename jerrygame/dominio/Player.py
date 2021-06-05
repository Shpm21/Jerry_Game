import pygame
class Player(pygame.sprite.Sprite):  # CLASE PADRE
    def __init__(self, position, imagen):
        super().__init__()
        self.sheet = pygame.image.load(imagen)
        self.sheet.set_clip(pygame.Rect(0, 0, 80, 67))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        # POSICIONES
        self.left_states =  {0: (0, 134, 80, 67), 1: (80, 134, 80, 67), 2: (160, 134, 80, 67), 3: (240, 134, 80, 67),
                             4: (320, 134, 80, 67), 5: (400, 134, 80, 67), 6: (480, 134, 80, 67), 7: (560, 134, 80, 67),
                             8: (480, 134, 80, 67), 9: (400, 134, 80, 67), 10: (320, 134, 80, 67), 11: (240, 134, 80, 67),
                             12: (160, 134, 80, 67), 13: (80, 134, 80, 67)}
        self.right_states = {0: (0, 201, 80, 67), 1: (80, 201, 80, 67), 2: (160, 201, 80, 67), 3: (240, 201, 80, 67),
                             4: (320, 201, 80, 67), 5: (400, 201, 80, 67), 6: (480, 201, 80, 67), 7: (560, 201, 80, 67),
                             8: (480, 201, 80, 67), 9: (400, 201, 80, 67), 10: (320, 201, 80, 67), 11: (240, 201, 80, 67),
                             12: (160, 201, 80, 67), 13: (80, 201, 80, 67)}
        self.up_states =    {0: (0, 67, 80, 67), 1: (80, 67, 80, 67), 2: (160, 67, 80, 67), 3: (240, 67, 80, 67),
                             4: (320, 67, 80, 67), 5: (400, 67, 80, 67), 6: (480, 67, 80, 67), 7: (560, 67, 80, 67),
                             8: (480, 67, 80, 67), 9: (400, 67, 80, 67), 10: (320, 67, 80, 67), 11: (240, 67, 80, 67),
                             12: (160, 67, 80, 67), 13: (80, 67, 80, 67)}
        self.down_states =  {0: (0, 0, 80, 67), 1: (80, 0, 80, 67), 2: (160, 0, 80, 67), 3: (240, 0, 80, 67),
                             4: (320, 0, 80, 67), 5: (400, 0, 80, 67), 6: (480, 0, 80, 67), 7: (560, 0, 80, 67),
                             8: (480, 0, 80, 67), 9: (400, 0, 80, 67), 10: (320, 0, 80, 67), 11: (240, 0, 80, 67),
                             12: (160, 0, 80, 67), 13: (80, 0, 80, 67)}
     # ANIMACION
    def update(self, direction):
        if direction == "left":
            self.clip(self.left_states)
            self.rect.x -= 4
        if direction == "right":
            self.clip(self.right_states)
            self.rect.x += 4
        if direction == "up":
            self.clip(self.up_states)
            self.rect.y -= 4
        if direction == "down":
            self.clip(self.down_states)
            self.rect.y += 4
     # ACA SE CREA EL EFECTO DE TRANSPORTACION POR LOS BORDES DE LA PANTALLA
        # Derecha
        if self.rect.x > 620:
            self.rect.x = -60
        # Izquierda
        if self.rect.x < -60:
            self.rect.x = 620
        # Arriba
        if self.rect.y > 520:
            self.rect.y = -60
        # Abajo
        if self.rect.y < -60:
            self.rect.y = 520
     # ACA SE CREA EL EFECTO DE TRANSPORTACION POR LOS BORDES DE LA PANTALLA
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        return clipped_rect