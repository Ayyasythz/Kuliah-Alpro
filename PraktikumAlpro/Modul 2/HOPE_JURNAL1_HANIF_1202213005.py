peran = ["anjing","kucing","tikus"]
player1 = str(input("Masukan Peran Player 1 : ")).lower()
player2 = str(input("Masukan Peran Player 2 : ")).lower()
print("========================================================")
if player1 == "anjing":
    if player2 == "anjing":
        print("Game Seri")
    elif player2 == "kucing":
        print("Player 1 Menang")
    elif player2 == "tikus":
        print("Player 2 Menang")
    else:
        print("Player 2 Salah memilih peran")
elif player1 == "kucing":
    if player2 == "anjing":
        print("Player 2 Menang")
    elif player2 == "kucing":
        print("Game Seri")
    elif player2 == "tikus":
        print("Player 1 Menang")
    else:
        print("Player 2 Salah memilih peran")
elif player1 == "tikus":
    if player2 == "anjing":
        print("Player 1 Menang")
    elif player2 == "kucing":
        print("Player 2 Menang")
    elif player2 == "tikus":
        print("Game Seri")
    else:
        print("Player 2 Salah memilih peran")
else:
    print("Player 1 Salah Memilih peran")