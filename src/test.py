import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu Example")

# Load images
play_img = pygame.image.load('play_button.png')
exit_img = pygame.image.load('exit_button.png')

def main_menu():
    while True:
        screen.fill((255, 255, 255))  # White background

        # Display play button
        play_button_rect = play_img.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        screen.blit(play_img, play_button_rect)

        # Display exit button
        exit_button_rect = exit_img.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(exit_img, exit_button_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(mouse_pos):
                    print("Start the game")  # This is where you would start the game
                elif exit_button_rect.collidepoint(mouse_pos):
                    print("Exiting...")  # This is where you would exit the game

        pygame.display.update()

main_menu()
