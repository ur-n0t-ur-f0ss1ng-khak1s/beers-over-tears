import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption('beers over tears')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a font object
font = pygame.font.Font(None, 36)  # None uses the default font, 36 is the font size

# Render the text
text_surface = font.render('Hello, Pygame!', True, BLACK)  # True for anti-aliasing

def adjust_to_aspect_ratio(width, height):
    # Maintain a 4:3 aspect ratio
    aspect_ratio = 4 / 3
    if width / height > aspect_ratio:
        width = int(height * aspect_ratio)
    else:
        height = int(width / aspect_ratio)
    return width, height

# Get the rectangle for positioning
text_rect = text_surface.get_rect()
text_rect.center = (400, 300)  # Position the text at the center of the window

# Load the image
image_path = './art/ross.png'
image = pygame.image.load(image_path)

scaled_image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))

# Get the rectangle for positioning
image_rect = scaled_image.get_rect()
image_rect.topleft = (20, 284)  # Position the image at coordinates (100, 100)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            # Update the screen size
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            # Optionally, re-render the text to fit the new size or adjust its position
            text_rect = text_surface.get_rect(center=(event.w // 2, event.h // 2))

    # Fill the screen with blue 
    screen.fill((0, 0, 255))

    width = pygame.display.get_window_size()[0]
    height = pygame.display.get_window_size()[1]
    width, height = adjust_to_aspect_ratio(width, height)

    scaled_image = pygame.transform.scale(image, (image.get_width() * width/200, image.get_height() * height/150))

    # Get the rectangle for positioning
    image_rect = scaled_image.get_rect()
    image_rect.topleft = (20, height-(79*(height/150)))  # Position the image at coordinates (100, 100)

    # Render the image
    screen.blit(scaled_image, image_rect)

        # Render the text surface
    screen.blit(text_surface, text_rect)

    print(pygame.display.get_window_size())
    # Update the display
    pygame.display.flip()

