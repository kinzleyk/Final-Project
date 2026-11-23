from pathlib import Path

import pygame

pygame.init()

screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("Character Design Editor")
clock = pygame.time.Clock()

ASSET_FOLDER = Path(__file__).resolve().parent / "assets"
PREVIEW_POSITION = (40, 110)

font = pygame.font.Font(None, 32)
title_font = pygame.font.Font(None, 42)


def load_image(path):
    """Load PNG while keeping transparent background"""
    return pygame.image.load(str(path)).convert_alpha()

def load_category(folder_name):
    """Load PNGs from one category in filename order"""
    folder = ASSET_FOLDER / folder_name
    paths = sorted(folder.glob("*.png"))

    if not paths:
        raise FileNotFoundError(
            f"No PNG images found in: {folder}"
        )
    return [load_image(path) for path in paths] 

base = load_image(ASSET_FOLDER / "base.png")
hair = load_category("hair")
faces = load_category("faces")
outfits = load_category("outfits")

hair_index = 0
face_index = 0
outfit_index = 0

# Button positions: x, y, width, height

hair_previous = pygame.Rect(510, 190, 60, 50)
hair_next = pygame.Rect(760, 190, 60, 50)

face_previous = pygame.Rect(510, 310, 60, 50)
face_next = pygame.Rect(760, 310, 60, 50)

outfit_previous = pygame.Rect(510, 430, 60, 50)
outfit_next = pygame.Rect(760, 430, 60, 50)

def draw_text(text, position):
    text_image = font.render(text, True, "#30283E")
    screen.blit(text_image, position)

def draw_button(rectangle, label):

    if rectangle.collidepoint(pygame.mouse.get_pos()):
        color = "#563877"
    else:
        color = "#705099"

    pygame.draw.rect(
        screen, color, rectangle, border_radius=10
    )

    text_image = font.render(label, True, "white")
    text_position = text_image.get.rect(
        center=rectangle.center
    )
    screen.blit(text_image, text_position)
    
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill ("#F4F0FA")

    screen.blit(base, PREVIEW_POSITION)
    screen.blit(outfits[outfit_index], PREVIEW_POSITION)
    screen.blit(faces[face_index], PREVIEW_POSITION)
    screen.blit(hair[hair_index], PREVIEW_POSITION)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()