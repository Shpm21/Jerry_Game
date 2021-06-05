from jerrygame.dominio.Player import Player
class Enemy(Player):  # ESTA CLASE DERIVA DE LA CLASE "Player"
    def update(self, counter_mov_enemy, state, mov_enemy):
        self.mov_enemy = mov_enemy
        if state == 1:  # Si el contador se encuentra entre 0 y 100 y el state es igual a 1 el personaje se movera de forma diferente al state 2 y 3
            if counter_mov_enemy >= 0 and counter_mov_enemy <= 100:
                self.clip(self.left_states)
                self.rect.x -= self.mov_enemy
            if counter_mov_enemy >= 101 and counter_mov_enemy <= 200:
                self.clip(self.right_states)
                self.rect.x += self.mov_enemy
            if counter_mov_enemy >= 201 and counter_mov_enemy <= 300:
                self.clip(self.up_states)
                self.rect.y -= self.mov_enemy
            if counter_mov_enemy >= 301 and counter_mov_enemy <= 400:
                self.clip(self.down_states)
                self.rect.y += self.mov_enemy
        if state == 2:  # Si el contador se encuentra entre 0 y 100 y el state es igual a 2 el personaje se movera de forma diferente al state 3 y 1
            if counter_mov_enemy >= 0 and counter_mov_enemy <= 100:
                self.clip(self.up_states)
                self.rect.y -= self.mov_enemy
            if counter_mov_enemy >= 101 and counter_mov_enemy <= 200:
                self.clip(self.down_states)
                self.rect.y += self.mov_enemy
            if counter_mov_enemy >= 201 and counter_mov_enemy <= 300:
                self.clip(self.left_states)
                self.rect.x -= self.mov_enemy
            if counter_mov_enemy >= 301 and counter_mov_enemy <= 400:
                self.clip(self.right_states)
                self.rect.x += self.mov_enemy
        if state == 3:  # Si el contador se encuentra entre 0 y 100 y el state es igual a 3 el personaje se movera de forma diferente al state 2 y 1
            if counter_mov_enemy >= 0 and counter_mov_enemy <= 100:
                self.clip(self.down_states)
                self.rect.y += self.mov_enemy
            if counter_mov_enemy >= 101 and counter_mov_enemy <= 200:
                self.clip(self.up_states)
                self.rect.y -= self.mov_enemy
            if counter_mov_enemy >= 201 and counter_mov_enemy <= 300:
                self.clip(self.right_states)
                self.rect.x += self.mov_enemy
            if counter_mov_enemy >= 301 and counter_mov_enemy <= 400:
                self.clip(self.left_states)
                self.rect.x -= self.mov_enemy
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