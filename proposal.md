# Final Project - Character Editor

## Repository
https://github.com/kinzleyk/Final-Project.git

## Description
I will build a simple 2D character design editor in Python with Pygame. Users will be able to flip through different
hairstyles, facial expressions, and outfits to try out different looks for an original character before committing to a design.
## Features
- Live character preview
	- I will draw a base character and create transparent PNg's for the hair, facial expressions, and outfits. I will use Pygame
   to layer the selected images to display the complete character.
- Previous and next buttons
	- Each category will haves its own left and right arrows. I'll store the options in lists and track the selected index
   for each category so that changing the hair keeps the current face and outfit. The arrows will wrap at the end.
- Reset button 
	- A reset button will return all three categories to their starting option, or the starting index

## Challenges
- I'll need to learn how to export transparent images onto a shared canvas to ensure all the options line up with the base
- I'll need to practice handling mouse clicks in Pygame and using list indexes to cycle through categories
- I'll need to figure out how to organize and load the image files so I can add new images without rewritting the code

## Outcomes
Ideal Outcome:
- A polished editor with orgiinal artwork with multiple categories that can be added to if more images are provided. Several
  choices in each category, and a reset button.

Minimal Viable Outcome:
- A single screen with a live preview with working arrows for each category with at least 3 options each. Users should be able
  to mix the three categories independently and see the change immediately.
## Milestones

- Week 1
  1. Make the base character 
  2. Build the Pygame window and test layering with placeholder art.

- Week 2
  1. Add the previous and nexdt buttons and ensure each category cycles independenly
  2. Import images for at least 3 options for each category

- Week N (Final)
  1. Test the artwork for alignment, verify controls, and implement the reset button.
  2. Ensure the code is optimized and doesn't slow down with continued use
