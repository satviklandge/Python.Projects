import pygame
import random

pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Lightning Strom")
clock = pygame .time.Clock()

def lightning():
    x = random.randint(100, W - 100)
    points = [(x, 0)]

    while points[-1][1] < H:
        x += random.randint(-40, 40)
        y = points[-1][1] + random.randint(15, 30)
        points.append((x, y))

    return points
bolt = lightning()
flash = 0

running = True
while running :
    screen.fill((0, 0, 0))

    # Random Lightning Strike 
    if random.randint(1, 50) == 1:
        bolt = lightning()
        flash = 255

    # Stronger Blue Flash Effect
    if flash > 0:
        overlay = pygame.Surface((W, H))
        overlay.set_alpha(flash)
        overlay.fill((100, 200, 255))
        screen.blit(overlay, (0, 0))
        flash -= 10

    # lightning glow layers
    pygame.draw.lines(screen, (0,80,255), False, bolt, 10)
    pygame.draw.lines(screen, (80,180,255), False, bolt, 6)
    pygame.draw.lines(screen, (180,230,255), False, bolt, 3)
    pygame.draw.lines(screen, (255,255,255), False, bolt, 1)

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
