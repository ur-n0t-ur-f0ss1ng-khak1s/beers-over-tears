import pygame
import sys

is_fullscreen = False

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PALE_BLUE = (173, 216, 230)  # RGB values for pale blue

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption('beers over tears')

# Create a font object
font = pygame.font.Font(None, 36)  # None uses the default font, 36 is the font size

# Render the text
text_surface = font.render("""
Look man, it's the third sunny day we've had this year so of course all these za zombies are bound to be outdoors.
All we gotta do is wait at the mud flats and someone with a solution 
(or a demand for some top shelf product) is bound to come by eventually.
""", True, WHITE)  # True for anti-aliasing
current_text_index = 0
intro_texts = [
        {"text":"they say weed is a gateway drug and I never knew why until that day weed became a gateway to the rest of my life.", "speaker":1},
        {"text":"10am I wake up and... to be honest... I think I'm still a bit stoned from eating edibles like popcorn last night. Suffice it to say: I got the damn munchies.", "speaker":1},
        {"text":"Also, suffice it to say I would never let myself get caught without eggs, bacon, sourdough, and some italian roast coffee in my kitchen. Just a few hours from now and I'll have this whole munchies problem solved.", "speaker":1},
        {"text":"Now that I really have been thinking hard about my breakfast strategy I kinda deserve a treat. Like a nice cold indica dab off of my bubbler E rig.", "speaker":1},
        {"text":"God please don't let me get so high that I forget about eating again.", "speaker":1},
        {"text":"****BOOOM CRASH!!****", "speaker":1},
        {"text":"Damn looks like that liquor truck just hit a parked car", "speaker":1},
        {"text":"Yo! Jeri did you see that car crash? Come on let's go check it out!", "speaker":1},
        {"text":"This is ain't a bad wreck. Easy fix too. We better get some beers outta this", "speaker":2},
        {"text":"Good morning sir! The two of us saw the whole thing happen and we happen to be the best mechanics in Anchorage", "speaker":1},
        {"text":"Phew, I sure could use some help. I've just felt slow and stupid and hungry all day... hahaha. Anyway, look gentlemen, I'm not in a rush hahahaha so either we can fix this truck together now or I'm happy to sell ya'll some beer under the table and I'll take the rest of the day off.", "speaker":2},
]
# Load left human art
left_image = pygame.image.load('./art/ross.png')
scaled__left_image = pygame.transform.scale(left_image, (left_image.get_width() * 4, left_image.get_height() * 4))

# Load right human art
right_image = pygame.image.load('./art/steve.png')
scaled__right_image = pygame.transform.scale(right_image, (right_image.get_width() * 4, right_image.get_height() * 4))

# Load background
#image_path = './art/candle-lit-beers.jpeg'
back_image = pygame.image.load('./art/warning-dangerous-waters-and-mud-flats.jpeg')

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

    if current_line:
        lines.append(' '.join(current_line))

    y = rect.top
    for line in lines:
        line_surface = font.render(line, aa, color)
        screen.blit(line_surface, (rect.left, y))
        y += height

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
            elif event.key == pygame.K_SPACE:
                current_text_index = (current_text_index + 1) % len(intro_texts) 
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
        outer_rect.left + 10,
        outer_rect.top + 10,
        outer_rect.width - 2 * 10,
        outer_rect.height - 2 * 10
    )
    #text_rect = text_surface.get_rect(center=inner_rect.center)

    # Render the text surface
    #screen.blit(text_surface, text_rect)
    # Render and blit the wrapped text
    render_text(intro_texts[current_text_index]["text"], font, BLACK, inner_rect)

    # Update the display
    pygame.display.flip()

