def main():

    czy_koniec = False
    while not czy_koniec:
        liczba_A = int(input("podaj liczbę A: "))
        liczba_B = int(input("podaj lizbę B: "))
        działanie = input("podaj znak działania matematycznego :")

        if działanie == "+":
            print(liczba_A + liczba_B)
        elif działanie == "-":
            print(liczba_A - liczba_B)
        elif działanie == "*":
            print(liczba_A*liczba_B)
        elif działanie == "/":
            print(liczba_A/liczba_B)
        elif działanie == "//":
            print(liczba_A//liczba_B)
        else:
            print(liczba_A%liczba_B)

        czy_kolejne = input("Czy chcesz wykonać kolejne działania? t lub n")
        if czy_kolejne == "n":
            czy_koniec = True
        elif czy_kolejne == "t":
            czy_koniec = False
        else:
            print("Nie odpowiedia komenda")
            break

if __name__ == "__main__":
    main()

