import pygame
import random
import time
from jerrygame.dominio import*
pygame.init()
def main():
    videoGame = Jerry_Game()
class Jerry_Game():
    def __init__(self):
        # variables de la ventana
        self.fuenteMediana = pygame.font.SysFont("comicsansms", 50)
        self.fuenteChica = pygame.font.SysFont("comicsansms", 20)
        self.fuenteSub = pygame.font.SysFont("comicsansms", 14)
        self.darkBlue = (8, 3, 114)
        self.whiteBlue = (0, 171, 245)
        self.screen_width = 600
        self.screen_height = 500
        self.listaEnemigos = []
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("The Jerry Game")
        self.background = pygame.image.load("jerrygame/dominio/spritesdesign/map.png").convert()
        self.clock = pygame.time.Clock()
        self.initGame()

    def createEnemys(self, cantidad):
        self.counter_mov_enemy = 0
        self.cantidadEnemys = cantidad
        for i in range(self.cantidadEnemys):
            self.coord_E_X = random.randint(0, 550)
            self.coord_E_Y = random.randint(0,450)
            self.enemy_Character = Enemy.Enemy((self.coord_E_X, self.coord_E_Y), "jerrygame/dominio/spritesdesign/enemy.png")
            if self.enemy_Character.rect.colliderect(self.jerry_Character.rect):
                self.enemy_Character.rect.x = random.randint(0,550)
                self.enemy_Character.rect.y = random.randint(0,450)
            self.listaEnemigos.append(self.enemy_Character);

    def createPlayer(self):
        self.Jerry_life = 300
        self.coord_Jerry_x = random.randint(0, 550)
        self.coord_Jerry_y = random.randint(0, 450)
        self.jerry_Character = Player.Player(
            (self.coord_Jerry_x, self.coord_Jerry_y), "jerrygame/dominio/spritesdesign/player.png")

        # variables de la screw_Character
        self.coord_S_X = random.randint(0, 550)
        self.coord_S_Y = random.randint(0, 450)
        self.screw_Character = Screw.Screw((self.coord_S_X, self.coord_S_Y))
        self.points = 0
        self.life_points = 0
        # variables de la vida
        self.Jerry_heart = Heart.Heart((500, 10), self.Jerry_life)
        self.createEnemys(2)

    def updateEnemy(self):
        self.counter_mov_enemy +=1
        self.random_enemy_x = random.randint(0, 550)
        self.random_enemy_y = random.randint(0, 450)   
        self.mov_character = 4;
        self.opcionmov = 1;
        for i in range(self.cantidadEnemys):
            self.listaEnemigos[i].update(self.counter_mov_enemy, self.opcionmov ,self.mov_character )  
            self.opcionmov+=1
            if self.opcionmov == 3:
                self.opcionmov = 1 

    def Game(self):
        self.createPlayer()
        time.sleep(0.1)
        self.game_reset = False
        while self.game_reset == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_reset = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.gamePause()

            pointMessage = self.fuenteChica.render(
                "Point: "+str(self.points), True, self.darkBlue)
            pointMessage2 = self.fuenteChica.render(
                "Point: "+str(self.points), True, self.whiteBlue)
            lifeMessage = self.fuenteChica.render(
                "Life: "+str(self.Jerry_life), True, self.darkBlue)
            lifeMessage2 = self.fuenteChica.render(
                "Life: "+str(self.Jerry_life), True, self.whiteBlue)

            # --------------------------LOGICA DEL VIDEOJUEGO------------------------------------
            self.random_enemy_x = random.randint(0, 550)
            self.random_enemy_y = random.randint(0, 450)
            self.random_screw_x = self.random_enemy_x
            self.random_screw_y = self.random_enemy_y
            # este counter sirve para hacer que los enemy_Character se muevan (mirar el metodo "update" de la clase "Enemy")
            # para entender esto mirar el metodo "update" de la clase "Heart"
            self.updateEnemy()
            self.Jerry_heart.update(True)
            # para entender esto mirar el metodo "update" de la clase "Screw"
            self.screw_Character.update(True)
            # -PARA UTILIZAR EL TECLADO
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.jerry_Character.update("right")
                if event.key == pygame.K_LEFT:
                    self.jerry_Character.update("left")
                if event.key == pygame.K_UP:
                    self.jerry_Character.update("up")
                if event.key == pygame.K_DOWN:
                    self.jerry_Character.update("down")

            self.screen.blit(self.background, [0, 0])
            self.screen.blit(self.screw_Character.image,
                             self.screw_Character.rect)
            self.screen.blit(self.Jerry_heart.image, self.Jerry_heart.rect)
            self.screen.blit(self.jerry_Character.image,
                             self.jerry_Character.rect)
            for i in range(self.cantidadEnemys):
                self.screen.blit(self.listaEnemigos[i].image, self.listaEnemigos[i].rect)
            self.screen.blit(pointMessage, (2, 0))
            self.screen.blit(lifeMessage, (2, 15))
            self.screen.blit(pointMessage2, (2, 3))
            self.screen.blit(lifeMessage2, (2, 18))
            # detectando colisiones del Jerry_character con los enemy_Character/screw_Character
            for i in range(self.cantidadEnemys):
                if pygame.sprite.collide_mask(self.jerry_Character, self.listaEnemigos[i]):
                    self.Jerry_heart.life -= 100  # SIRVE PARA QUE LA IMAGEN DEL CORAZON SE ACTUALICE
                    self.Jerry_life -= 100  # SIRVE PARA QUE SE ACTUALICE EL TEXTO Y SE CIERRE EL JUEGO
                    self.listaEnemigos[i].rect.x = self.random_enemy_x
                    self.listaEnemigos[i].rect.y = self.random_enemy_y                   


            if pygame.sprite.collide_mask(self.jerry_Character, self.screw_Character):
                self.screw_Character.rect.x = self.random_screw_y
                self.screw_Character.rect.y = self.random_screw_y
                self.points += 1  # sumando puntos con la tuerca
                self.life_points += 1  # sumando puntos al contador de vida
            # recuperando vida al tener 3 tuercas
            if self.life_points == 3:
                self.Jerry_heart.life += 100
                self.Jerry_life += 100
                self.life_points = 0
            if self.Jerry_life <= 0:  # ACA SE CIERRA EL JUEGO
                self.background = pygame.image.load(
                    "jerrygame/dominio/spritesdesign/map.png")
                message = self.fuenteMediana.render(
                    "You Lose!!", True, self.darkBlue)
                self.screen.blit(
                    message, ((200), (200)))
                message2 = self.fuenteMediana.render(
                    "You Lose!!", True, self.whiteBlue)
                self.screen.blit(
                    message2, ((200), (203)))
                pygame.display.update()
                time.sleep(0.7)
                self.gameOver()

            # reiniciando el counter enemy_Character
            if self.counter_mov_enemy == 400:
                self.counter_mov_enemy = 0
            pygame.display.update()
            self.clock.tick_busy_loop(60)
            if self.points > 10 and self.points <= 20:
                self.mov_character = 5
            if self.points > 20 and self.points <= 30:
                self.mov_character = 6
            if self.points > 30 and self.points <= 40:
                self.mov_character = 7

    def gamePause(self):
        pausado = True
        while pausado:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        pausado = False
                    if event.key == pygame.K_e:
                        self.game_reset = True
                        pausado = False
            pauseMessage = self.fuenteMediana.render(
                "Juego en pausa", True, (self.whiteBlue))
            centerPauseMessage = pauseMessage.get_rect(center=(self.screen_width/2, self.screen_height/2))
            self.screen.blit(pauseMessage, centerPauseMessage)
            instruction1 = self.fuenteSub.render(
                "Para quitar el pausado presiona C", True, self.whiteBlue)
            self.screen.blit(instruction1, (10, 470))
            salidaText = self.fuenteSub.render(
                "Para salir pulsa E", True, self.whiteBlue)
            self.screen.blit(salidaText, (475, 470))
            pygame.display.update()

    def initGame(self):
        init = True
        while init:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    init = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        self.Game()

                    if event.key == pygame.K_e:
                        init = False

            self.screen.fill((0, 55, 79))
            initmessage = self.fuenteMediana.render(
                "The Jerry Game!!", True, self.whiteBlue)
            centerInitMessage = initmessage.get_rect(center=(self.screen_width/2, self.screen_height/2))
            self.screen.blit(initmessage, centerInitMessage)
            messageInit = self.fuenteChica.render(
                "Para iniciar presiona la tecla I", True, self.whiteBlue)
            self.screen.blit(messageInit, (170, 300))
            instruction1 = self.fuenteSub.render(
                "Para pausar el juego presiona P", True, self.whiteBlue)
            self.screen.blit(instruction1, (10, 470))
            salidaText = self.fuenteSub.render(
                "Para salir pulsa E", True, self.whiteBlue)
            self.screen.blit(salidaText, (475, 470))
            pygame.display.update()
        pygame.quit()

    def gameOver(self):

        self.game_reset = True

        # --------------------------LOGICA DEL VIDEOJUEGO------------------------------------
if __name__ == "__main__":
    main()
