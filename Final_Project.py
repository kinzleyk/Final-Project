from pathlib import Path

import pygame

pygame.init()

screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("Character Design Editor")

clock = pygame.time.Clock()

ASSET_FOLDER = Path(__file__).resolve().parent / "assets"
PREVIEW_POSITION = (40, 110)

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