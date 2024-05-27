#Crie um programa que abra e reproduza um áudio de um arquivo MP3
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("Audiodisc.mp3")
pygame.mixer.music.play()
pygame.event.wait()
