import pygame
import sys
from intro import intro_texts
from intro_druggie1 import intro_druggie1
#from intro_charitable1 import intro_charitable1

is_fullscreen = False

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PALE_BLUE = (173, 216, 230)  # RGB values for pale blue

# victory point counters
charitable_vp = 0
selfish_vp = 0
no_morals_vp = 0
druggie_vp = 0

curr_text = []

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption('beers over tears')

# Create a font object
font = pygame.font.Font(None, 36)  # None uses the default font, 36 is the font size

current_text_index = 0

curr_text = intro_texts
# Load left human art
left_image = pygame.image.load('./art/ross.png')
scaled__left_image = pygame.transform.scale(left_image, (left_image.get_width() * 4, left_image.get_height() * 4))

# Load right human art
right_image = pygame.image.load('./art/steve.png')
scaled__right_image = pygame.transform.scale(right_image, (right_image.get_width() * 4, right_image.get_height() * 4))

# Load background
#image_path = './art/candle-lit-beers.jpeg'
back_image = pygame.image.load('./art/ross-wakes-up.jpeg')

# load textbox
text_box_image = pygame.image.load('./art/text-box.png')

def adjust_to_aspect_ratio(width, height):
    # Maintain a 4:3 aspect ratio
    aspect_ratio = 4 / 3
    if width / height > aspect_ratio:
        width = int(height * aspect_ratio)
    else:
        height = int(width / aspect_ratio)
    return width, height

def scale(w,h):
    global text_rect, left_per_rect, back_rect, scaled_left_image, left_image, back_image, outer_rect, right_per_rect, scaled_right_image, right_image, scaled_text_box_image, text_box_image

    width, height = adjust_to_aspect_ratio(w, h)
    print(f"{width},{height}")

    # scaling the text box
    outer_rect = pygame.Rect(((w - width) / 2) + 20, ((h - height) / 2) + 10, width - 40, (height / 2) - 20)
    scaled_text_box_image = pygame.transform.scale(text_box_image, (outer_rect.w, outer_rect.h))

    # scaling the left character
    scaled_left_image = pygame.transform.scale(left_image, (left_image.get_width() * width/200, left_image.get_height() * height/150))

    left_per_rect = scaled_left_image.get_rect() # rectangle for positioning on the screen
    left_per_rect.topleft = (((w - width) / 2) + 20, ((h - height) / 2)+(height-(79*(height/150))))

    # scaling the right character
    scaled_right_image = pygame.transform.scale(right_image, (right_image.get_width() * width/200, right_image.get_height() * height/150))

    right_per_rect = scaled_right_image.get_rect() # rectangle for positioning on the screen
    right_per_rect.topright = (((w - width) / 2) + width - 20, ((h - height) / 2)+(height-(79*(height/150))))

    # scaling the background
    back_image = pygame.transform.scale(back_image, (back_image.get_width() * width/back_image.get_width(), back_image.get_height() * height/back_image.get_height()))

    back_rect = back_image.get_rect()
    back_rect.topleft = ((w - width) / 2,(h - height) / 2)

# Function to render wrapped text
def render_text(text, font, color, rect, aa=True):
    words = text.split(' ')
    lines = []
    current_line = []
    width, height = 0, 0

    for word in words:
        current_line.append(word)
        width, height = font.size(' '.join(current_line))
        if width > rect.width:
            current_line.pop()
            lines.append(' '.join(current_line))
            current_line = [word]
        elif word == "\n":
            current_line.pop()
            lines.append(' '.join(current_line))
            current_line = []

    if current_line:
        lines.append(' '.join(current_line))

    y = rect.top
    for line in lines:
        line_surface = font.render(line, aa, color)
        screen.blit(line_surface, (rect.left, y))
        y += height

def handle_input(input_dict):
    global charitable_vp, selfish_vp, no_morals_vp, druggie_vp, curr_text
    if (input_dict["victory"] == "charitable"):
        charitable_vp += input_dict["VP"]
    elif (input_dict["victory"] == "selfish"):
        selfish_vp += input_dict["VP"]
    elif (input_dict["victory"] == "no_morals"):
        no_morals_vp += input_dict["VP"]
    elif (input_dict["victory"] == "druggie"):
        druggie_vp += input_dict["VP"]
    curr_text = input_dict["next"]


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
            elif (event.key == pygame.K_SPACE and "input" not in curr_text[current_text_index]):
                current_text_index = (current_text_index + 1) % len(curr_text) 
            elif (event.key == pygame.K_1 and 1 in curr_text[current_text_index]["input"]):
                handle_input(curr_text[current_text_index]["input"][1])
                current_text_index = (current_text_index + 1) % len(curr_text) 
                print("1 pressed")
            elif (event.key == pygame.K_2 and 2 in curr_text[current_text_index]["input"]):
                handle_input(curr_text[current_text_index]["input"][2])
                current_text_index = (current_text_index + 1) % len(curr_text) 
                print("2 pressed")
            elif (event.key == pygame.K_3 and 3 in curr_text[current_text_index]["input"]):
                current_text_index = (current_text_index + 1) % len(curr_text) 
                print("3 pressed")

        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            scale(event.w, event.h)

    
    # Fill the screen with blue 
    screen.fill(PALE_BLUE)

    # Render the background 
    screen.blit(back_image, back_rect)

    # render the background image
    screen.blit(scaled_text_box_image, outer_rect)
    #draw the text box background
    #pygame.draw.rect(screen, PALE_BLUE, outer_rect)

    # Render the image
    screen.blit(scaled_left_image, left_per_rect)

    # Render the right image
    screen.blit(scaled_right_image, right_per_rect)

     # Calculate the inner text rectangle dimensions and position
    inner_rect = pygame.Rect(
        outer_rect.left + 25,
        outer_rect.top + 25,
        outer_rect.width - 2 * 25,
        outer_rect.height - 2 * 25
    )
    #text_rect = text_surface.get_rect(center=inner_rect.center)

    # Render the text surface
    #screen.blit(text_surface, text_rect)
    # Render and blit the wrapped text
    print(curr_text[current_text_index])
    if (curr_text[current_text_index]["speaker"] == 0):
        TEXT_COLOR = BLACK 
    elif (curr_text[current_text_index]["speaker"] == 1):
        TEXT_COLOR = WHITE
    elif (curr_text[current_text_index]["speaker"] == 2):
        TEXT_COLOR = RED 
    elif (curr_text[current_text_index]["speaker"] == 3):
        TEXT_COLOR = GREEN

    render_text(curr_text[current_text_index]["text"], font, TEXT_COLOR, inner_rect)

    # Update the display
    pygame.display.flip()

