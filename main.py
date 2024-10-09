import pygame, time
pygame.init()

# Define constants
WIDTH = 640
HEIGHT = 480

FPS = 60

BLACK = (0,   0,   0  )
WHITE = (255, 255, 255)

# Define variables
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

delta = 0
prev_time = time.time()

# Main loop
running = True
while running:
    # Tick clock for updating on framerate
    clock.tick(FPS)

    # Calculate delta
    now = time.time()
    delta = now - prev_time
    prev_time = now

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill with white
    screen.fill(WHITE)

    # UPDATE YOUR SPRITES HERE!
    # e.x. screen.blit(player, (player.x, player.y))

    # Update the screen
    pygame.display.flip()

# Quit after main loop stops
pygame.quit()