lista =["0", "0011", "1100", "0001", "0101", "0100", "1111", "0110", "0011", "1100", "1010", "1001", "1111", "1111", "1110", "0111", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0001", "0101", "0100", "0110", "0", "0", "1010", "1001", "1110", "0111", "0", "0", "0", "1011", "1110", "1011", "1110"]

for index, valoare in enumerate(lista):
    print(f"lista[{index}] = {valoare}")

print("")
print("")

selected_card = 1

selected_row = 1
selected_col = 1
TablaJoc = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34]]
WhereIsTheGold = [27, 28, 29]

sus_gol = [39, 40, 44, 11, 10, 48, 37, 36, 3, 35, 38, 8, 1, 0, 34]
sus_plin = [27, 28, 29, 15, 42, 12, 41, 14, 43, 7, 49, 51, 5, 9, 13, 50, 4, 6, 2, 0, 34]
jos_gol = [28, 29, 7, 4, 41, 3, 35, 42, 50, 15, 5, 8, 1, 0, 34]
jos_plin = [27, 39, 40, 10, 12, 38, 49, 51, 9, 37, 13, 36, 6, 48, 14, 43, 44, 11, 2, 0, 34]
dreapta_gol = [28, 40, 10, 7, 9, 49, 5, 37, 14, 36, 35, 42, 2, 0, 34]
dreapta_plin = [27, 29, 39, 6, 12, 41, 48, 50, 11, 3, 15, 44, 4, 38, 43, 13, 8, 51, 0, 34]
stanga_gol = [29, 39, 41, 9, 5, 37, 4, 11, 38, 51, 43, 3, 2, 0, 34]
stanga_plin = [27, 28, 40, 15, 44, 42, 10, 14, 12, 6, 7, 36, 35, 48, 50, 13, 8, 49, 1, 0, 34]



string_valori = lista[selected_card]
print(lista[selected_card])
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

if ok_final == False:
    print("Nu se poate muta cartea")


if (selected_row, selected_col) not in [(3, 1), (1, 9), (3, 9), (5, 9)]:
    if not((TablaJoc[selected_row - 1][selected_col] == 0 or TablaJoc[selected_row - 1][selected_col] == 34 or selected_row == 0) and (TablaJoc[selected_row + 1][selected_col] == 0 or TablaJoc[selected_row + 1][selected_col] == 34 or selected_row == 6) and (TablaJoc[selected_row][selected_col - 1] == 0 or TablaJoc[selected_row][selected_col - 1] == 34 or selected_col == 0) and (TablaJoc[selected_row][selected_col + 1] == 0 or TablaJoc[selected_row][selected_col + 1] == 34 or selected_col == 10)):
        print("Nu se poate muta cartea")
    
Blocked_raods =[1, 2, 3, 4, 5, 6, 7, 35, 36, 37, 38, 48, 49, 50, 51]

Finish_up = [12, 41, 42, 14, 43, 44]
Finish_down = [10, 11, 12, 14, 15, 43]
Finish_right = [8, 10, 11, 12, 14, 15, 44]
Finish_left = [8, 11, 12, 15, 41, 43, 44]

if (TablaJoc[selected_row - 1][selected_col] == 34 or TablaJoc[selected_row + 1][selected_col] == 34 or TablaJoc[selected_row][selected_col - 1] == 34 or TablaJoc[selected_row][selected_col + 1] == 34) and (TablaJoc[selected_row][selected_col] not in Blocked_raods):
    if selected_row == 1:
        if selected_col == 8:
            if TablaJoc[selected_row][selected_col] in Finish_left and TablaJoc[1][9] == 34:
                if WhereIsTheGold[0] == 27:
                    state = "WIN"
                if WhereIsTheGold[0] == 28:
                    TablaJoc[1][9] = 39
        
        if selected_col == 10:
            if TablaJoc[selected_row][selected_col] in Finish_right and TablaJoc[1][9] == 34:
                if WhereIsTheGold[0] == 27:
                    state = "WIN"
                if WhereIsTheGold[0] == 29:
                    TablaJoc[1][9] = 40
    
    if selected_row == 0:
        if selected_col == 9:
            if TablaJoc[selected_row][selected_col] in Finish_up and TablaJoc[1][9] == 34:
                if WhereIsTheGold[0] == 27:
                    TablaJoc[1][9] = 27
                    state = "WIN"
                if WhereIsTheGold[0] == 28:
                    TablaJoc[1][9] = 39

                if WhereIsTheGold[0] == 29:
                    TablaJoc[1][9] = 40

    if selected_row == 2:
        if selected_col == 9:
            if TablaJoc[selected_row][selected_col] in Finish_down and TablaJoc[1][9] == 34:
                if WhereIsTheGold[0] == 27:
                    TablaJoc[1][9] = 27
                    state = "WIN"
            if TablaJoc[selected_row][selected_col] in Finish_up and TablaJoc[3][9] == 34:
                if WhereIsTheGold[1] == 27:
                    TablaJoc[3][9] = 27
                    state = "WIN"
                if WhereIsTheGold[0] == 28:
                    TablaJoc[3][9] = 39

                if WhereIsTheGold[0] == 29:
                    TablaJoc[3][9] = 40
    
    if selected_row == 3:
        if selected_col == 8:
            if TablaJoc[selected_row][selected_col] in Finish_left and TablaJoc[3][9] == 34:
                if WhereIsTheGold[1] == 27:
                    TablaJoc[3][9] = 27
                    state = "WIN"
                if WhereIsTheGold[1] == 28:
                    TablaJoc[3][9] = 39

        if selected_col == 10:
            if TablaJoc[selected_row][selected_col] in Finish_right and TablaJoc[3][9] == 34:
                if WhereIsTheGold[1] == 27:
                    TablaJoc[3][9] = 27
                    state = "WIN"
                if WhereIsTheGold[1] == 29:
                    TablaJoc[3][9] = 40

    if selected_row == 4:
        if selected_col == 9:
            if TablaJoc[selected_row][selected_col] in Finish_down and TablaJoc[3][9] == 34:
                if WhereIsTheGold[1] == 27:
                    TablaJoc[3][9] = 27
                    state = "WIN"

            if TablaJoc[selected_row][selected_col] in Finish_up and TablaJoc[5][9] == 34:
                if WhereIsTheGold[2] == 27:
                    TablaJoc[5][9] = 27
                    state = "WIN"
                if WhereIsTheGold[2] == 28:
                    TablaJoc[5][9] = 39

                if WhereIsTheGold[2] == 29:
                    TablaJoc[5][9] = 40
    
    if selected_row == 5:
        if selected_col == 8:
            if TablaJoc[selected_row][selected_col] in Finish_left and TablaJoc[5][9] == 34:
                if WhereIsTheGold[2] == 27:
                    TablaJoc[5][9] = 27
                    state = "WIN"
                if WhereIsTheGold[2] == 28:
                    TablaJoc[5][9] = 39

        if selected_col == 10:
            if TablaJoc[selected_row][selected_col] in Finish_right and TablaJoc[5][9] == 34:
                if WhereIsTheGold[2] == 27:
                    TablaJoc[5][9] = 27
                    state = "WIN"
                if WhereIsTheGold[2] == 29:
                    TablaJoc[5][9] = 40

    if selected_row == 6:
        if selected_col == 9:
            if TablaJoc[selected_row][selected_col] in Finish_down and TablaJoc[5][9] == 34:
                if WhereIsTheGold[2] == 27:
                    TablaJoc[5][9] = 27
                    state = "WIN"





import random


for i in range(0, 2):
    print("i = ", i)

