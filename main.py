import pygame
import sys
from intro import intro_texts

is_fullscreen = False

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
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
#intro_texts = [
#        {"text":"they say weed is a gateway drug and I never knew why until that day weed became a gateway to the rest of my life.", "speaker":0},
#        {"text":"10am I wake up and... to be honest... I think I'm still a bit stoned from eating edibles like popcorn last night. Suffice it to say: I got the damn munchies.", "speaker":0},
#        {"text":"Also, suffice it to say I would never let myself get caught without eggs, bacon, sourdough, and some italian roast coffee in my kitchen. Just a few hours from now and I'll have this whole munchies problem solved.", "speaker":0},
#        {"text":"Now that I really have been thinking hard about my breakfast strategy I kinda deserve a treat. Like a nice cold indica dab off of my bubbler E rig.", "speaker":0},
#        {"text":"God please don't let me get so high that I forget about eating again.", "speaker":0},
#        {"text":"****BOOOM CRASH!!****", "speaker":0},
#        {"text":"Damn looks like that liquor truck just hit a parked car", "speaker":0},
#        {"text":"Yo! Jeri did you see that car crash? Come on let's go check it out!", "speaker":0},
#        {"text":"This is ain't a bad wreck. Easy fix too. We better get some beers outta this", "speaker":1},
#        {"text":"Good morning sir! The two of us saw the whole thing happen and we happen to be the best mechanics in Anchorage", "speaker":0},
#        {"text":"Phew, I sure could use some help. I've just felt slow and stupid and hungry all day... hahaha. Anyway, look gentlemen, I'm not in a rush hahahaha so either we can fix this truck together now or I'm happy to sell ya'll some beer under the table and I'll take the rest of the day off.", "speaker":1},
#        {"text":"""(1) I'd be god damned if I left a fellow American to suffer due to the forces of entropy... not to mention how bad this could affect the economy... we're gonna help!! \n \n (2) All this talking has me thirsting. We'll take the beer, sir.""", "speaker":2, "input":{1:{"victory":"charitable", "VP":10}, 2:{"victory":"selfish", "VP":10}}},
#]

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
    if (input_dict["victory"] == "charitable"):
        charitable_vp += input_dict["VP"]
    elif (input_dict["victory"] == "selfish"):
        selfish_vp += input_dict["VP"]
    elif (input_dict["victory"] == "no_morals"):
        no_morals_vp += input_dict["VP"]
    elif (input_dict["victory"] == "druggie"):
        druggie_vp += input_dict["VP"]


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
    if (curr_text[current_text_index]["speaker"] == 0):
        TEXT_COLOR = BLACK 
    elif (curr_text[current_text_index]["speaker"] == 1):
        TEXT_COLOR = WHITE
    elif (curr_text[current_text_index]["speaker"] == 2):
        TEXT_COLOR = RED 
    render_text(curr_text[current_text_index]["text"], font, TEXT_COLOR, inner_rect)

    # Update the display
    pygame.display.flip()

