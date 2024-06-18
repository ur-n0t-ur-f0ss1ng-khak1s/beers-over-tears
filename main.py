import pygame
import sys

is_fullscreen = False

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption('beers over tears')

# Create a font object
font = pygame.font.Font(None, 36)  # None uses the default font, 36 is the font size

# Render the text
text_surface = font.render('Hello, Pygame!', True, BLACK)  # True for anti-aliasing

# Load left human art
#image_path = './art/ross.png'
left_image = pygame.image.load('./art/ross.png')
scaled__left_image = pygame.transform.scale(left_image, (left_image.get_width() * 4, left_image.get_height() * 4))

# Load background
#image_path = './art/candle-lit-beers.jpeg'
back_image = pygame.image.load('./art/candle-lit-beers.jpeg')

def adjust_to_aspect_ratio(width, height):
    # Maintain a 4:3 aspect ratio
    aspect_ratio = 4 / 3
    if width / height > aspect_ratio:
        width = int(height * aspect_ratio)
    else:
        height = int(width / aspect_ratio)
    return width, height

def scale(w,h):
    global text_rect, left_per_rect, back_rect, scaled_left_image, left_image, back_image

    width, height = adjust_to_aspect_ratio(w, h)
    print(f"{width},{height}")

    text_rect = text_surface.get_rect(center=(w // 2, ((h - height) / 2) + 10))

    scaled_left_image = pygame.transform.scale(left_image, (left_image.get_width() * width/200, left_image.get_height() * height/150))
    # Get the rectangle for positioning
    left_per_rect = scaled_left_image.get_rect()
    left_per_rect.topleft = (((w - width) / 2) + 20, ((h - height) / 2)+(height-(79*(height/150))))

    back_image = pygame.transform.scale(back_image, (back_image.get_width() * width/back_image.get_width(), back_image.get_height() * height/back_image.get_height()))
    # Get the rectangle for positioning
    back_rect = back_image.get_rect()
    back_rect.topleft = ((w - width) / 2,(h - height) / 2)

scale(800,600)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
                scale(pygame.display.get_window_size()[0],pygame.display.get_window_size()[1])
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            scale(event.w, event.h)

    
    # Fill the screen with blue 
    screen.fill((0, 0, 255))

    # Render the background 
    screen.blit(back_image, back_rect)

    # Render the image
    screen.blit(scaled_left_image, left_per_rect)

    # Render the text surface
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

