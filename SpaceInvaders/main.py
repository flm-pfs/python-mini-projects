import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 5
ALIEN_SPEED = 1
BULLET_SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Font for displaying the score and game over message
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))


class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -50)
        self.speed = ALIEN_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -50)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()


# Sprite groups
all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create aliens
for _ in range(10):
    alien = Alien()
    all_sprites.add(alien)
    aliens.add(alien)

# Game loop
running = True
score = 0
game_over = False
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
            elif event.key == pygame.K_RETURN and game_over:
                running = False

    if not game_over:
        # Update
        all_sprites.update()

        # Check for game over condition
        if pygame.sprite.spritecollide(player, aliens, False):
            game_over = True

        # Collision detection
        if not game_over:
            hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
            for hit in hits:
                score += 1
                alien = Alien()
                all_sprites.add(alien)
                aliens.add(alien)

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Display the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = game_over_font.render("Game Over", True, WHITE)
        game_over_rect = game_over_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(game_over_text, game_over_rect)

        final_score_text = font.render(f"Your score: {score}", True, WHITE)
        final_score_rect = final_score_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(final_score_text, final_score_rect)

        press_enter_text = font.render("Press Enter to quit", True, WHITE)
        press_enter_rect = press_enter_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(press_enter_text, press_enter_rect)

    # Flip the display
    pygame.display.flip()

pygame.quit()
sys.exit()
