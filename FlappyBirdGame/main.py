import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
BIRD_SIZE = 20
PIPE_WIDTH = 80
PIPE_GAP = 200
GRAVITY = 0.6
FLAP_STRENGTH = -10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock to control the frame rate
clock = pygame.time.Clock()


class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, int(self.y)), BIRD_SIZE)


class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.passed = False

    def update(self):
        self.x -= 5

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, GREEN, (self.x, self.height +
                         PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP))

    def off_screen(self):
        return self.x + PIPE_WIDTH < 0

    def collides_with(self, bird):
        return (bird.x - BIRD_SIZE < self.x + PIPE_WIDTH and bird.x + BIRD_SIZE > self.x and
                (bird.y - BIRD_SIZE < self.height or bird.y + BIRD_SIZE > self.height + PIPE_GAP))


def show_game_over_screen(score):
    # Display game over screen
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

    # Display score
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(f"Score: {score}", True, WHITE)
    score_text_rect = score_text.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(score_text, score_text_rect)

    pygame.display.flip()


def main():
    bird = Bird()
    pipes = [Pipe(WIDTH + i * 300) for i in range(3)]
    score = 0

    running = True
    game_over = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over:
                        main()  # Restart the game
                        return  # Add this line to exit the current game loop
                    else:
                        bird.flap()

        if not game_over:
            bird.update()

            for pipe in pipes:
                pipe.update()

            if pipes[0].off_screen():
                pipes.pop(0)
                pipes.append(Pipe(pipes[-1].x + 300))

            if not pipes[0].passed and pipes[0].x + PIPE_WIDTH < bird.x:
                pipes[0].passed = True
                score += 1

            if pipes[0].collides_with(bird) or bird.y + BIRD_SIZE > HEIGHT or bird.y - BIRD_SIZE < 0:
                game_over = True

            screen.fill((0, 0, 0))
            bird.draw()
            for pipe in pipes:
                pipe.draw()

            font = pygame.font.Font(None, 36)
            text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(text, (10, 10))
        else:
            screen.fill((0, 0, 0))
            show_game_over_screen(score)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
