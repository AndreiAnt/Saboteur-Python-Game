import pygame
import sys
import random
import os

# Inițializare Pygame
pygame.init()

# Setare dimensiune fereastră
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
#screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Titlu fereastră
pygame.display.set_caption("Saboteur - The Board Game")

# Încărcare imagini necesare
title_image = pygame.image.load('Saboteur_Logo.jpg')
title_image = pygame.transform.scale(title_image, (screen_width, screen_height))

background_image = pygame.image.load('BackGround_Players_Number.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

stone_background = pygame.image.load('Stone_Background.png')
stone_background = pygame.transform.scale(stone_background, (200, 150))  # Dimensiunea pentru pop-up
stone_background_rect = stone_background.get_rect(topleft=(0, 0))

# Săgeți pentru navigație
arrow_size = 70
arrow_up = pygame.transform.scale(pygame.image.load('Arrow_Up.png'),(arrow_size, arrow_size))
arrow_down = pygame.transform.scale(pygame.image.load('Arrow_Down.png'),(arrow_size, arrow_size))
arrow_right = pygame.transform.scale(pygame.image.load('Arrow_Right.png'),(arrow_size, arrow_size))
arrow_left2 = pygame.transform.scale(pygame.image.load('Arrow_Left.png'),(arrow_size, arrow_size))

# Poziționare săgeți
same_up_down = 100
same_left_right = 320

up_y = same_left_right - 50
down_y = up_y + 100
right_x = 55
left_x = right_x + 90

arrow_up_rect = arrow_up.get_rect(topleft=(same_up_down, up_y))
arrow_down_rect = arrow_down.get_rect(topleft=(same_up_down, down_y))
arrow_right_rect = arrow_right.get_rect(topleft=(left_x, same_left_right))
arrow_left_rect2 = arrow_left2.get_rect(topleft=(right_x, same_left_right))


#Sageti navigatie carti jucator
arrow_size2 = 40
arrow_right3 = pygame.transform.scale(pygame.image.load('Arrow_Right.png'),(arrow_size2, arrow_size2))
arrow_left3 = pygame.transform.scale(pygame.image.load('Arrow_Left.png'),(arrow_size2, arrow_size2))

# Poziționare săgeți navigatie carti jucator
arrow_left_x = 145
arrow_right_x = arrow_left_x + 50
arrow_left_y = 535
arrow_right_y = arrow_left_y

arrow_right_rect3 = arrow_right3.get_rect(topleft=(arrow_right_x, arrow_right_y))
arrow_left_rect3 = arrow_left3.get_rect(topleft=(arrow_left_x, arrow_left_y))


#Imagine de ales o carte din tabla de joc
width_boardgame = 160
height_boardgame = 85
select_image_boardgame = pygame.transform.scale(pygame.image.load('Choose_A_Card_From_The_Table.png'), (width_boardgame, height_boardgame))

#Imagine de ales carte din mana jucatorului
width_hand = 160
height_hand = 85
select_image_hand = pygame.transform.scale(pygame.image.load('Choose_A_Card.png'), (width_hand, height_hand))

#Imagine dreptunghi gri
width_grey_rect = 250
height_grey_rect = 180
grey_rect = pygame.transform.scale(pygame.image.load('Grey_Rectangle_Background.png'), (width_grey_rect, height_grey_rect))


#Imagine pentru rotire
width_rotate = 50
height_rotate = 50
rotate_image = pygame.transform.scale(pygame.image.load('Rotate.png'), (width_rotate, height_rotate))

#Poziționare imagine pentru rotire
rotate_x = 165
rotate_y = 590
rotate_image_rect = rotate_image.get_rect(topleft=(rotate_x, rotate_y))

#Imagine pentru confirmare
width_confirm = 55
height_confirm = 55
confirm_image = pygame.transform.scale(pygame.image.load('Confirm_OG.png'), (width_confirm, height_confirm))

#Poziționare imagine pentru confirmare
confirm_x = 163
confirm_y = 650
confirm_image_rect = confirm_image.get_rect(topleft=(confirm_x, confirm_y))

#imagine de Tras Carte
width_draw = 80
height_draw = 100
draw_image = pygame.transform.scale(pygame.image.load('Backside_Blue_Road.png'), (width_draw, height_draw))

#Poziționare imagine pentru tragere carte
draw_x = 1080
draw_y = 170
draw_image_rect = draw_image.get_rect(topleft=(draw_x, draw_y))

#Imagine de sters carte
width_delete = 80
height_delete = 100
delete_image = pygame.transform.scale(pygame.image.load('Backside_Delete_Road.png'), (width_delete, height_delete))

#Poziționare imagine pentru stergere carte
delete_x = 1080
delete_y = 270
delete_image_rect = delete_image.get_rect(topleft=(delete_x, delete_y))

#Imagine terminare runda
width_finish = 200
height_finish = 100
finish_image = pygame.transform.scale(pygame.image.load('Finish_Round.png'), (width_finish, height_finish))

#Poziționare imagine pentru terminare runda
finish_x = 1070
finish_y = 600
finish_image_rect = finish_image.get_rect(topleft=(finish_x, finish_y))

# Imagine de selecție
selection_image = pygame.image.load('Backside_Red_Road.png').convert_alpha()
selection_image = pygame.transform.scale(selection_image, (75, 75))  # Dimensiunea trebuie să se potrivească cu cea a cărților din TablaJoc

# Inițializare variabile de poziție pentru selecție
selected_row = 0
selected_col = 0

# Imagine pentru numarul de jucători
number_of_players_image = pygame.image.load('Number_Of_Players.png')
number_of_players_image = pygame.transform.scale(number_of_players_image, (400, 250))  # Ajustează dimensiunile după necesități
number_of_players_rect = number_of_players_image.get_rect(center=(screen_width // 2, screen_height // 2 - 130))

# Imagine pentru Just_Gold
just_gold_image = pygame.image.load('Just_Gold.png')
just_gold_image = pygame.transform.scale(just_gold_image, (70, 70))  # Ajustează dimensiunile după necesități
just_gold_rect = just_gold_image.get_rect(center=(screen_width // 2, screen_height // 2 - 130))

Trophy_x = 150
Trophy_y = 600

Trophy_Width = 300
Trophy_Height = Trophy_Width 

# Imagine pentru Trophy1
trophy_image1 = pygame.image.load('Trophy.png')
trophy_image1 = pygame.transform.scale(trophy_image1, (Trophy_Width, Trophy_Height))  # Ajustează dimensiunile după necesități
trophy_rect1 = trophy_image1.get_rect(center=(Trophy_x, Trophy_y))

# Imagine pentru Trophy2
trophy_image2 = pygame.image.load('Trophy.png')
trophy_image2 = pygame.transform.scale(trophy_image2, (Trophy_Width, Trophy_Height))  # Ajustează dimensiunile după necesități
trophy_rect2 = trophy_image2.get_rect(center=(Trophy_x + 1020, Trophy_y))

# Imagine pentru Trophy3
trophy_image3 = pygame.image.load('Trophy_Saboteur.png')
trophy_image3 = pygame.transform.scale(trophy_image3, (Trophy_Width, Trophy_Height))  # Ajustează dimensiunile după necesități
trophy_rect3 = trophy_image3.get_rect(center=(Trophy_x + 1020, Trophy_y + 600))

# Imagine pentru Trophy4
trophy_image4 = pygame.image.load('Trophy_Saboteur.png')
trophy_image4 = pygame.transform.scale(trophy_image4, (Trophy_Width, Trophy_Height))  # Ajustează dimensiunile după necesități
trophy_rect4 = trophy_image4.get_rect(center=(Trophy_x, Trophy_y + 600))

player_numbers_images = {str(i): pygame.transform.scale(pygame.image.load(f'{i}.png'), (100, 100)) for i in range(1, 11)}
player_numbers_images2 = {str(i): pygame.transform.scale(pygame.image.load(f'{i}.png'), (70, 70)) for i in range(1, 11)}
plus_image = pygame.transform.scale(pygame.image.load('+.png'), (50, 50))
minus_image = pygame.transform.scale(pygame.image.load('-.png'), (50, 50))
arrow_left_image = pygame.transform.scale(pygame.image.load('Arrow_Left.png'), (50, 50))  # Redimensionarea săgeții
arrow_left_rect = arrow_left_image.get_rect(topleft=(20, 20))

menu_image = pygame.transform.scale(pygame.image.load('Menu.png'), (50, 50))
start_button_image = pygame.transform.scale(pygame.image.load('Start.png'), (200, 100))
instructions_button_image = pygame.transform.scale(pygame.image.load('Instructions.png'), (200, 100))

# Redimensionare și poziționare butoane pop-up
home_button_image = pygame.transform.scale(pygame.image.load('Home.png'), (50,60))
cancel_button_image = pygame.transform.scale(pygame.image.load('Cancel.png'), (50, 60))
home_button_rect = home_button_image.get_rect(topleft=(70, stone_background_rect.bottom - 80))
cancel_button_rect = cancel_button_image.get_rect(topleft=(home_button_rect.right + 10, stone_background_rect.bottom - 80))

# Poziționare și redimensionare elemente
plus_rect = plus_image.get_rect(center=(screen_width/2 + 100, screen_height/2))
minus_rect = minus_image.get_rect(center=(screen_width/2 - 100, screen_height/2))
start_button_rect = start_button_image.get_rect(center=(screen_width/2, screen_height/2 + 150))
instructions_button_rect = instructions_button_image.get_rect(center=(screen_width/2, screen_height/2 + 250))
menu_button_rect = menu_image.get_rect(topleft=(screen_width - 1270, 20))  # Poziționat în partea dreaptă sus

#Butonul de pauză
paused_image = pygame.image.load('Paused.png')
paused_image = pygame.transform.scale(paused_image, (300, 200))  # Ajustează la dimensiunea dorită pentru "Paused"
paused_rect = paused_image.get_rect(center=(screen_width // 2, screen_height // 2))

# Inițializare mixer pentru muzică
pygame.mixer.init()
pygame.mixer.music.load('Avatars_Love.mp3')
pygame.mixer.music.play(-1)  # Argumentul -1 va face muzica să fie redată în buclă
pygame.mixer.music.set_volume(0.5)  # Setează volumul inițial la jumătate. Ajustează după preferințe.

# Încărcarea imaginilor pentru sunet
sound_on_image = pygame.image.load('Sound.png')
sound_on_image = pygame.transform.scale(sound_on_image, (50, 50))
sound_off_image = pygame.image.load('Mute.png')
sound_off_image = pygame.transform.scale(sound_off_image, (50, 50))

# Buton pentru controlul sunetului
sound_button_image = sound_on_image  # Începem cu sunetul pornit
sound_button_rect = sound_button_image.get_rect(topleft=(screen_width - 80, 20))
is_sound_on = True

#incarcare imagine pentru al doilea dreptunghi gri
Grey_rect2_x = 1075
Grey_rect2_y = 380
width_grey_rect2 = 200
height_grey_rect2 = 220
grey_rect2 = pygame.transform.scale(pygame.image.load('Grey_Rectangle_Background.png'), (width_grey_rect2, height_grey_rect2))

# Creare matrice TablaJoc cu 7 linii și 11 coloane, inițializată cu 0
TablaJoc = [[0 for _ in range(11)] for _ in range(7)]

# Setarea valorilor specifice pe TablaJoc
TablaJoc[3][1] = 13  # Setează poziția (3,1) cu valoarea 13
TablaJoc[1][9] = 34  # Setează poziția (1,9) cu valoarea 34
TablaJoc[3][9] = 34  # Setează poziția (3,9) cu valoarea 34
TablaJoc[5][9] = 34  # Setează poziția (5,9) cu valoarea 34





# Funcție pentru determinarea numărului de cărți per jucător
def calculate_cards_per_player(num_players):
    if 3 <= num_players <= 5:
        return 6
    elif 6 <= num_players <= 7:
        return 5
    elif 8 <= num_players <= 10:
        return 4
    return 0  # Sau orice alt număr default, dacă este necesar



size = 75  # Dimensiunea fiecărei cărți

large_card_width = 120  # Lățimea cărții mari
large_card_height = 150  # Înălțimea cărții mari

horizontal_offset = 250  # Deplasare la dreapta pentru întreaga matrice
tile_width, tile_height = size, size

# Încărcare imagini pentru valorile din TablaJoc
try:
    card_images = {
        -1: pygame.transform.smoothscale(pygame.image.load('Blank.png'), (size, size)),
        0: pygame.transform.smoothscale(pygame.image.load('Backside_Silver_Road.png'), (size, size)),
        1: pygame.transform.smoothscale(pygame.image.load('Blocked_road_1.png'), (size, size)),
        2: pygame.transform.smoothscale(pygame.image.load('Blocked_road_2.png'), (size, size)),
        3: pygame.transform.smoothscale(pygame.image.load('Blocked_road_3.png'), (size, size)),
        4: pygame.transform.smoothscale(pygame.image.load('Blocked_road_4.png'), (size, size)),
        5: pygame.transform.smoothscale(pygame.image.load('Blocked_road_5.png'), (size, size)),
        6: pygame.transform.smoothscale(pygame.image.load('Blocked_road_6.png'), (size, size)),
        7: pygame.transform.smoothscale(pygame.image.load('Blocked_road_7.png'), (size, size)),
        8: pygame.transform.smoothscale(pygame.image.load('I1_road.png'), (size, size)),
        9: pygame.transform.smoothscale(pygame.image.load('I2_road.png'), (size, size)),
        10: pygame.transform.smoothscale(pygame.image.load('L1_road.png'), (size, size)),
        11: pygame.transform.smoothscale(pygame.image.load('L2_road.png'), (size, size)),
        12: pygame.transform.smoothscale(pygame.image.load('Roundabout.png'), (size, size)),
        13: pygame.transform.smoothscale(pygame.image.load('Stairs.png'), (size, size)),
        14: pygame.transform.smoothscale(pygame.image.load('T1_road.png'), (size, size)),
        15: pygame.transform.smoothscale(pygame.image.load('T2_road.png'), (size, size)),
        16: pygame.transform.smoothscale(pygame.image.load('Unlock_lamp.png'), (size, size)),
        17: pygame.transform.smoothscale(pygame.image.load('Unlock_lamp_minecart.png'), (size, size)),
        18: pygame.transform.smoothscale(pygame.image.load('Unlock_minecart.png'), (size, size)),
        19: pygame.transform.smoothscale(pygame.image.load('Unlock_pickaxe.png'), (size, size)),
        20: pygame.transform.smoothscale(pygame.image.load('Unlock_pickaxe_lamp.png'), (size, size)),
        21: pygame.transform.smoothscale(pygame.image.load('Unlock_pickaxe_minecart.png'), (size, size)),
        22: pygame.transform.smoothscale(pygame.image.load('See_gold.png'), (size, size)),
        23: pygame.transform.smoothscale(pygame.image.load('Block_lamp.png'), (size, size)),
        24: pygame.transform.smoothscale(pygame.image.load('Block_minecart.png'), (size, size)),
        25: pygame.transform.smoothscale(pygame.image.load('Block_pickaxe.png'), (size, size)),
        26: pygame.transform.smoothscale(pygame.image.load('Destroy.png'), (size, size)),
        27: pygame.transform.smoothscale(pygame.image.load('Finish_GOLD.png'), (size, size)),
        28: pygame.transform.smoothscale(pygame.image.load('Finish1.png'), (size, size)),
        29: pygame.transform.smoothscale(pygame.image.load('Finish2.png'), (size, size)),
        30: pygame.transform.smoothscale(pygame.image.load('Saboteur1.png'), (size, size)),
        31: pygame.transform.smoothscale(pygame.image.load('Saboteur2.png'), (size, size)),
        32: pygame.transform.smoothscale(pygame.image.load('Saboteur3.png'), (size, size)),
        33: pygame.transform.smoothscale(pygame.image.load('Saboteur4.png'), (size, size)),
        34: pygame.transform.smoothscale(pygame.image.load('Backside_Bronze_Finish.png'), (size, size)),
        35: pygame.transform.smoothscale(pygame.image.load('Reversed_Blocked_road_3.png'), (size, size)),
        36: pygame.transform.smoothscale(pygame.image.load('Reversed_Blocked_road_4.png'), (size, size)),
        37: pygame.transform.smoothscale(pygame.image.load('Reversed_Blocked_road_5.png'), (size, size)),
        38: pygame.transform.smoothscale(pygame.image.load('Reversed_Blocked_road_7.png'), (size, size)),
        39: pygame.transform.smoothscale(pygame.image.load('Reversed_Finish1.png'), (size, size)),
        40: pygame.transform.smoothscale(pygame.image.load('Reversed_Finish2.png'), (size, size)),
        41: pygame.transform.smoothscale(pygame.image.load('Reversed_L1_road.png'), (size, size)),
        42: pygame.transform.smoothscale(pygame.image.load('Reversed_L2_road.png'), (size, size)),
        43: pygame.transform.smoothscale(pygame.image.load('Reversed_T1_road.png'), (size, size)),
        44: pygame.transform.smoothscale(pygame.image.load('Reversed_T2_road.png'), (size, size)),
        45: pygame.transform.smoothscale(pygame.image.load('Backside_Bronze_Finish_1.png'), (size, size)),
        46: pygame.transform.smoothscale(pygame.image.load('Backside_Bronze_Finish_2.png'), (size, size)),
        47: pygame.transform.smoothscale(pygame.image.load('Backside_Bronze_Finish_3.png'), (size, size)),
        48: pygame.transform.smoothscale(pygame.image.load('Blocked_road_8.png'), (size, size)),
        49: pygame.transform.smoothscale(pygame.image.load('Blocked_road_9.png'), (size, size)),
        50: pygame.transform.smoothscale(pygame.image.load('Reversed_Blocked_road_8.png'), (size, size)),
        51: pygame.transform.smoothscale(pygame.image.load('Reversed_Blocked_road_9.png'), (size, size)),
        52: pygame.transform.smoothscale(pygame.image.load('Dwarf1.png'), (size, size)),
        53: pygame.transform.smoothscale(pygame.image.load('Dwarf2.png'), (size, size)),
        54: pygame.transform.smoothscale(pygame.image.load('Dwarf3.png'), (size, size)),
        55: pygame.transform.smoothscale(pygame.image.load('Dwarf4.png'), (size, size)),
        56: pygame.transform.smoothscale(pygame.image.load('Dwarf5.png'), (size, size)),
        57: pygame.transform.smoothscale(pygame.image.load('Dwarf6.png'), (size, size)),
        58: pygame.transform.smoothscale(pygame.image.load('Dwarf7.png'), (size, size))
    }
except Exception as e:
    print(f"Failed to load images: {e}")
    sys.exit(1)



#AllTheCards = [
    #1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11,
    #12, 12, 12, 12, 12, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 17, 18, 18, 
    #19, 19, 20, 21, 22, 22, 22, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25, 
    #26, 26, 26, 48, 49
#]

AllTheCards = [
    1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11,
    12, 12, 12, 12, 12, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 17, 18, 18, 
    19, 19, 20, 21, 22, 22, 22, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25, 
    48, 49
]

random.shuffle(AllTheCards)

CurrentPlayer = 1
number_of_players = 3

#Imagine pentru cărțile jucătorilor verde
transparent_card_image = pygame.image.load('Backside_Green_Transparent_Road.png').convert_alpha()
transparent_card_image = pygame.transform.scale(transparent_card_image, (large_card_width, large_card_height))

selected_card_index = 0  

selected_card_display_x = 15  # Poziție X pentru cartea selectată, spre marginea dreaptă a ecranului
selected_card_display_y = 550  # Poziție Y pentru cartea selectată

index_RestulPachetului = 0

# Încărcare imagini pentru fiecare jucător
player_images = {i: pygame.image.load(f'Player{i}.png') for i in range(1, 11)}
for i, img in player_images.items():
    player_images[i] = pygame.transform.scale(img, (130, 100))  # Redimensionare imagine

player_images2 = {i: pygame.image.load(f'Player{i}.png') for i in range(1, 11)}
for i, img in player_images2.items():
    player_images2[i] = pygame.transform.scale(img, (130, 100))  # Redimensionare imagine

# Încărcare imagini pentru schimbarea jucătorilor
player_switch_images = {i: pygame.image.load(f'Play_As_Player{i}.png') for i in range(1, 11)}
for i, img in player_switch_images.items():
    player_switch_images[i] = pygame.transform.scale(img, (200, 100))

# Încărcare imagini pentru cărțile extra
bonus_card_values = {16, 17, 18, 19, 20, 21, 23, 24, 25}


finish_1_image = pygame.image.load('Finish_1.png')
finish_1_image = pygame.transform.scale(finish_1_image, (150, 80))  # Ajustează dimensiunile după necesități
finish_1_rect = finish_1_image.get_rect(center=(635, 600))  # Ajustează poziția după necesități

finish_2_image = pygame.image.load('Finish_Aur.png')
finish_2_image = pygame.transform.scale(finish_2_image, (150, 80))  # Ajustează dimensiunile după necesități
finish_2_rect = finish_2_image.get_rect(center=(635, 600))  # Ajustează poziția după necesități

block_unblock_image = pygame.image.load('Block_Unblock.png')
block_unblock_image = pygame.transform.scale(block_unblock_image, (250, 125))  # Ajustează dimensiunile după necesități
block_unblock_rect = block_unblock_image.get_rect(center=(635, 100))  # Ajustează poziția după necesități

# Încărcare imagini pentru cărțile bonus
Aici_Width = 110
Aici_Height = 55
Aici_y = 525
Aici_x = 75

#imagine pentru Aici1
aici1_image = pygame.image.load('Aici1.png')
aici1_image = pygame.transform.scale(aici1_image, (Aici_Width, Aici_Height))  # Ajustează dimensiunile după necesități
aici1_rect = aici1_image.get_rect(center=(Aici_x, Aici_y))  # Ajustează poziția după necesități

#imagine pentru Aici2
aici2_image = pygame.image.load('Aici2.png')
aici2_image = pygame.transform.scale(aici2_image, (Aici_Width, Aici_Height))  # Ajustează dimensiunile după necesități
aici2_rect = aici2_image.get_rect(center=(Aici_x + 125, Aici_y))  # Ajustează poziția după necesități

#imagine pentru Aici3
aici3_image = pygame.image.load('Aici3.png')
aici3_image = pygame.transform.scale(aici3_image, (Aici_Width, Aici_Height))  # Ajustează dimensiunile după necesități
aici3_rect = aici3_image.get_rect(center=(Aici_x + 250, Aici_y))  # Ajustează poziția după necesități

#imagine pentru Aici4
aici4_image = pygame.image.load('Aici4.png')
aici4_image = pygame.transform.scale(aici4_image, (Aici_Width, Aici_Height))  # Ajustează dimensiunile după necesități
aici4_rect = aici4_image.get_rect(center=(Aici_x + 375, Aici_y))  # Ajustează poziția după necesități

#imagine pentru Aici5
aici5_image = pygame.image.load('Aici5.png')
aici5_image = pygame.transform.scale(aici5_image, (Aici_Width, Aici_Height))  # Ajustează dimensiunile după necesități
aici5_rect = aici5_image.get_rect(center=(Aici_x + 500, Aici_y))  # Ajustează poziția după necesități

#imagine pentru Aici6
aici6_image = pygame.image.load('Aici6.png')
aici6_image = pygame.transform.scale(aici6_image, (Aici_Width, Aici_Height))  # Ajustează dimensiunile după necesități
aici6_rect = aici6_image.get_rect(center=(Aici_x + 625, Aici_y))  # Ajustează poziția după necesități

#imagine pentru Aici7
aici7_image = pygame.image.load('Aici7.png')
aici7_image = pygame.transform.scale(aici7_image, (Aici_Width, Aici_Height))  # Ajustează dimensiunile după necesități
aici7_rect = aici7_image.get_rect(center=(Aici_x + 750, Aici_y))  # Ajustează poziția după necesități

#imagine pentru Aici8
aici8_image = pygame.image.load('Aici8.png')
aici8_image = pygame.transform.scale(aici8_image, (Aici_Width, Aici_Height))  # Ajustează dimensiunile după necesități
aici8_rect = aici8_image.get_rect(center=(Aici_x + 875, Aici_y))  # Ajustează poziția după necesități

#imagine pentru Aici9
aici9_image = pygame.image.load('Aici9.png')
aici9_image = pygame.transform.scale(aici9_image, (Aici_Width, Aici_Height))  # Ajustează dimensiunile după necesități
aici9_rect = aici9_image.get_rect(center=(Aici_x + 1000, Aici_y))  # Ajustează poziția după necesități

#imagine pentru Aici10
aici10_image = pygame.image.load('Aici10.png')
aici10_image = pygame.transform.scale(aici10_image, (Aici_Width, Aici_Height))  # Ajustează dimensiunile după necesități
aici10_rect = aici10_image.get_rect(center=(Aici_x + 1125, Aici_y))  # Ajustează poziția după necesități

#imagine pentru cartile de blocare
blocked_road_1_image = pygame.image.load('BlockingCards.png')
blocked_road_1_image = pygame.transform.scale(blocked_road_1_image, (130, 200))  # Ajustează dimensiunile după necesități
blocked_road_1_rect = blocked_road_1_image.get_rect(center=(1140, 490))  # Ajustează poziția după necesități

#imagine pentru press and hold
press_and_hold_image = pygame.image.load('PressAndHold.png')
press_and_hold_image = pygame.transform.scale(press_and_hold_image, (300, 200))  # Ajustează dimensiunile după necesități
press_and_hold_rect = press_and_hold_image.get_rect(center=(1080, 290))  # Ajustează poziția după necesități

allowed_values = {23, 24, 25}

BlockMatrix = [[0 for _ in range(3)] for _ in range(number_of_players)]

# Inițializare vector WhereIsTheGold
WhereIsTheGold = [27, 28, 29]
random.shuffle(WhereIsTheGold)

# Inițializare matrice FindTheGold cu 7 rânduri și 3 coloane
FindTheGold = [[0 for _ in range(3)] for _ in range(7)]

# Setarea valorilor specifice în matricea FindTheGold
FindTheGold[1][1] = 45
FindTheGold[3][1] = 46
FindTheGold[5][1] = 47

Aur_x = 800
Aur_y = 160

Aur_Width = 110
Aur_Height = 75

#imagine pentru Aur1
Aur1_image = pygame.image.load('Aur1.png')
Aur1_image = pygame.transform.scale(Aur1_image, (Aur_Width, Aur_Height))  # Ajustează dimensiunile după necesități
Aur1_rect = Aur1_image.get_rect(center=(Aur_x, Aur_y))  # Ajustează poziția după necesități

#imagine pentru Aur2
Aur2_image = pygame.image.load('Aur2.png')
Aur2_image = pygame.transform.scale(Aur2_image, (Aur_Width, Aur_Height))  # Ajustează dimensiunile după necesități
Aur2_rect = Aur2_image.get_rect(center=(Aur_x, Aur_y + 130))  # Ajustează poziția după necesități

#imagine pentru Aur3
Aur3_image = pygame.image.load('Aur3.png')
Aur3_image = pygame.transform.scale(Aur3_image, (Aur_Width, Aur_Height))  # Ajustează dimensiunile după necesități
Aur3_rect = Aur3_image.get_rect(center=(Aur_x, Aur_y + 260))  # Ajustează poziția după necesități

#imagine pentru rol
role1_image = pygame.image.load('Role.png')
role1_image = pygame.transform.scale(role1_image, (100, 50))  # Ajustează dimensiunile după necesități
role1_rect = role1_image.get_rect(center=(1136, 25))  # Ajustează poziția după necesități

#imagine pentru add_card
add_card_image = pygame.image.load('AddCard.png')
add_card_image = pygame.transform.scale(add_card_image, (100, 50))  # Ajustează dimensiunile după necesități
add_card_rect = add_card_image.get_rect(center=(1220, 220))  # Ajustează poziția după necesități

#imagine pentru drop_card
drop_card_image = pygame.image.load('DropCard.png')
drop_card_image = pygame.transform.scale(drop_card_image, (100, 50))  # Ajustează dimensiunile după necesități
drop_card_rect = drop_card_image.get_rect(center=(1220, 315))  # Ajustează poziția după necesități

#imagine pentru WIN
win_image = pygame.image.load('WIN.png')
win_image = pygame.transform.scale(win_image, (50, 50))  # Ajustează dimensiunile după necesități
win_rect = win_image.get_rect(topleft=(screen_width - 80, 90))  # Ajustează poziția după necesități




#imagine pentru DwarfWin
dwarf_win_image = pygame.image.load('DwarfWin.png')
dwarf_win_image = pygame.transform.scale(dwarf_win_image, (400, 200))  # Ajustează dimensiunile după necesități
dwarf_win_rect = dwarf_win_image.get_rect(topleft=(450, 500))  # Ajustează poziția după necesități

#imagine pentru SaboteurWin
saboteur_win_image = pygame.image.load('SaboteursWin.png')
saboteur_win_image = pygame.transform.scale(saboteur_win_image, (400, 200))  # Ajustează dimensiunile după necesități
saboteur_win_rect = saboteur_win_image.get_rect(topleft=(450, 500))  # Ajustează poziția după necesități

lista =["0", "0011", "1100", "0001", "0101", "0100", "1111", "0110", "0011", "1100", "1010", "1001", "1111", "1111", "1110", "1011", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0010", "1010", "1000", "1001", "0", "0", "0101", "0110", "1101", "0111", "0", "0", "0", "1011", "1110", "0111", "1101"]
sus_gol = [1, 3, 8, 10, 11, 15, 35, 36, 37, 38, 48, 39, 40, 0, 34]
sus_plin = [2, 4, 5, 6, 7, 9, 12, 13, 14, 41, 42, 43, 44, 49, 50, 51, 27, 28, 29, 0, 34]

jos_gol = [1, 3, 4, 5, 7, 8, 35, 41, 42, 44, 50, 28, 29, 0, 34]
jos_plin = [2, 6, 9, 10, 11, 12, 13, 14, 15, 36, 37, 38, 43, 48, 49, 51, 27, 39, 40, 0, 34]

dreapta_gol = [2, 5, 7, 9, 10, 14, 35, 36, 37, 42, 49, 28, 40, 0, 34]
dreapta_plin = [1, 3, 4, 6, 8, 11, 12, 13, 15, 38, 41, 43, 44, 48, 50, 51, 27, 29, 39, 0, 34]

stanga_gol = [2, 3, 4, 5, 9, 11, 37, 38, 41, 43, 51, 29, 39, 0, 34]
stanga_plin = [1, 6, 7, 8, 10, 12, 13, 14, 15, 35, 36, 42, 44, 48, 49, 50, 27, 28, 40, 0, 34]

Blocked_raods =[1, 2, 3, 4, 5, 6, 7, 35, 36, 37, 38, 48, 49, 50, 51]

Finish_up = [9, 12, 14, 41, 42, 43, 44]
Finish_down = [9, 10, 11, 12, 14, 15, 43]
Finish_right = [8, 11, 12, 15, 41, 43, 44]
Finish_left = [8, 10, 12, 14, 15, 42, 44]

galetusa_aur = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
random.shuffle(galetusa_aur)
aux = 0
amesteca = False
deschis = False

# Stări pentru ecran și pop-up
state = "MAIN_MENU"
popup = False  # Control pentru afișarea pop-up-ului

# Variabila pentru control buclă principală
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if state == "GASESTE_AURUL":
                AllTheCards[(CurrentPlayer - 1) * 6 + selected_card_index] = -1

            if state == "BonusCards":
                if selected_card_value in allowed_values:
                    # Implementarea acțiunilor pentru butoanele "Aici"
                    aici_buttons = [aici1_rect, aici2_rect, aici3_rect, aici4_rect, aici5_rect,
                                    aici6_rect, aici7_rect, aici8_rect, aici9_rect, aici10_rect]
                    for index, aici_button in enumerate(aici_buttons):
                        if aici_button.collidepoint(event.pos):

                            if selected_card_value in bonus_card_values:
                                row = BlockMatrix[index]
                                # Verificăm și aplicăm regulile specifice pentru fiecare tip de carte
                                modified = False
                                if selected_card_value in {16, 17, 20} and 23 in row:
                                    row[row.index(23)] = 0
                                    modified = True
                                if selected_card_value in {18, 17, 21} and 24 in row:
                                    row[row.index(24)] = 0
                                    modified = True
                                if selected_card_value in {19, 20, 21} and 25 in row:
                                    row[row.index(25)] = 0
                                    modified = True
                                # După modificare, cartea este eliminată din mâna jucătorului
                                if modified:
                                    AllTheCards[(CurrentPlayer - 1) * 6 + selected_card_index] = -1
                                    break

                            # Adaugă valoarea în prima poziție liberă pe linia corespunzătoare
                            for i, val in enumerate(BlockMatrix[index]):
                                if val == 0:
                                    BlockMatrix[index][i] = selected_card_value
                                    AllTheCards[(CurrentPlayer - 1) * 6 + selected_card_index] = -1
                                    break
                            break  # Oprește bucla după ce o valoare a fost adăugată
                else:
                     # Obține cartea curent selectată pentru a verifica acțiunile speciale
                    selected_card_value = CartiJucatori[CurrentPlayer - 1][selected_card_index]

                    aici_buttons = [aici1_rect, aici2_rect, aici3_rect, aici4_rect, aici5_rect,
                                    aici6_rect, aici7_rect, aici8_rect, aici9_rect, aici10_rect]
                    for index, aici_button in enumerate(aici_buttons):
                        if aici_button.collidepoint(event.pos):
                            # Verifică dacă cartea selectată poate interacționa cu blocările
                            if selected_card_value in bonus_card_values:
                                row = BlockMatrix[index]
                                # Verificăm și aplicăm regulile specifice pentru fiecare tip de carte
                                modified = False
                                if selected_card_value in {16, 17, 20} and 23 in row:
                                    row[row.index(23)] = 0
                                    modified = True
                                if selected_card_value in {18, 17, 21} and 24 in row:
                                    row[row.index(24)] = 0
                                    modified = True
                                if selected_card_value in {19, 20, 21} and 25 in row:
                                    row[row.index(25)] = 0
                                    modified = True
                                # După modificare, cartea este eliminată din mâna jucătorului
                                if modified:
                                    AllTheCards[(CurrentPlayer - 1) * 6 + selected_card_index] = -1
                                    break           
                            


            # Verifică dacă cartea selectată are o funcție specială
            if state == "GAME_SCREEN" and len(CartiJucatori[CurrentPlayer - 1]) > selected_card_index:
                selected_card = CartiJucatori[CurrentPlayer - 1][selected_card_index]
                if confirm_image_rect.collidepoint(event.pos) and selected_card in bonus_card_values:
                    state = "BonusCards"
                    continue  # Sari peste alte verificări și actualizări

            if state == "PLAYER_SWITCH":
                # Verificăm dacă click-ul a fost pe butonul Play_As_Player
                if player_button_rect.collidepoint(event.pos):
                    state = "GAME_SCREEN"
                    continue

            if state == "GASESTE_AURUL":
                if Aur1_rect.collidepoint(event.pos):
                        state = "GASESTE_AURUL1"

                if Aur2_rect.collidepoint(event.pos):
                    state = "GASESTE_AURUL2"
                    
                if Aur3_rect.collidepoint(event.pos):
                    state = "GASESTE_AURUL3"


            if finish_image_rect.collidepoint(event.pos):
                CurrentPlayer += 1
                if CurrentPlayer > number_of_players:
                    CurrentPlayer = 1
                state = "PLAYER_SWITCH"

            if win_rect.collidepoint(event.pos):
                state = "WIN_Saboteur"

            
            

            if draw_image_rect.collidepoint(event.pos) and state == "GAME_SCREEN":
                # Verifică dacă există cărți rămase în pachet
                if(index_RestulPachetului < len(RestulPachetului)):
                    for i in range(len(CartiJucatori[CurrentPlayer - 1])):
                        if CartiJucatori[CurrentPlayer - 1][i] == -1:
                            AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = RestulPachetului[index_RestulPachetului]
                            index_RestulPachetului += 1
                            break
                    

            if delete_image_rect.collidepoint(event.pos) and state == "GAME_SCREEN":
                # Verifică dacă există cărți în mâna jucătorului
                if len(CartiJucatori[CurrentPlayer - 1]) > 0 and selected_card_index < len(CartiJucatori[0]):
                    # Elimină cartea selectată din lista de cărți ale jucătorului
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = -1
                    # Ajustează indexul selectat pentru a evita erori de indexare
                    selected_card_index = max(0, min(selected_card_index, len(CartiJucatori[CurrentPlayer - 1]) - 1))

            if rotate_image_rect.collidepoint(event.pos) and state == "GAME_SCREEN":
                if CartiJucatori[CurrentPlayer - 1][selected_card_index] == 3:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 35
                
                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 4:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 36
                
                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 5:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 37

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 7:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 38

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 28:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 39
                
                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 29:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 40

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 10:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 41

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 11:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 42

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 14:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 43

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 15:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 44

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 35:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 3
                
                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 36:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 4
                
                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 37:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 5
                
                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 38:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 7
                
                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 39:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 28
                
                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 40:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 29

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 41:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 10

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 42:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 11

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 43:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 14

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 44:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 15

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 48:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 50

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 50:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 48

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 49:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 51

                elif CartiJucatori[CurrentPlayer - 1][selected_card_index] == 51:
                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = 49

            if confirm_image_rect.collidepoint(event.pos) and state == "GAME_SCREEN":
                try:
                    selected_card = CartiJucatori[CurrentPlayer - 1][selected_card_index]
                    print(f"Card selected: {selected_card}")

                    if selected_card == 22:
                        state = "GASESTE_AURUL"



                    #if selected_card == 26:
                        #if (selected_row, selected_col) not in [(3, 1), (1, 9), (3, 9), (5, 9)]:
                            #TablaJoc[selected_row][selected_col] = 0
                            #AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = -1

                    
                    
                    
                    # Verifică dacă cartea selectată este una specială și necesită tranziția la starea BonusCards
                    if selected_card in bonus_card_values:
                        print("Switching to BonusCards state due to special card selection.")
                        state = "BonusCards"
                        continue  # Sari peste alte verificări și actualizări

                    # Verifică dacă există blocări active pentru jucătorul curent
                    if any(value != 0 for value in BlockMatrix[CurrentPlayer - 1]):
                        print("Cannot place card due to an active block.")
                    else:
                        string_valori = lista[selected_card]
                        if len(string_valori) >= 4:
                            numar_up = int(string_valori[0])   # Convertim primul caracter în întreg și îl salvăm în numar_up
                            numar_down = int(string_valori[1]) # Convertim al doilea caracter în întreg și îl salvăm în numar_down
                            numar_right = int(string_valori[2])# Convertim al treilea caracter în întreg și îl salvăm în numar_right
                            numar_left = int(string_valori[3]) # Convertim al patrulea caracter în întreg și îl salvăm în numar_left

                            ok_sus = False
                            ok_jos = False
                            ok_dreapta = False
                            ok_stanga = False
                            
                            ok_final = False


                            if numar_up == 0:
                                if selected_row == 0:
                                    ok_sus = True
                                if TablaJoc[selected_row - 1][selected_col] in sus_gol:
                                    ok_sus = True
                                
                            if numar_up == 1:
                                if selected_row == 0:
                                    ok_sus = True
                                if TablaJoc[selected_row - 1][selected_col] in sus_plin:
                                    ok_sus = True
                            
                            if numar_down == 0:
                                if selected_row == 6:
                                    ok_jos = True
                                if TablaJoc[selected_row + 1][selected_col] in jos_gol:
                                    ok_jos = True

                            if numar_down == 1:
                                if selected_row == 6:
                                    ok_jos = True
                                if TablaJoc[selected_row + 1][selected_col] in jos_plin:
                                    ok_jos = True
                            
                            if numar_right == 0:
                                if selected_col == 10:
                                    ok_dreapta = True
                                if TablaJoc[selected_row][selected_col + 1] in dreapta_gol:
                                    ok_dreapta = True
                            
                            if numar_right == 1:
                                if selected_col == 10:
                                    ok_dreapta = True
                                if TablaJoc[selected_row][selected_col + 1] in dreapta_plin:
                                    ok_dreapta = True

                            if numar_left == 0:
                                if selected_col == 0:
                                    ok_stanga = True
                                if TablaJoc[selected_row][selected_col - 1] in stanga_gol:
                                    ok_stanga = True

                            if numar_left == 1:
                                if selected_col == 0:
                                    ok_stanga = True
                                if TablaJoc[selected_row][selected_col - 1] in stanga_plin:
                                    ok_stanga = True
                                
                                    
                            if ok_sus == True and ok_jos == True and ok_dreapta == True and ok_stanga == True:
                                ok_final = True

                        # Continuă cu logica normală de confirmare dacă nu este o carte specială și nu există blocări
                        if (selected_row, selected_col) not in [(3, 1), (1, 9), (3, 9), (5, 9)] and ok_final == True:
                            if not((TablaJoc[selected_row - 1][selected_col] == 0 or TablaJoc[selected_row - 1][selected_col] == 34 or selected_row == 0) and (TablaJoc[selected_row + 1][selected_col] == 0 or TablaJoc[selected_row + 1][selected_col] == 34 or selected_row == 6) and (TablaJoc[selected_row][selected_col - 1] == 0 or TablaJoc[selected_row][selected_col - 1] == 34 or selected_col == 0) and (TablaJoc[selected_row][selected_col + 1] == 0 or TablaJoc[selected_row][selected_col + 1] == 34 or selected_col == 10)):
                                if selected_card not in [0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, -1]:
                                    TablaJoc[selected_row][selected_col] = selected_card
                                    AllTheCards[(CurrentPlayer - 1)*6 + selected_card_index] = -1
                                    print("Card placed on the board and removed from player's hand.")
                                    if (TablaJoc[selected_row - 1][selected_col] == 34 or TablaJoc[selected_row + 1][selected_col] == 34 or TablaJoc[selected_row][selected_col - 1] == 34 or TablaJoc[selected_row][selected_col + 1] == 34) and (TablaJoc[selected_row][selected_col] not in Blocked_raods):
                                        if selected_row == 1:
                                            if selected_col == 8:
                                                if TablaJoc[1][8] in Finish_left and TablaJoc[1][9] == 34:
                                                    if WhereIsTheGold[0] == 27:
                                                        state = "WIN"
                                                    if WhereIsTheGold[0] == 28:
                                                        TablaJoc[1][9] = 39
                                                    if WhereIsTheGold[0] == 29:
                                                        TablaJoc[1][9] = 29
                                            
                                            if selected_col == 10:
                                                if TablaJoc[1][10] in Finish_right and TablaJoc[1][9] == 34:
                                                    if WhereIsTheGold[0] == 27:
                                                        state = "WIN"
                                                    if WhereIsTheGold[0] == 29:
                                                        TablaJoc[1][9] = 40
                                                    if WhereIsTheGold[0] == 28:
                                                        TablaJoc[1][9] = 28
                    
                                        if selected_row == 0:
                                            if selected_col == 9:
                                                if TablaJoc[0][9] in Finish_up and TablaJoc[1][9] == 34:
                                                    if WhereIsTheGold[0] == 27:
                                                        TablaJoc[1][9] = 27
                                                        state = "WIN"
                                                    if WhereIsTheGold[0] == 28:
                                                        TablaJoc[1][9] = 39
                                                    if WhereIsTheGold[0] == 29:
                                                        TablaJoc[1][9] = 40

                                        if selected_row == 2:
                                            if selected_col == 9:
                                                if TablaJoc[2][9] in Finish_down and TablaJoc[1][9] == 34:
                                                    if WhereIsTheGold[0] == 27:
                                                        TablaJoc[1][9] = 27
                                                        state = "WIN"
                                                    if WhereIsTheGold[0] == 28:
                                                        TablaJoc[1][9] = 28
                                                    if WhereIsTheGold[0] == 29:
                                                        TablaJoc[1][9] = 29
                                                if TablaJoc[2][9] in Finish_up and TablaJoc[3][9] == 34:
                                                    if WhereIsTheGold[1] == 27:
                                                        TablaJoc[3][9] = 27
                                                        state = "WIN"
                                                    if WhereIsTheGold[0] == 28:
                                                        TablaJoc[3][9] = 39
                                                    if WhereIsTheGold[0] == 29:
                                                        TablaJoc[3][9] = 40
                                        
                                        if selected_row == 3:
                                            if selected_col == 8:
                                                if TablaJoc[3][8] in Finish_left and TablaJoc[3][9] == 34:
                                                    if WhereIsTheGold[1] == 27:
                                                        TablaJoc[3][9] = 27
                                                        state = "WIN"
                                                    if WhereIsTheGold[1] == 28:
                                                        TablaJoc[3][9] = 39
                                                    if WhereIsTheGold[1] == 29:
                                                        TablaJoc[3][9] = 29

                                            if selected_col == 10:
                                                if TablaJoc[3][10] in Finish_right and TablaJoc[3][9] == 34:
                                                    if WhereIsTheGold[1] == 27:
                                                        TablaJoc[3][9] = 27
                                                        state = "WIN"
                                                    if WhereIsTheGold[1] == 29:
                                                        TablaJoc[3][9] = 40
                                                    if WhereIsTheGold[1] == 28:
                                                        TablaJoc[3][9] = 28

                                        if selected_row == 4:
                                            if selected_col == 9:
                                                if TablaJoc[4][9] in Finish_down and TablaJoc[3][9] == 34:
                                                    if WhereIsTheGold[1] == 27:
                                                        TablaJoc[3][9] = 27
                                                        state = "WIN"
                                                    if WhereIsTheGold[1] == 28:
                                                        TablaJoc[3][9] = 28
                                                    if WhereIsTheGold[1] == 29:
                                                        TablaJoc[3][9] = 29

                                                if TablaJoc[4][9] in Finish_up and TablaJoc[5][9] == 34:
                                                    if WhereIsTheGold[2] == 27:
                                                        TablaJoc[5][9] = 27
                                                        state = "WIN"
                                                    if WhereIsTheGold[2] == 28:
                                                        TablaJoc[5][9] = 39

                                                    if WhereIsTheGold[2] == 29:
                                                        TablaJoc[5][9] = 40
                                        
                                        if selected_row == 5:
                                            if selected_col == 8:
                                                if TablaJoc[5][8] in Finish_left and TablaJoc[5][9] == 34:
                                                    if WhereIsTheGold[2] == 27:
                                                        TablaJoc[5][9] = 27
                                                        state = "WIN"
                                                    if WhereIsTheGold[2] == 28:
                                                        TablaJoc[5][9] = 39
                                                    if WhereIsTheGold[2] == 29:
                                                        TablaJoc[5][9] = 29

                                            if selected_col == 10:
                                                if TablaJoc[5][10] in Finish_right and TablaJoc[5][9] == 34:
                                                    if WhereIsTheGold[2] == 27:
                                                        TablaJoc[5][9] = 27
                                                        state = "WIN"
                                                    if WhereIsTheGold[2] == 29:
                                                        TablaJoc[5][9] = 40
                                                    if WhereIsTheGold[2] == 28:
                                                        TablaJoc[5][9] = 28

                                        if selected_row == 6:
                                            if selected_col == 9:
                                                if TablaJoc[6][9] in Finish_down and TablaJoc[5][9] == 34:
                                                    if WhereIsTheGold[2] == 27:
                                                        TablaJoc[5][9] = 27
                                                        state = "WIN"
                                                    if WhereIsTheGold[2] == 28:
                                                        TablaJoc[5][9] = 28
                                                    if WhereIsTheGold[2] == 29:
                                                        TablaJoc[5][9] = 29
                except Exception as e:
                    print(f"An error occurred during card confirmation: {e}")

            
            


            if arrow_right_rect3.collidepoint(event.pos) and state == "GAME_SCREEN":
                selected_card_index = min(len(CartiJucatori[CurrentPlayer - 1]) - 1, selected_card_index + 1)  
            if arrow_left_rect3.collidepoint(event.pos) and state == "GAME_SCREEN":
                selected_card_index = max(0, selected_card_index - 1)  

            if arrow_up_rect.collidepoint(event.pos) and state == "GAME_SCREEN":
                selected_row = max(0, selected_row - 1)
            if arrow_down_rect.collidepoint(event.pos) and state == "GAME_SCREEN":
                selected_row = min(6, selected_row + 1)
            if arrow_left_rect2.collidepoint(event.pos) and state == "GAME_SCREEN":
                selected_col = max(0, selected_col - 1)
            if arrow_right_rect.collidepoint(event.pos) and state == "GAME_SCREEN":
                selected_col = min(10, selected_col + 1)

            if sound_button_rect.collidepoint(event.pos):
                # Schimbă starea sunetului
                is_sound_on = not is_sound_on
                if is_sound_on:
                    pygame.mixer.music.unpause()
                    sound_button_image = sound_on_image
                else:
                    pygame.mixer.music.pause()
                    sound_button_image = sound_off_image

            if popup:
                if home_button_rect.collidepoint(event.pos):
                    running = False

                elif cancel_button_rect.collidepoint(event.pos):
                    popup = False

            elif state == "GAME_SCREEN":
                if menu_button_rect.collidepoint(event.pos):
                    popup = not popup  # Afișează sau ascunde pop-up-ul
            elif state == "PLAYER_SELECTION":
                if plus_rect.collidepoint(event.pos) and number_of_players < 10:
                    number_of_players += 1# Crește numărul de jucători

                    

                    BlockMatrix = [[0 for _ in range(3)] for _ in range(number_of_players)]
                    NumarCartiJucatori = calculate_cards_per_player(number_of_players)

                elif minus_rect.collidepoint(event.pos) and number_of_players > 3:
                    number_of_players -= 1#scade numarul de jucatori

                   

                    BlockMatrix = [[0 for _ in range(3)] for _ in range(number_of_players)]
                    NumarCartiJucatori = calculate_cards_per_player(number_of_players)

                elif start_button_rect.collidepoint(event.pos):
                    try:

                        Aur_Cautatori = [None] * (number_of_players - 1)
                        if number_of_players == 3:
                            Rol_Jucatori = [52, 53, 30]
                            Aur_Sabotori = 4
                            for i in range(0, number_of_players - 1):
                                Aur_Cautatori[i] = galetusa_aur[i]

                        if number_of_players == 4:
                            Rol_Jucatori = [52, 53, 54, 30]
                            Aur_Sabotori = 4
                            for i in range(0, number_of_players - 1):
                                Aur_Cautatori[i] = galetusa_aur[i]

                        if number_of_players == 5:
                            Rol_Jucatori = [52, 53, 54, 30, 31]
                            Aur_Sabotori = 3
                            for i in range(0, number_of_players - 2):
                                Aur_Cautatori[i] = galetusa_aur[i]

                        if number_of_players == 6:
                            Rol_Jucatori = [52, 53, 54, 55, 30, 31]
                            Aur_Sabotori = 3
                            for i in range(0, number_of_players - 2):
                                Aur_Cautatori[i] = galetusa_aur[i]

                        if number_of_players == 7:
                            Rol_Jucatori = [52, 53, 54, 55, 30, 31, 32]
                            Aur_Sabotori = 3
                            for i in range(0, number_of_players - 3):
                                Aur_Cautatori[i] = galetusa_aur[i]

                        if number_of_players == 8:
                            Rol_Jucatori = [52, 53, 54, 55, 56, 30, 31, 32]
                            Aur_Sabotori = 3
                            for i in range(0, number_of_players - 3):
                                Aur_Cautatori[i] = galetusa_aur[i]

                        if number_of_players == 9:
                            Rol_Jucatori = [52, 53, 54, 55, 56, 57, 30, 31, 32]
                            Aur_Sabotori = 3
                            for i in range(0, number_of_players - 3):
                                Aur_Cautatori[i] = galetusa_aur[i]

                        if number_of_players == 10:
                            Rol_Jucatori = [52, 53, 54, 55, 56, 57, 30, 31, 32, 33]
                            Aur_Sabotori = 2
                            for i in range(0, number_of_players - 4):
                                Aur_Cautatori[i] = galetusa_aur[i]

                        
                        random.shuffle(Rol_Jucatori)

                        NumarCartiJucatori = calculate_cards_per_player(number_of_players)
                        CartiJucatori = [[None for _ in range(NumarCartiJucatori)] for _ in range(number_of_players)]
                        state = "GAME_SCREEN"
                        
                    except Exception as e:
                        print(f"An error occurred while initializing player cards: {e}")
                elif arrow_left_rect.collidepoint(event.pos):
                    state = "MAIN_MENU"
            elif state == "MAIN_MENU":
                if start_button_rect.collidepoint(event.pos):
                    state = "PLAYER_SELECTION"

                if instructions_button_rect.collidepoint(event.pos):
                    if deschis == False:
                        try:
                            os.startfile("Instructions.pdf")
                        except Exception as e:
                            print(f"Failed to open PDF: {e}")
                        deschis = True
                    

            

            

    # Actualizare ecran în funcție de starea jocului
    screen.blit(background_image, (0, 0))

    
    if state == "MAIN_MENU":
        screen.blit(title_image, (0, 0))
        screen.blit(start_button_image, start_button_rect)
        screen.blit(instructions_button_image, instructions_button_rect)
    elif state == "PLAYER_SELECTION":
         screen.blit(arrow_left_image, arrow_left_rect)
         screen.blit(number_of_players_image, number_of_players_rect)
         number_image = player_numbers_images[str(number_of_players)]
         number_rect = number_image.get_rect(center=(screen_width // 2, screen_height // 2))
         screen.blit(number_image, number_rect)
         screen.blit(plus_image, plus_rect)
         screen.blit(minus_image, minus_rect)
         screen.blit(start_button_image, start_button_rect) 
         
    elif state == "GAME_SCREEN":
        if popup:
            screen.blit(stone_background, stone_background_rect)
            screen.blit(home_button_image, home_button_rect)
            screen.blit(cancel_button_image, cancel_button_rect)
            screen.blit(paused_image, paused_rect)
            

        else:
            # Desenează săgețile
            screen.blit(arrow_up, (same_up_down, up_y))
            screen.blit(arrow_down, (same_up_down, down_y))
            screen.blit(arrow_left2, (right_x, same_left_right))
            screen.blit(arrow_right, (left_x, same_left_right))

            # Desenează imaginea pentru a alege o carte din TablaJoc
            screen.blit(select_image_boardgame, (55, 180))

            #Desenează dreptunghiul gri
            screen.blit(grey_rect, (10, 535))

            #desenare dreptunghi 2 gri
            screen.blit(grey_rect2, (Grey_rect2_x, Grey_rect2_y))

            # Desenează săgețile pentru navigarea cărților jucătorului
            screen.blit(arrow_right3, (arrow_right_x, arrow_right_y))
            screen.blit(arrow_left3, (arrow_left_x, arrow_left_y))



            # Desenează imaginea pentru a alege o carte din mâna jucătorului
            screen.blit(select_image_hand, (55, 450))

            # Afișarea imaginii corespunzătoare rolului jucătorului curent
            current_role_image = card_images[Rol_Jucatori[CurrentPlayer - 1]]
            current_role_image_scaled = pygame.transform.smoothscale(current_role_image, (100, 130))  # Redimensionare dacă este necesar
            role_image_position = (screen_width - 195, 38)  # Ajustează poziția după necesități
            screen.blit(current_role_image_scaled, role_image_position)

            # Afisarea imaginii pentru rol
            screen.blit(role1_image, role1_rect)

            # Afisarea imaginii pentru add_card
            screen.blit(add_card_image, add_card_rect)

            # Afisarea imaginii pentru drop_card
            screen.blit(drop_card_image, drop_card_rect)
            

            # Desenarea cărții selectate din CartiJucatori
            if len(CartiJucatori[CurrentPlayer - 1]) > selected_card_index:  # Verifică dacă indexul este valid
                selected_card_value = CartiJucatori[CurrentPlayer - 1][selected_card_index]
                selected_card_image = card_images.get(selected_card_value, card_images[CurrentPlayer - 1])  # Obține imaginea pentru cartea selectată
                selected_card_image = pygame.transform.scale(selected_card_image, (large_card_width, large_card_height))
                screen.blit(selected_card_image, (selected_card_display_x, selected_card_display_y))

            #Desenare buton pentru rotire
            screen.blit(rotate_image, (rotate_x, rotate_y))

            # Desenarea confirmării
            screen.blit(confirm_image, (confirm_x, confirm_y))

            #Desenare buton pentru tragere carte
            screen.blit(draw_image, (draw_x, draw_y))

            #Desenare buton pentru stergere carte
            screen.blit(delete_image, (delete_x, delete_y))

            #Desenare buton pentru terminare runda
            screen.blit(finish_image, (finish_x, finish_y))

            # Afișare imagine jucător curent
            player_image = player_images[CurrentPlayer]
            player_image_rect = player_image.get_rect(center=(135, 100))
            screen.blit(player_image, player_image_rect)

            # Afisare buton WIN
            screen.blit(win_image, win_rect)

            #Afisare carti de blocare
            screen.blit(blocked_road_1_image, blocked_road_1_rect)

            # Afișează valori din linia CurrentPlayer - 1 din BlockMatrix
            base_x = 1210  # Poziția inițială x pentru afișarea blocurilor
            base_y = 385  # Poziția y pentru afișarea pe linia de sub tabloul de joc
            row_to_display = BlockMatrix[CurrentPlayer - 1]
            for value in row_to_display:
                    block_image = card_images.get(value, card_images[0])  # Default la o imagine dacă valoarea nu este găsită
                    scaled_image = pygame.transform.scale(block_image, (60, 70))  # Mărim imaginea
                    screen.blit(scaled_image, (base_x, base_y))
                    base_y += 70  # Adaugă spațiu între blocuri

            # Inițializare matrice pentru cărțile jucătorilor
            CartiJucatori = [[None for _ in range(NumarCartiJucatori)] for _ in range(number_of_players)]
            RestulPachetului = []

            # Distribuirea cărților către jucători
            index = 0
            for i in range(number_of_players):
                for j in range(NumarCartiJucatori):
                    if index < len(AllTheCards):
                        CartiJucatori[i][j] = AllTheCards[index]
                        index += 1

            # Adăugarea restului de cărți în RestulPachetului
            RestulPachetului.extend(AllTheCards[index:])

            if (index_RestulPachetului == len(RestulPachetului)):
                for i in range(0, len(CartiJucatori[0])):
                    available_cards = False
                    for j in range(0, number_of_players):
                        if CartiJucatori[j][i] in {8, 9, 10, 11, 12, 14, 15, 41, 42, 43, 44}:
                            available_cards = True
                if available_cards == False:            
                    state = "WIN_Saboteur"

            # Desenarea imaginilor corespunzătoare valorilor din TablaJoc
            for row_index, row in enumerate(TablaJoc):
                for col_index, value in enumerate(row):
                    card_image = card_images.get(value, card_images[0])  # Folosește imaginea default dacă valoarea nu există
                    x_position = col_index * tile_width + horizontal_offset  # Calcul poziție X
                    y_position = row_index * tile_height  # Calcul poziție Y
                    screen.blit(card_image, (x_position, y_position))
                    if row_index == selected_row and col_index == selected_col:
                        screen.blit(selection_image, (x_position, y_position))

            
            # Desenarea cărților din prima linie a CartiJucatori
            base_y = 7 * tile_height + 20  # Poziție de start pentru Y, 20 pixels sub ultima linie a TablaJoc
            for idx, card_value in enumerate(CartiJucatori[CurrentPlayer - 1]):
                card_image = card_images.get(card_value)
                large_card_image = pygame.transform.scale(card_image, (large_card_width, large_card_height))
                x_position = idx * (large_card_width + 10) + horizontal_offset + 40  # Poziționează cu un spațiu mai mare între cărți
                screen.blit(large_card_image, (x_position, base_y))
                if idx == selected_card_index:
                    screen.blit(transparent_card_image, (x_position, base_y))

        screen.blit(menu_image, menu_button_rect)
    elif state == "PLAYER_SWITCH":
        # Display specific player button
        player_button_image = player_switch_images[CurrentPlayer]
        player_button_rect = player_button_image.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(player_button_image, player_button_rect)

    elif state == "BonusCards":


        # Desenează imaginile pentru jucătorii activi în funcție de numărul lor
        x_pos = 10  # Poziție de start pentru x
        y_pos = 200  # Poziție de start pentru y
        spacing = 125  # Spațierea între imagini

        # Afișează imagini pentru fiecare jucător activ
        for i in range(1, number_of_players + 1):
            player_image = player_images[i]
            screen.blit(player_image, (x_pos, y_pos))
            x_pos += spacing  # Actualizează poziția x pentru următoarea imagine

        # Afișează butonul pentru terminarea rundei în BonusCards
        screen.blit(finish_1_image, finish_1_rect)

        # Afișează butonul pentru blocare/deblocare
        screen.blit(block_unblock_image, block_unblock_rect)

        # Verifică dacă a fost apăsat butonul Finish_1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if finish_1_rect.collidepoint(event.pos):
                state = "GAME_SCREEN"

        

        # Afișează valorile din BlockMatrix cu imagini corespunzătoare
        matrix_x = 45  # Poziție x de start pentru BlockMatrix
        matrix_y = 300  # Poziție y de start pentru BlockMatrix
        for row in BlockMatrix:
            for value in row:
                block_image = card_images[value]  # Obține imaginea corespunzătoare valorii
                scaled_image = pygame.transform.scale(block_image, (60, 65))
                screen.blit(scaled_image, (matrix_x, matrix_y))
                matrix_y += 65  # Adaugă un spațiu între imagini
            matrix_y = 300 
            matrix_x = matrix_x + 125  # Resetare la poziția x inițială pentru următoarea linie

        # Afisați butoanele pentru aici
        screen.blit(aici1_image, aici1_rect)
        screen.blit(aici2_image, aici2_rect)
        screen.blit(aici3_image, aici3_rect)
        if(number_of_players > 3):
            screen.blit(aici4_image, aici4_rect)
            if(number_of_players > 4):
                screen.blit(aici5_image, aici5_rect)
                if(number_of_players > 5):
                    screen.blit(aici6_image, aici6_rect)
                    if(number_of_players > 6):
                        screen.blit(aici7_image, aici7_rect)
                        if(number_of_players > 7):
                            screen.blit(aici8_image, aici8_rect)
                            if(number_of_players > 8):
                                screen.blit(aici9_image, aici9_rect)
                                if(number_of_players > 9):
                                    screen.blit(aici10_image, aici10_rect)
    elif state == "GASESTE_AURUL":
        screen.blit(finish_2_image, finish_2_rect)

        FindTheGold[1][1] = 45
        FindTheGold[3][1] = 46
        FindTheGold[5][1] = 47

        if event.type == pygame.MOUSEBUTTONDOWN:
            if finish_2_rect.collidepoint(event.pos):
                state = "GAME_SCREEN"
                

        matrice_x = 535
        matrice_y = 60
        for row in FindTheGold:
            for value in row:
                block_image = card_images[value]
                scaled_image = pygame.transform.smoothscale(block_image, (60, 65))
                screen.blit(scaled_image, (matrice_x, matrice_y))
                matrice_x += 65
            matrice_y = matrice_y + 65
            matrice_x = 535 

        screen.blit(Aur1_image, Aur1_rect)
        screen.blit(Aur2_image, Aur2_rect)
        screen.blit(Aur3_image, Aur3_rect)

    elif state == "GASESTE_AURUL1":
        screen.blit(finish_2_image, finish_2_rect)
        screen.blit(press_and_hold_image, press_and_hold_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if finish_2_rect.collidepoint(event.pos):
                FindTheGold[1][1] = 45
                FindTheGold[3][1] = 46
                FindTheGold[5][1] = 47
                Afisare = card_images[-1]
                scaled_image = pygame.transform.scale(Afisare, (200, 300))
                screen.blit(scaled_image, (200, 180))
                Activate = 0
                state = "GAME_SCREEN"

            FindTheGold[1][1] = WhereIsTheGold[0]
            Afisare = card_images[WhereIsTheGold[0]]
            scaled_image = pygame.transform.scale(Afisare, (200, 300))
            screen.blit(scaled_image, (200, 180))

        matrice_x = 535
        matrice_y = 60
        for row in FindTheGold:
            for value in row:
                block_image = card_images[value]
                scaled_image = pygame.transform.smoothscale(block_image, (60, 65))
                screen.blit(scaled_image, (matrice_x, matrice_y))
                matrice_x += 65
            matrice_y = matrice_y + 65
            matrice_x = 535 

    elif state == "GASESTE_AURUL2":
        screen.blit(finish_2_image, finish_2_rect)
        screen.blit(press_and_hold_image, press_and_hold_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if finish_2_rect.collidepoint(event.pos):
                FindTheGold[1][1] = 45
                FindTheGold[3][1] = 46
                FindTheGold[5][1] = 47
                Afisare = card_images[-1]
                scaled_image = pygame.transform.scale(Afisare, (200, 300))
                screen.blit(scaled_image, (200, 180))
                Activate = 0
                state = "GAME_SCREEN"

            FindTheGold[3][1] = WhereIsTheGold[1]
            Afisare = card_images[WhereIsTheGold[1]]
            scaled_image = pygame.transform.scale(Afisare, (200, 300))
            screen.blit(scaled_image, (200, 180))

        matrice_x = 535
        matrice_y = 60
        for row in FindTheGold:
            for value in row:
                block_image = card_images[value]
                scaled_image = pygame.transform.smoothscale(block_image, (60, 65))
                screen.blit(scaled_image, (matrice_x, matrice_y))
                matrice_x += 65
            matrice_y = matrice_y + 65
            matrice_x = 535 


    elif state == "GASESTE_AURUL3":
        screen.blit(finish_2_image, finish_2_rect)
        screen.blit(press_and_hold_image, press_and_hold_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if finish_2_rect.collidepoint(event.pos):
                FindTheGold[1][1] = 45
                FindTheGold[3][1] = 46
                FindTheGold[5][1] = 47
                Afisare = card_images[-1]
                scaled_image = pygame.transform.scale(Afisare, (200, 300))
                screen.blit(scaled_image, (200, 180))
                Activate = 0
                state = "GAME_SCREEN"

            FindTheGold[5][1] = WhereIsTheGold[2]
            Afisare = card_images[WhereIsTheGold[2]]
            scaled_image = pygame.transform.scale(Afisare, (200, 300))
            screen.blit(scaled_image, (200, 180))

        matrice_x = 535
        matrice_y = 60
        for row in FindTheGold:
            for value in row:
                block_image = card_images[value]
                scaled_image = pygame.transform.smoothscale(block_image, (60, 65))
                screen.blit(scaled_image, (matrice_x, matrice_y))
                matrice_x += 65
            matrice_y = matrice_y + 65
            matrice_x = 535 
    
    elif state == "WIN":
        for row_index, row in enumerate(TablaJoc):
                for col_index, value in enumerate(row):
                    card_image = card_images.get(value, card_images[0])  # Folosește imaginea default dacă valoarea nu există
                    x_position = col_index * tile_width + horizontal_offset  # Calcul poziție X
                    y_position = row_index * tile_height  # Calcul poziție Y
                    screen.blit(card_image, (x_position, y_position))
                    if row_index == selected_row and col_index == selected_col:
                        screen.blit(selection_image, (x_position, y_position))
        
        #Afisare Dwarf_Win
        screen.blit(dwarf_win_image, dwarf_win_rect)
    
        igreg = 50
        
        JucatorCurent = CurrentPlayer
        copie_nr_jucatori = number_of_players

        lungime = len(Aur_Cautatori)
        i = 0

        Aur_Cautatori.sort(reverse = True)
        

        while copie_nr_jucatori > 0:
            if JucatorCurent <= number_of_players:
                if Rol_Jucatori[JucatorCurent - 1] in {52, 53, 54, 55, 56, 57, 58}:
                    player_image = player_images2[JucatorCurent]
                    player_rect = player_image.get_rect(center=(65, igreg))
                    screen.blit(player_image, player_rect)
                    screen.blit(just_gold_image, (185, igreg - 25))
                    if lungime > i:
                        number_image2 = player_numbers_images2[str(Aur_Cautatori[i])]
                        i += 1
                        screen.blit(number_image2, (125, igreg - 25))
                    igreg += 100
                JucatorCurent += 1
                copie_nr_jucatori -= 1
            else:
                JucatorCurent = 1

        screen.blit(trophy_image1, trophy_rect1)
        screen.blit(trophy_image2, trophy_rect2)

    elif state == "WIN_Saboteur":
        for row_index, row in enumerate(TablaJoc):
                for col_index, value in enumerate(row):
                    card_image = card_images.get(value, card_images[0])  # Folosește imaginea default dacă valoarea nu există
                    x_position = col_index * tile_width + horizontal_offset  # Calcul poziție X
                    y_position = row_index * tile_height  # Calcul poziție Y
                    screen.blit(card_image, (x_position, y_position))
                    if row_index == selected_row and col_index == selected_col:
                        screen.blit(selection_image, (x_position, y_position))
        
        #Afisare Saboteur_Win
        screen.blit(saboteur_win_image, saboteur_win_rect)
        
        igreg = 50
        
        JucatorCurent = CurrentPlayer
        copie_nr_jucatori = number_of_players

        while copie_nr_jucatori > 0:
            if JucatorCurent <= number_of_players:
                if Rol_Jucatori[JucatorCurent - 1] in {30, 31, 32, 33}:
                    player_image = player_images2[JucatorCurent]
                    player_rect = player_image.get_rect(center=(65, igreg))
                    screen.blit(player_image, player_rect)
                    screen.blit(just_gold_image, (185, igreg - 25))
                    number_image2 = player_numbers_images2[str(Aur_Sabotori)]
                    screen.blit(number_image2, (125, igreg - 25))
                    igreg += 100
                JucatorCurent += 1
                copie_nr_jucatori -= 1
            else:
                JucatorCurent = 1

        screen.blit(trophy_image3, (10, 450))
        screen.blit(trophy_image4, (1010, 450))

        
                



    screen.blit(sound_button_image, sound_button_rect)
        

    pygame.display.flip()

pygame.quit()