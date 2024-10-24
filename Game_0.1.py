import pygame
import sys
import random

# Inițializare Pygame
pygame.init()

# Setare dimensiune fereastră
screen_width = 1550
screen_height = 842
#screen_width = 1280 
#screen_height = 720 
screen = pygame.display.set_mode((screen_width, screen_height))

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

# Imagine pentru numarul de jucători
number_of_players_image = pygame.image.load('Number_Of_Players.png')
number_of_players_image = pygame.transform.scale(number_of_players_image, (400, 250))
number_of_players_rect = number_of_players_image.get_rect(center=(screen_width // 2, screen_height // 2 - 130))

player_numbers_images = {str(i): pygame.transform.scale(pygame.image.load(f'{i}.png'), (100, 100)) for i in range(1, 12)}
plus_image = pygame.transform.scale(pygame.image.load('+.png'), (50, 50))
minus_image = pygame.transform.scale(pygame.image.load('-.png'), (50, 50))
arrow_left_image = pygame.transform.scale(pygame.image.load('Arrow_Left.png'), (50, 50))
arrow_left_rect = arrow_left_image.get_rect(topleft=(20, 20))

menu_image = pygame.transform.scale(pygame.image.load('Menu.png'), (50, 50))
start_button_image = pygame.transform.scale(pygame.image.load('Start.png'), (200, 100))

# Redimensionare și poziționare butoane pop-up
home_button_image = pygame.transform.scale(pygame.image.load('Home.png'), (50, 70))
cancel_button_image = pygame.transform.scale(pygame.image.load('Cancel.png'), (50, 70))
home_button_rect = home_button_image.get_rect(topleft=(70, stone_background_rect.bottom - 80))
cancel_button_rect = cancel_button_image.get_rect(topleft=(home_button_rect.right + 10, stone_background_rect.bottom - 80))

# Poziționare și redimensionare elemente
plus_rect = plus_image.get_rect(center=(screen_width/2 + 100, screen_height/2))
minus_rect = minus_image.get_rect(center=(screen_width/2 - 100, screen_height/2))
start_button_rect = start_button_image.get_rect(center=(screen_width/2, screen_height/2 + 150))
menu_button_rect = menu_image.get_rect(topleft=(screen_width - 1530, 20))

# Butonul de pauză
paused_image = pygame.image.load('Paused.png')
paused_image = pygame.transform.scale(paused_image, (300, 200))
paused_rect = paused_image.get_rect(center=(screen_width // 2, screen_height // 2))

# Definește culoarea fundalului matricei (RGB)
matrix_background_color = (150, 150, 150)  # Gri

# Inițializare mixer pentru muzică
pygame.mixer.init()
pygame.mixer.music.load('Avatars_Love.mp3')
pygame.mixer.music.play(-1)  # Redă în buclă
pygame.mixer.music.set_volume(0.5)

# Încărcarea imaginilor pentru sunet
sound_on_image = pygame.image.load('Sound.png')
sound_on_image = pygame.transform.scale(sound_on_image, (50, 50))
sound_off_image = pygame.image.load('Mute.png')
sound_off_image = pygame.transform.scale(sound_off_image, (50, 50))

# Buton pentru controlul sunetului
sound_button_image = sound_on_image
sound_button_rect = sound_button_image.get_rect(topleft=(screen_width - 80, 20))
is_sound_on = True

# Coordonate inițiale pentru imaginea numărului de jucători
player_number_image_x = screen_width // 2 - 500
player_number_image_y = 50  # De exemplu, poziționează imaginea mai sus în ecran
player_number_image_width = 70
player_number_image_height = 70

cell_width = 80  # Lățimea celulei ajustată în funcție de necesități
cell_height = cell_width + 10  # Înălțimea celulei ajustată în funcție de necesități

cell_width2 = 140  # Lățimea celulei ajustată în funcție de necesități
cell_height2 = cell_width2 + 20  # Înălțimea celulei ajustată în funcție de necesități

# Încărcarea și redimensionarea imaginii pentru spatele cărților de drum
backside_image_original = pygame.image.load('Backside_Silver_Road.png')
backside_image = pygame.transform.scale(backside_image_original, (cell_width, cell_height))

# Încărcarea și redimensionarea imaginii pentru spatele cărții scara
backside_ladder_original = pygame.image.load('Stairs.png')
backside_ladder = pygame.transform.scale(backside_ladder_original, (cell_width, cell_height))

# Încărcarea și redimensionarea imaginii pentru finisajul din bronz
backside_bronze_finish_original = pygame.image.load('Backside_Bronze_Finish.png')
backside_bronze_finish = pygame.transform.scale(backside_bronze_finish_original, (cell_width, cell_height))

#incarcare si redimensionarea imaginii pentru afisajul aurului final
backside_gold_finish_original = pygame.image.load('Finish_GOLD.png')
backside_gold_finish = pygame.transform.scale(backside_gold_finish_original, (cell_width, cell_height))

#incarcarea imaginii Blocked_road_1.png
blocked_road_1_original = pygame.image.load('Blocked_road_1.png')
blocked_road_1 = pygame.transform.scale(blocked_road_1_original, (cell_width2, cell_height2))

#incarcarea imaginii Blocked_road_2.png
blocked_road_2_original = pygame.image.load('Blocked_road_2.png')
blocked_road_2 = pygame.transform.scale(blocked_road_2_original, (cell_width2, cell_height2))

#incarcarea imaginii Blocked_road_3.png
blocked_road_3_original = pygame.image.load('Blocked_road_3.png')
blocked_road_3 = pygame.transform.scale(blocked_road_3_original, (cell_width2, cell_height2))

#incarcarea imaginii Blocked_road_4.png
blocked_road_4_original = pygame.image.load('Blocked_road_4.png')
blocked_road_4 = pygame.transform.scale(blocked_road_4_original, (cell_width2, cell_height2))

#incarcarea imaginii Blocked_road_5.png
blocked_road_5_original = pygame.image.load('Blocked_road_5.png')
blocked_road_5 = pygame.transform.scale(blocked_road_5_original, (cell_width2, cell_height2))

#incarcarea imaginii Blocked_road_6.png
blocked_road_6_original = pygame.image.load('Blocked_road_6.png')
blocked_road_6 = pygame.transform.scale(blocked_road_6_original, (cell_width2, cell_height2))

#incarcarea imaginii Blocked_road_7.png
blocked_road_7_original = pygame.image.load('Blocked_road_7.png')
blocked_road_7 = pygame.transform.scale(blocked_road_7_original, (cell_width2, cell_height2))

#incarcarea imaginii I1_road.png
I1_road_original = pygame.image.load('I1_road.png')
I1_road = pygame.transform.scale(I1_road_original, (cell_width2, cell_height2))

#incarcarea imaginii I2_road.png
I2_road_original = pygame.image.load('I2_road.png')
I2_road = pygame.transform.scale(I2_road_original, (cell_width2, cell_height2))

#incarcarea imaginii L1_road.png
L1_road_original = pygame.image.load('L1_road.png')
L1_road = pygame.transform.scale(L1_road_original, (cell_width2, cell_height2))

#incarcarea imaginii L2_road.png
L2_road_original = pygame.image.load('L2_road.png')
L2_road = pygame.transform.scale(L2_road_original, (cell_width2, cell_height2))

#incarcarea imaginii Roundabout.png
Roundabout_original = pygame.image.load('Roundabout.png')
Roundabout = pygame.transform.scale(Roundabout_original, (cell_width2, cell_height2))

#incarcarea imaginii T1_road.png
T1_road_original = pygame.image.load('T1_road.png')
T1_road = pygame.transform.scale(T1_road_original, (cell_width2, cell_height2))

#incarcarea imaginii T2_road.png
T2_road_original = pygame.image.load('T2_road.png')
T2_road = pygame.transform.scale(T2_road_original, (cell_width2, cell_height2))

#incarcare Block_lamp.png
blocked_lamp_original = pygame.image.load('Block_lamp.png')
blocked_lamp = pygame.transform.scale(blocked_lamp_original, (cell_width2, cell_height2))

#incarcare Block_minecart.png
blocked_minecart_original = pygame.image.load('Block_minecart.png')
blocked_minecart = pygame.transform.scale(blocked_minecart_original, (cell_width2, cell_height2))

#incarcare Block_pickaxe.png
blocked_pickaxe_original = pygame.image.load('Block_pickaxe.png')
blocked_pickaxe = pygame.transform.scale(blocked_pickaxe_original, (cell_width2, cell_height2))

#incarcare Destroy.png
destroy_original = pygame.image.load('Destroy.png')
destroy = pygame.transform.scale(destroy_original, (cell_width2, cell_height2))

#incarcare See_gold.png
see_gold_original = pygame.image.load('See_gold.png')
see_gold = pygame.transform.scale(see_gold_original, (cell_width2, cell_height2))

#incarcare Unlock_lamp.png
unlock_lamp_original = pygame.image.load('Unlock_lamp.png')
unlock_lamp = pygame.transform.scale(unlock_lamp_original, (cell_width2, cell_height2))

#incarcare Unlock_minecart.png
unlock_minecart_original = pygame.image.load('Unlock_minecart.png')
unlock_minecart = pygame.transform.scale(unlock_minecart_original, (cell_width2, cell_height2))

#incarcare Unlock_pickaxe.png
unlock_pickaxe_original = pygame.image.load('Unlock_pickaxe.png')
unlock_pickaxe = pygame.transform.scale(unlock_pickaxe_original, (cell_width2, cell_height2))

#incarare Unlock_lamp_minecart.png
unlock_lamp_minecart_original = pygame.image.load('Unlock_lamp_minecart.png')
unlock_lamp_minecart = pygame.transform.scale(unlock_lamp_minecart_original, (cell_width2, cell_height2))

#incarcare Unlock_pickaxe_lamp.png
unlock_pickaxe_lamp_original = pygame.image.load('Unlock_pickaxe_lamp.png')
unlock_pickaxe_lamp = pygame.transform.scale(unlock_pickaxe_lamp_original, (cell_width2, cell_height2))

#incarcare Unlock_pickaxe_minecart.png
unlock_pickaxe_minecart_original = pygame.image.load('Unlock_pickaxe_minecart.png')
unlock_pickaxe_minecart = pygame.transform.scale(unlock_pickaxe_minecart_original, (cell_width2, cell_height2))

# După inițializarea celorlalte imagini
confirm_image = pygame.image.load('Confirm_OG.png')
confirm_image = pygame.transform.scale(confirm_image, (60, 60))  # Redimensionează la dimensiunea dorită
confirm_rect = confirm_image.get_rect(bottomleft=(240, 820))  # Poziționează în colțul din stânga jos

#incarcare fundal gri
grey_rectangle_background = pygame.image.load('Grey_Rectangle_Background.png')
grey_rectangle_background = pygame.transform.scale(grey_rectangle_background, (310, 180))  # Ajustați dimensiunea după necesități


def update_display():
    # Curăță întregul ecran
    screen.fill((0, 0, 0))

    # Redesenează fundalul și alte elemente în funcție de starea curentă
    if state == "MAIN_MENU":
        screen.blit(background_image, (0, 0))
        screen.blit(title_image, (0, 0))
        screen.blit(start_button_image, start_button_rect)
    elif state == "PLAYER_SELECTION":
        screen.blit(background_image, (0, 0))
        screen.blit(arrow_left_image, arrow_left_rect)
        screen.blit(number_of_players_image, number_of_players_rect)
        number_image = player_numbers_images[str(number_of_players)]
        number_rect = number_image.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(number_image, number_rect)
        screen.blit(plus_image, plus_rect)
        screen.blit(minus_image, minus_rect)
        screen.blit(start_button_image, start_button_rect)
    elif state == "GAME_SCREEN":
        screen.blit(background_image, (0, 0))
        # Afișarea matricei de imagini
        for row in range(rows):
            for col in range(cols):
                cell_pos_x = (screen_width - cols * cell_width) // 2 + col * cell_width
                cell_pos_y = (screen_height - rows * cell_height) // 2 - 100 + row * cell_height
                screen.blit(matrix[row][col], (cell_pos_x, cell_pos_y))
                if confirmed_positions[row][col]:
                    screen.blit(backside_red_road, (cell_pos_x, cell_pos_y))

        

        screen.blit(confirm_image, confirm_rect)
        # Afișează butoanele și contoarele
        screen.blit(column_image, column_counter_pos)
        screen.blit(plus_image1, (210, 310))
        screen.blit(minus_image1, (80, 310))
        screen.blit(plus_image2, (145, 360))
        screen.blit(minus_image2, (145, 260))
        screen.blit(card_image2, card_counter_pos)
        screen.blit(plus_image3, (270, 660))
        screen.blit(minus_image3, (210, 660))

        # Poate fi necesar să actualizezi și alte elemente aici

    # Redesenează elementele UI comune, cum ar fi butoanele de sunet
    screen.blit(menu_image, menu_button_rect)
    screen.blit(sound_button_image, sound_button_rect)
    
    # Actualizează afișarea pentru a reflecta noile schimbări
    pygame.display.flip()




#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Valorile inițiale pentru countere
counter_column_value = 1
counter_line_value = 1
counter_card_value = 1

# Încărcarea imaginilor pentru counter
column_image = pygame.transform.scale(pygame.image.load('Choose_A_Card_From_The_Table.png'), (220, 120))
line_image = pygame.transform.scale(pygame.image.load('Line.png'), (150, 100))
card_image2 = pygame.transform.scale(pygame.image.load('Choose_A_Card.png'), (220, 120))
plus_image1 = pygame.transform.scale(pygame.image.load('Arrow_Right.png'), (90, 90))
minus_image1 = pygame.transform.scale(pygame.image.load('Arrow_Left.png'), (90, 90))
plus_image2 = pygame.transform.scale(pygame.image.load('Arrow_Down.png'), (90, 90))
minus_image2 = pygame.transform.scale(pygame.image.load('Arrow_Up.png'), (90, 90))
plus_image3 = pygame.transform.scale(pygame.image.load('Arrow_Right.png'), (50, 50))
minus_image3 = pygame.transform.scale(pygame.image.load('Arrow_Left.png'), (50, 50))

# Poziționarea counterelor
column_counter_pos = (80, screen_height - 700)  # Ajustează poziția după necesități

line_counter_pos = (30, screen_height - 700)    # Ajustează poziția după necesități

card_counter_pos = (80, screen_height - 310)    # Ajustează poziția după necesități


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Crearea listei de cărți cu numărul specific de exemplare pentru fiecare
cards_list = (
    ["Blocked_road_1"] * 1 + 
    ["Blocked_road_2"] * 1 + 
    ["Blocked_road_3"] * 1 + 
    ["Blocked_road_4"] * 1 + 
    ["Blocked_road_5"] * 1 + 
    ["Blocked_road_6"] * 1 + 
    ["Blocked_road_7"] * 1 + 
    ["I1_road"] * 3 + 
    ["I2_road"] * 4 + 
    ["L1_road"] * 5 + 
    ["L2_road"] * 4 + 
    ["Roundabout"] * 5 + 
    ["T1_road"] * 5 + 
    ["T2_road"] * 5 +
    ["Block_lamp"] * 3 +
    ["Block_minecart"] * 3 +
    ["Block_pickaxe"] * 3 +
    ["Destroy"] * 3 +
    ["See_gold"] * 6 +
    ["Unlock_lamp"] * 2 +
    ["Unlock_minecart"] * 2 +
    ["Unlock_pickaxe"] * 2 +
    ["Unlock_lamp_minecart"] * 1 +
    ["Unlock_pickaxe_lamp"] * 1 +
    ["Unlock_pickaxe_minecart"] * 1
    
)

random.shuffle(cards_list)




# Crearea matricei de imagini
rows = 7
cols = 11
matrix = [[backside_image for _ in range(cols)] for _ in range(rows)]


# Actualizarea matricei pentru scara pe linia 4, coloana 2
backside_ladder = pygame.transform.scale(backside_ladder_original, (cell_width, cell_height))
matrix[3][1] = backside_ladder

# Actualizarea matricei pentru finisajul din bronz pe pozițiile specificate
matrix[1][9] = backside_bronze_finish
matrix[3][9] = backside_bronze_finish
matrix[5][9] = backside_bronze_finish

# Numărul inițial de jucători
number_of_players = 3

# Stări pentru ecran și pop-up
state = "MAIN_MENU"
popup = False

# Variabila pentru control buclă principală
running = True

# Încărcarea și redimensionarea imaginii pentru drumul roșu
backside_red_road_original = pygame.image.load('Backside_Red_Road.png')
backside_red_road = pygame.transform.scale(backside_red_road_original, (cell_width, cell_height))

# Încărcarea și redimensionarea imaginii "Backside_Green_Transparent_Road.png"
backside_green_transparent_road_original = pygame.image.load('Backside_Green_Transparent_Road.png')
backside_green_transparent_road = pygame.transform.scale(backside_green_transparent_road_original, (cell_width2, cell_height2))


# Matricea de poziții confirmate
confirmed_positions = [[False for _ in range(cols)] for _ in range(rows)]

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            

            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            
            # Logica pentru counter-ul de coloane
            plus_rect_col = plus_image1.get_rect(topleft=(210, 310))
            minus_rect_col = minus_image1.get_rect(topleft=(80, 310))
            if plus_rect_col.collidepoint(event.pos):
                counter_column_value = min(counter_column_value + 1, 11)  # Asigură-te că valoarea nu depășește 11
            elif minus_rect_col.collidepoint(event.pos):
                counter_column_value = max(counter_column_value - 1, 1)  # Asigură-te că valoarea nu scade sub 1
            
            # Logica pentru counter-ul de linii
            plus_rect_line = plus_image2.get_rect(topleft=(145, 360))
            minus_rect_line = minus_image2.get_rect(topleft=(145, 260))
            if plus_rect_line.collidepoint(event.pos):
                counter_line_value = min(counter_line_value + 1, 7)
            elif minus_rect_line.collidepoint(event.pos):
                counter_line_value = max(counter_line_value - 1, 1)

            # Logica pentru counter-ul de cărți
            plus_rect_card = plus_image.get_rect(topleft=(270, 660))
            minus_rect_card = minus_image.get_rect(topleft=(210, 660 ))
            if plus_rect_card.collidepoint(event.pos):
                counter_card_value = min(counter_card_value + 1, cards_to_display)
            elif minus_rect_card.collidepoint(event.pos):
                counter_card_value = max(counter_card_value - 1, 1)

            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            
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
                # Dacă există un eveniment de clic în timp ce pop-up-ul este activ
                if home_button_rect.collidepoint(event.pos):
                    pygame.quit()  # Închide fereastra Pygame
                    sys.exit()  # Încheie execuția scriptului
                elif cancel_button_rect.collidepoint(event.pos):
                    popup = False
                    # Repornește muzica dacă pop-up-ul este dezactivat și sunetul este pornit
                    if is_sound_on:
                        pygame.mixer.music.unpause()

            elif state == "GAME_SCREEN":

                if menu_button_rect.collidepoint(event.pos):
                    popup = not popup  # Afișează sau ascunde pop-up-ul
                    # Dacă popup-ul este activat, pune muzica pe pauză. Altfel, reia redarea.
                    if popup and is_sound_on:
                        pygame.mixer.music.pause()
            elif state == "PLAYER_SELECTION":
                if plus_rect.collidepoint(event.pos) and number_of_players < 10:
                    number_of_players += 1
                elif minus_rect.collidepoint(event.pos) and number_of_players > 3:
                    number_of_players -= 1
                elif start_button_rect.collidepoint(event.pos):
                    state = "GAME_SCREEN"
                elif arrow_left_rect.collidepoint(event.pos):
                    state = "MAIN_MENU"
            elif state == "MAIN_MENU":
                if start_button_rect.collidepoint(event.pos):
                    state = "PLAYER_SELECTION"

    # Actualizare ecran în funcție de starea jocului
    screen.blit(background_image, (0, 0))
    if state == "MAIN_MENU":
        screen.blit(title_image, (0, 0))
        screen.blit(start_button_image, start_button_rect)
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

       

        # Logica pentru apăsarea butonului Confirm
        if event.type == pygame.MOUSEBUTTONDOWN:
            if confirm_rect.collidepoint(event.pos):
                if (counter_line_value, counter_column_value) not in [(4, 2), (2, 10), (4, 10), (6, 10)]:
                    if not confirmed_positions[counter_line_value - 1][counter_column_value - 1]:
                        # Obține cartea selectată și actualizează matricea jocului
                        selected_card_image = matrix_players_cards[linie][counter_card_value - 1]  # corectare index
                        resized_image = pygame.transform.scale(selected_card_image, (cell_width, cell_height))
                        matrix[counter_line_value - 1][counter_column_value - 1] = resized_image
                        confirmed_positions[counter_line_value - 1][counter_column_value - 1] = True
                        
                        # Elimină cartea din mâna jucătorului
                        matrix_players_cards[linie][counter_card_value - 1] = backside_image  # Setează poziția ca fiind None sau folosește o imagine goală
                        
                        # Afișarea doar a primei linii din matricea jucătorilor (cărțile primului jucător)
                        for j, card_image in enumerate(matrix_players_cards[linie]):
                            card_pos_x = start_x + j * (cell_width + 60)  # Adaugă spațiu între cărți
                            screen.blit(backside_image, (card_pos_x, start_y))
                        
                        # Actualizează ecranul pentru a reflecta modificările
                        update_display()


                        




        background_x = 30  # Poziția x este 0 pentru a fi în colțul din stânga
        background_y = screen_height - 190  # Ajustați la înălțimea imaginii scalate

        screen.blit(grey_rectangle_background, (background_x, background_y))

         # Afisarea butonului Confirm
        screen.blit(confirm_image, confirm_rect)

        #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        # Afișează imaginile și butoanele pentru counter-ul de coloane
        screen.blit(column_image, column_counter_pos)
        screen.blit(plus_image1, ( 210, 310))  # Plus button
        screen.blit(minus_image1, (80, 310))  # Minus button
        # Afișează valoarea curentă a counterului
        counter_value_image = player_numbers_images[str(counter_column_value)]
        ###screen.blit(counter_value_image, (195, 310))
        
        # Afișează imaginile și butoanele pentru counter-ul de linii
        ###screen.blit(line_image, line_counter_pos)
        screen.blit(plus_image2, (145, 360))  # Plus button
        screen.blit(minus_image2, (145, 260)) # Minus button
        # Afișează valoarea curentă a counterului
        counter_value_image = player_numbers_images[str(counter_line_value)]
        ###screen.blit(counter_value_image, (60, 310))

        # Afișează imaginile și butoanele pentru counter-ul de cărți
        screen.blit(card_image2, card_counter_pos)
        screen.blit(plus_image3, ( 270, 660))  # Plus button
        screen.blit(minus_image3, ( 210, 660)) # Minus button
        # Afișează valoarea curentă a counterului
        counter_value_image = player_numbers_images[str(counter_card_value)]
        ###screen.blit(counter_value_image, (135, 550))

        #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # Determinarea numărului de cărți în funcție de numărul de jucători
        if 3 <= number_of_players <= 5:
            cards_to_display = 6
        elif 6 <= number_of_players <= 7:
            cards_to_display = 5
        elif 8 <= number_of_players <= 10:
            cards_to_display = 4
        else:
            cards_to_display = 0  # Dacă din orice motiv numărul de jucători nu este în intervalul așteptat

        # Alege numărul de cărți pe care vrei să le afișezi, de exemplu 6
        selected_cards = cards_list[:cards_to_display]

        

        # Calcularea spațiului disponibil și a poziției inițiale pentru cărți
        total_cards_width = cards_to_display * cell_width + (cards_to_display - 1) * 10  # 10 pixeli spațiu între cărți
        start_x = (screen_width - total_cards_width) // 2 - 140
        start_y = screen_height - cell_height - 90  # 20 pixeli de marginea de jos a ecranului



        # Crearea unui dicționar pentru a mapă numele la imaginile încărcate
        cards_images_dict = {
            "Blocked_road_1": blocked_road_1,
            "Blocked_road_2": blocked_road_2,
            "Blocked_road_3": blocked_road_3,
            "Blocked_road_4": blocked_road_4,
            "Blocked_road_5": blocked_road_5,
            "Blocked_road_6": blocked_road_6,
            "Blocked_road_7": blocked_road_7,
            "I1_road": I1_road,
            "I2_road": I2_road,
            "L1_road": L1_road,
            "L2_road": L2_road,
            "Roundabout": Roundabout,
            "T1_road": T1_road,
            "T2_road": T2_road,
            "Block_lamp": blocked_lamp,
            "Block_minecart": blocked_minecart,
            "Block_pickaxe": blocked_pickaxe,
            "Destroy": destroy,
            "See_gold": see_gold,
            "Unlock_lamp": unlock_lamp,
            "Unlock_minecart": unlock_minecart,
            "Unlock_pickaxe": unlock_pickaxe,
            "Unlock_lamp_minecart": unlock_lamp_minecart,
            "Unlock_pickaxe_lamp": unlock_pickaxe_lamp,
            "Unlock_pickaxe_minecart": unlock_pickaxe_minecart
        }

        # Calcularea spațiului disponibil și a poziției inițiale pentru cărți
        total_cards_width = cards_to_display * cell_width + (cards_to_display - 1) * 10  # 10 pixeli spațiu între cărți
        start_x = (screen_width - total_cards_width) // 2 - 140
        start_y = screen_height - cell_height - 90  # 20 pixeli de marginea de jos a ecranului

        # Crearea matricei pentru cărțile jucătorilor
        matrix_players_cards = [[None for _ in range(cards_to_display)] for _ in range(number_of_players)]

        # Popularea matricei cu imagini pentru cărțile fiecărui jucător
        for i in range(number_of_players):
            for j in range(cards_to_display):
                card_name = cards_list[j]  
                matrix_players_cards[i][j] = cards_images_dict[card_name]
      

        linie = 0#linia pe care se afla jucatorul

        # Afișarea doar a primei linii din matricea jucătorilor (cărțile primului jucător)
        for j, card_image in enumerate(matrix_players_cards[linie]):
            card_pos_x = start_x + j * (cell_width + 60)  # Adaugă spațiu între cărți
            screen.blit(card_image, (card_pos_x, start_y))

        # Afisarea imaginii selectate din matricea de cărți a jucătorului în colțul din stânga jos
        selected_card_image = matrix_players_cards[linie][counter_card_value - 1]  # Ajustează indexul
        card_display_x = background_x + 10  # Puțin spațiu de la marginea fundalului gri
        card_display_y = background_y + 10  # Puțin spațiu de la marginea fundalului gri
        screen.blit(selected_card_image, (card_display_x, card_display_y))

        """
         # Ajustează dimensiunea imaginii cu numărul de jucători
        player_number_image = pygame.transform.scale(
            player_numbers_images[str(number_of_players)], 
            (player_number_image_width, player_number_image_height)
        )
        player_number_rect = player_number_image.get_rect(center=(player_number_image_x, player_number_image_y))
        screen.blit(player_number_image, player_number_rect)
        """
        # Calculul poziției de start pentru a centra matricea pe ecran
        start_x = (screen_width - cols * cell_width) // 2
        start_y = (screen_height - rows * cell_height) // 2 - 100  # Ajustează această valoare dacă este necesar


        # Calcularea poziției inițiale pentru cărțile de la baza ecranului
        start_x_cards = (screen_width - cards_to_display * cell_width - (cards_to_display - 1) * 10) // 2 - 140  # Ajustează dacă este necesar
        start_y_cards = screen_height - cell_height - 90  # Ajustează dacă este necesar


        # Afișarea imaginii "Backside_Green_Transparent_Road.png" deasupra cărților jucătorilor
        # Calculul poziției imaginii în funcție de valoarea counterului de cărți
        overlay_pos_x = start_x_cards + (counter_card_value - 1) * (cell_width + 60)  # 60 este spațiul dintre cărți, ajustează dacă este necesar
        overlay_pos_y = start_y_cards

        # Afișarea imaginii overlay
        screen.blit(backside_green_transparent_road, (overlay_pos_x, overlay_pos_y))


        # Afișarea matricei de imagini
        for row in range(rows):
            for col in range(cols):
                screen.blit(matrix[row][col], (start_x + col * cell_width, start_y + row * cell_height))

        # Afișarea matricei de imagini cu overlay-ul pentru poziția selectată
        for row in range(rows):
            for col in range(cols):
                cell_pos_x = start_x + col * cell_width
                cell_pos_y = start_y + row * cell_height
                screen.blit(matrix[row][col], (cell_pos_x, cell_pos_y))

                # Verifică dacă poziția curentă este cea selectată de counteri și afișează imaginea red road deasupra
                if row == counter_line_value - 1 and col == counter_column_value - 1:
                    screen.blit(backside_red_road, (cell_pos_x, cell_pos_y))


        if popup:
            screen.blit(stone_background, stone_background_rect)
            screen.blit(home_button_image, home_button_rect)
            screen.blit(cancel_button_image, cancel_button_rect)
            screen.blit(paused_image, paused_rect)
        screen.blit(menu_image, menu_button_rect)

    screen.blit(sound_button_image, sound_button_rect)

    pygame.display.flip()

pygame.quit()
