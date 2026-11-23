from pathlib import Path
from datetime import datetime

import pygame

pygame.init()

screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("Character Design Editor")
clock = pygame.time.Clock()

ASSET_FOLDER = Path(__file__).resolve().parent / "assets"
EXPORT_FOLDER = Path(__file__).resolve().parent / "exports"
PREVIEW_POSITION = (40, 110)

font = pygame.font.Font(None, 32)
title_font = pygame.font.Font(None, 42)
small_font = pygame.font.Font(None, 22)


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

reset_button = pygame.Rect(550, 520, 230, 50)
export_button = pygame.Rect(685, 530, 190, 50)

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
    text_position = text_image.get_rect(
        center=rectangle.center
    )
    screen.blit(text_image, text_position)

def export_character():
    EXPORT_FOLDER.mkdir(parents=True, exist_ok=True)
#transparent canvas
    character = pygame.Surface(
        base.get_size(), pygame.SRCALPHA
    )
    character.fill((0, 0, 0, 0))
#Layers onto canvas
    character.blit(base, (0,0))
    character.blit(outfits[outfit_index], (0,0))
    character.blit(faces[face_index], (0,0))
    character.blit(hair[hair_index], (0,0))

    export_path = EXPORT_FOLDER / f"character.png"

    pygame.image.save(character, str(export_path))

    return export_path


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if hair_previous.collidepoint(event.pos):
                    hair_index = (hair_index - 1) % len(hair)
                elif hair_next.collidepoint(event.pos):
                    hair_index = (hair_index + 1) % len(hair) 
                if face_previous.collidepoint(event.pos):
                    face_index = (face_index - 1) % len(faces)
                elif face_next.collidepoint(event.pos):
                    face_index = (face_index + 1) % len(faces) 
                if outfit_previous.collidepoint(event.pos):
                    outfit_index = (outfit_index - 1) % len(outfits)
                elif outfit_next.collidepoint(event.pos):
                    outfit_index = (outfit_index + 1) % len(outfits) 
                elif reset_button.collidepoint(event.pos):
                    hair_index = 0
                    face_index = 0
                    outfit_index = 0
                elif export_button.collidepoint(event.pos):
                    try:
                        saved_path = export_character()
                        status_message = "PNG saved in the exports file"
                        print(f"Saved PNG: {saved_path}")

                    except (OSError, pygame.error) as error:
                        status_message = "Export failed. See terminal."
                        print(f"Could not eport PNG: {error}")

    screen.fill ("#F4F0FA")

    screen.blit(base, PREVIEW_POSITION)
    screen.blit(outfits[outfit_index], PREVIEW_POSITION)
    screen.blit(faces[face_index], PREVIEW_POSITION)
    screen.blit(hair[hair_index], PREVIEW_POSITION)

    draw_text("Hairstyle", (510, 150))
    draw_button(hair_previous, "<")
    draw_button(hair_next, ">")
    draw_text(
            f"{hair_index + 1} / {len(hair)}",
            (630, 205),
        )

    draw_text("Expression", (510, 270))
    draw_button(face_previous, "<")
    draw_button(face_next, ">")
    draw_text(
            f"{face_index + 1} / {len(faces)}",
            (630, 325),
        )

    draw_text("Outfit", (510, 390))
    draw_button(outfit_previous, "<")
    draw_button(outfit_next, ">")
    draw_text(
            f"{outfit_index + 1} / {len(outfits)}",
            (630, 445),
        )

    draw_button(reset_button, "Reset character")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()