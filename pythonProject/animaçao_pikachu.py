import pygame
import spritesheet

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

# Load sprite sheet image
try:
    sprite_sheet_image = pygame.image.load('sprite_pikachu.png').convert_alpha()
except pygame.error as e:
    print(f"Error loading sprite sheet: {e}")
    pygame.quit()
    quit()

# Create a SpriteSheet object
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

# Animation parameters
animation_list = []
animation_steps = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 500
frame = 0
step_counter = 0
power = False
transformed = False

# Populate animation list
for animation in animation_steps:
    if step_counter == 1:
        temp_img_list = [sprite_sheet.get_image(step_counter, 197.8, 157, 1.5, BLACK) for _ in range(animation)]
    elif 2 <= step_counter <= 5:
        temp_img_list = [sprite_sheet.get_image(step_counter, 200, 157, 1.5, BLACK) for _ in range(animation)]
    elif 6 <= step_counter <= 9:
        temp_img_list = [sprite_sheet.get_image(step_counter, 200, 157, 1.5, BLACK) for _ in range(animation)]
    else:
        temp_img_list = [sprite_sheet.get_image(step_counter, 155, 157, 1.5, BLACK) for _ in range(animation)]
    animation_list.append(temp_img_list)
    step_counter += animation

print(animation_list)

# Variables for sprite looping
sprite_index = 0
sprite_positions = [0]  # Adicionado os sprites de transformação

# Create a clock object
clock = pygame.time.Clock()

# Main game loop
run = True
shift_pressed = False
while run:

    screen.fill(BG_COLOR)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        last_update = current_time
        frame = (frame + 1) % len(animation_list[action])
        if frame == 0:
            sprite_index = (sprite_index + 1) % len(sprite_positions)
            action = sprite_positions[sprite_index]

    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    if keys[pygame.K_DOWN]:
        animation_cooldown = 140
        action = 1  # A ação agora será a transformação em Super Saiyajin
        frame = 0
    elif keys[pygame.K_RIGHT]:
        if mods & pygame.KMOD_SHIFT:
            clock.tick(10)
            animation_cooldown = 1400
            action = (action + 1) if 6 <= action < 9 else 6
            frame = 0
        else:
            clock.tick(6)
            animation_cooldown = 1400
            action = (action + 1) if 2 <= action < 5 else 2
            frame = 0
    else:
        action = 0
        frame = 0

    if 0 <= action < len(animation_list) and 0 <= frame < len(animation_list[action]):
        screen.blit(animation_list[action][frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()

    pygame.quit()
