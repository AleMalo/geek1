import pygame

class Player:
    def __init__(self, number, x, y):
        self.x = x
        self.y = y
        self.speed = 3
        self.number = number
        if number == 1:
            self.image = pygame.image.load('haker1.png')
        else:
            self.image = pygame.image.load('haker1.png')


    def move(self, keys):
        if self.number == 1:
            if keys[pygame.K_RIGHT]:
                self.x += self.speed
            if keys[pygame.K_LEFT]:
                self.x -= self.speed
            if keys[pygame.K_UP]:
                self.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.y += self.speed
        else:
            if keys[pygame.K_d]:
                self.x += self.speed
            if keys[pygame.K_a]:
                self.x -= self.speed
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed

        # if

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))



class Chest:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('chest_closed.png')
        self.image2 = pygame.image.load('chest_open.png')

    def opening(self, keys):
        if keys[pygame.K_e]:
            self.image = self.image2

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))