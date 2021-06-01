

giliran = 0
x_menang, o_menang = False, False
angka_terpilih = ''
player = "X"
angka_menang = (
    (1, 2, 3), (4, 5, 6), (7, 8, 9), 
    (1, 4, 7), (2, 5, 8), (3, 6, 9), 
    (1, 5, 9), (3, 5, 7))
angka_x = []
angka_o = []

# Judul permainan
print("--- Tic Tac Toe --- \nTekan \"ctrl + c\" untuk keluar")

while True:
    print('')
    for i in range(1, 10):
        # Mengganti angka terpilih dengan huruf "X" atau "O"
        if i in angka_x:
            print(f"X ", end='')
        elif i in angka_o:
            print(f"O ", end='')
        else:
            print(f"{i} ", end='')

        if i % 3 != 0:
            print("| ", end='')
        else:
            if i != 9:
                print('')
                for _ in range(3):
                    print('---', end='')
            print('')

    if x_menang:
        print("Player X menang !")
        break
    elif o_menang:
        print("Player O menang !")
        break

    # Menghentikan permainan jika semua angka terisi
    if giliran == 9:
        print("Permainan seri !")
        break

    try:
        angka_terpilih = int(input(f"Giliran {player}, pilih salah satu angka: "))
        if not 0 < angka_terpilih < 10:
            print("\nAngka yang dipilih tidak tersedia !")
            continue
    except ValueError:
        print("\nMohon masukan angka !")
        continue
    except KeyboardInterrupt:
        print("\nAyo coba lagi !")
        break

    giliran += 1

    # Mengganti player dan menambah angka terpilih
    if player == 'X':
        # Menambahkan angka terpilih dari X
        if angka_terpilih in angka_x:
            print("\nAngka yang dipilih tidak tersedia !")
            continue
        else:
            angka_x.append(angka_terpilih)
        # Mengecek apakah ada player yang menang
        for i in angka_menang:
            x_menang = True
            for j in i:
                if j not in angka_x:
                    x_menang = False
                    break
            if x_menang:
                break
        # Mengganti giliran player ke "O"
        player = 'O'
    elif player == 'O':
        # Menambahkan angka terpilih dari X
        if angka_terpilih in angka_x:
            print("\nAngka yang dipilih tidak tersedia !")
            continue
        else:
            angka_o.append(angka_terpilih)
        # Mengecek apakah ada player yang menang
        for i in angka_menang:
            o_menang = True
            for j in i:
                if j not in angka_o:
                    o_menang = False
                    break
            if o_menang:
                break
        # Mengganti giliran player ke "O"
        player = 'X'