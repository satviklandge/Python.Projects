import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HIGHT = 800
GRAVITY = 0.25
FLAP_STRENGTH = -6.5
PIPE_SPEED = 3
PIPE_GAP = 150

# Colors
WHITE = (255, 255, 255)
SKY_BLUE = (113, 197, 207)
BIRD_RED = (247, 212, 45)
PIPE_GREEN = (115, 191, 46)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)


class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HIGHT // 2
        self.velocity = 0
        self.radius = 15

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += int(self.velocity)
        # prevent going off-screen
        if self.y < self.radius:
            self.y = self.radius
            self.velocity = 0
        if self.y > SCREEN_HIGHT - self.radius:
            self.y = SCREEN_HIGHT - self.radius
            self.velocity = 0

    def draw(self):
        pygame.draw.circle(screen, BIRD_RED, (self.x, self.y), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)


class Pipe:
    WIDTH = 50

    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, 400)
        self.passed = False
        # Top and bottom rects
        self.top_rect = pygame.Rect(self.x, 0, Pipe.WIDTH, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, Pipe.WIDTH, SCREEN_HIGHT - (self.height + PIPE_GAP))

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self):
        pygame.draw.rect(screen, PIPE_GREEN, self.top_rect)
        pygame.draw.rect(screen, PIPE_GREEN, self.bottom_rect)


def main():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    game_over = False

    while True:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.flap()
                elif event.key == pygame.K_SPACE and game_over:
                    # Restart the game
                    bird = Bird()
                    pipes = [Pipe()]
                    score = 0
                    game_over = False

        if not game_over:
            # Update game objects
            bird.update()

            # Spawn new pipes
            if pipes[-1].x < SCREEN_WIDTH - 200:
                pipes.append(Pipe())

            for pipe in pipes:
                pipe.update()

                # check if bird passed the pipe for scoring
                if not pipe.passed and pipe.x + Pipe.WIDTH < bird.x:
                    pipe.passed = True
                    score += 1

                # Check for collisions
                bird_rect = bird.get_rect()
                if bird_rect.colliderect(pipe.top_rect) or bird_rect.colliderect(pipe.bottom_rect):
                    game_over = True

            # Remove off-screen pipes
            pipes = [p for p in pipes if p.x > -Pipe.WIDTH]

            # Floor/Celline
            if bird.y + bird.radius > SCREEN_HIGHT or bird.y - bird.radius < 0:
                game_over = True

        # Draw
        screen.fill(SKY_BLUE)
        for pipe in pipes:
            pipe.draw()
        bird.draw()
        score_surf = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (10, 10))

        if game_over:
            over_surf = font.render("Game Over - Press SPACE to restart", True, WHITE)
            screen.blit(over_surf, (SCREEN_WIDTH//2 - over_surf.get_width()//2, SCREEN_HIGHT//2))

        pygame.display.flip()
        clock.tick(60)


    if __name__ == '__main__':
        main()
           
        