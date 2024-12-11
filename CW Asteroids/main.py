
import pygame
import math
import random
pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Asteroids")

WIDTH = 800
HEIGHT = 800

asteroid50 = pygame.image.load("asteroidPics/asteroid50.png")
asteroid100 = pygame.image.load("asteroidPics/asteroid100.png")
asteroid150 = pygame.image.load("asteroidPics/asteroid150.png")
rocket = pygame.image.load("asteroidPics/spaceRocket.png")
alienShip = pygame.image.load("asteroidPics/alienShip.png")
star = pygame.image.load("asteroidPics/star.png")
bg = pygame.image.load("asteroidPics/starbg.png")

bangLarge = pygame.mixer.Sound("sounds/bangLarge.wav")
bangSmall = pygame.mixer.Sound("sounds/bangSmall.wav")
shootSound = pygame.mixer.Sound("sounds/shoot.wav")

# - changing the volume
bangLarge.set_volume(0.7)
bangSmall.set_volume(1.5)
shootSound.set_volume(0.3)

clock = pygame.time.Clock()
gameover = False
lives = 3
score = 0
rapidfire = False
isSoundOn = True
rfStart = -1

class Player():
    def __init__(self):
        self.image = rocket
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.angle = 0
        self.rotatedSurface = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    def drawPlayer(self, window):
        window.blit(self.rotatedSurface, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurface = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosin  * self.w//2, self.y - self.sine * self.h//2)
    
    def turnRight(self):
        self.angle -= 5
        self.rotatedSurface = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosin  * self.w//2, self.y - self.sine * self.h//2)
    
    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurface = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosin  * self.w//2, self.y - self.sine * self.h//2)

    def update(self):
        if self.x > WIDTH + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = WIDTH
        elif self.y < -50:
            self.y = HEIGHT
        elif self.y > HEIGHT + 50:
            self.y = 0

class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x , self.y = self.point
        self.w = 4
        self.h = 4
        self.cosine = player.cosine
        self.sine = player.sine
        self.vx = self.cosine * 10
        self.vy = self.sine * 10
    
    def move(self):
        self.x += self.vx
        self.y += self.vy
    
    def draw(self, window):
        pygame.draw.rect(window, (255,255,255), [self.x, self.y, self.w, self.h])

    def outOfScreen(self):
        if self.x < -50 or self.x > WIDTH or self.y < -50 or self.y > HEIGHT:
            return True

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)