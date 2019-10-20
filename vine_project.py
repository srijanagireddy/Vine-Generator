# Write your code here :-)
import pygame
import random
from gpiozero import Button
pygame.init()


vineList = []
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/adam_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/freshavocado_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/life_lemons_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/road_work_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/wednesday_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/country_boi_i_love_you_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/hi_my_name_is_trey_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/hi_welcome_to_chilis_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/i_couldve_dropped_my_croissant_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/i_smell_like_beef_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/is_that_a_weed_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/its_an_avocado_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/look_at_all_those_chickens_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/merry_chrysler_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/more_like_hurricane_tortilla_vine.wav"))
vineList.append(pygame.mixer.Sound("/home/pi/vine-audio-project/recordings/why_you_always_lyin_vine.wav"))
check = True
while True:
    if Button(7).is_pressed:
        print("it works")


