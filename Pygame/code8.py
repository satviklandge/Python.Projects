import pygame
import random

pygame.init()

WIDTH,HEIGHT = 600 , 600
screen = pygame.display.set_mode((WIDTH , HEIGHT ))
pygame.display.set_caption("Plane game")

plane = pygame.Rect(200, 500, 40, 40)

enemies = []

clock = pygame.time.Clock()
score = 0

running = True

while running :
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        plane.x -= 5
    if keys[pygame.K_RIGHT]:
        plane.x += 5

    if random.randint(1, 30) == 1:
        enemies.append (pygame.Rect(random.randint(0, 560),0, 40, 40))

    for enemy in enemies[ : ]:
        enemy.y += 5

        if enemy.colliderect(plane):
            print ("Game Over !!!")
            running = False

        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            score += 1

        pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.draw.rect(screen, (0, 255, 255), plane)

    pygame.display.set_caption(f"Score: (score)")

    pygame.display.update()
    clock.tick(60)

pygame.quit()