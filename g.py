import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Football Game")    

    
# Colors
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_COLOR = (220, 220, 0)
PLAYER_COLOR = (30, 144, 255)
GOAL_COLOR = (255, 0, 0)

# Player settings
player_pos = [100, HEIGHT // 2]
player_radius = 20
player_speed = 5

# Ball settings
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_radius = 15
ball_speed = 7

# Goal settings
goal_rect = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 50, 40, 100)

# Game loop
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 36)
running = True
while running:
    screen.fill(GREEN)
    pygame.draw.rect(screen, GOAL_COLOR, goal_rect)
    pygame.draw.circle(screen, PLAYER_COLOR, player_pos, player_radius)
    pygame.draw.circle(screen, BALL_COLOR, ball_pos, ball_radius)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] - player_radius > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] + player_radius < WIDTH:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] - player_radius > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] + player_radius < HEIGHT:
        player_pos[1] += player_speed

    # Ball collision with player
    dx = ball_pos[0] - player_pos[0]
    dy = ball_pos[1] - player_pos[1]
    distance = (dx**2 + dy**2) ** 0.5
    if distance < player_radius + ball_radius:
        # Move ball in direction of player movement
        if keys[pygame.K_LEFT]:
            ball_pos[0] -= ball_speed
        if keys[pygame.K_RIGHT]:
            ball_pos[0] += ball_speed
        if keys[pygame.K_UP]:
            ball_pos[1] -= ball_speed
        if keys[pygame.K_DOWN]:
            ball_pos[1] += ball_speed

    # Ball boundaries
    ball_pos[0] = max(ball_radius, min(WIDTH - ball_radius, ball_pos[0]))
    ball_pos[1] = max(ball_radius, min(HEIGHT - ball_radius, ball_pos[1]))

    # Check for goal
    if goal_rect.collidepoint(ball_pos[0], ball_pos[1]):
        score += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()