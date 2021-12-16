import pygame, random
import sprites.util

class Bomb(pygame.sprite.Sprite):


    def __init__(self, *group):
        image = sprites.util.load_image("bomb.png")
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(300)
        self.rect.y = random.randrange(300)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)