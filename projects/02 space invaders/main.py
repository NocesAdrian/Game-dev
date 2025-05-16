import pygame
import sys
from src.core.game import GameLoop

SCREEN_HEIGHT_START = 450
SCREEN_WIDTH_START = 700
GAME_TITLE = "space invaders"
FPS = 120

def start():
    game = GameLoop(SCREEN_WIDTH_START, SCREEN_HEIGHT_START, GAME_TITLE, FPS)
    game.run()

if __name__ == "__main__": 
    start()