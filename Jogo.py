# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, GAME_OVER
from init_screen import init_screen
from game_screen import game_screen
from game_over_screen import game_over_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state, score = game_screen(window)
    elif state == GAME_OVER:
   
        state = game_over_screen(window, score)
    else:
        state = QUIT

# ----- Gera tela 'game over'
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')



# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

