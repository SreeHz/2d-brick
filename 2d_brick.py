import pygame
import sys

# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 60, 10
BALL_DIAMETER = 10
BALL_VELOCITY = 1
BRICK_WIDTH, BRICK_HEIGHT = 60, 15

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up assets
paddle = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_DIAMETER, BALL_DIAMETER)

ball_dx = BALL_VELOCITY
ball_dy = BALL_VELOCITY

bricks = []
for i in range(5):
    for j in range(10):
        brick = pygame.Rect(j * (BRICK_WIDTH + 5) + 50, i * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_ip(-2, 0)
    if keys[pygame.K_RIGHT]:
        paddle.move_ip(2, 0)

    # Keep paddle on the screen
    if paddle.left < 0:
        paddle.left = 0
    if paddle.right > SCREEN_WIDTH:
        paddle.right = SCREEN_WIDTH

    # Move ball
    ball.move_ip(ball_dx, ball_dy)

    # Collide with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1
            break

    # Collide with paddle
    if ball.colliderect(paddle):
        ball_dy *= -1

    # Collide with wall
    if ball.left < 0 or ball.right > SCREEN_WIDTH:
        ball_dx *= -1
    if ball.top < 0:
        ball_dy *= -1

    # Ball falls off the screen
    if ball.bottom > SCREEN_HEIGHT:
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # All bricks are broken - player wins!
    if not bricks:
        print("You win!")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill((0, 0, 0))
    
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)

    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    
    pygame.display.flip()
