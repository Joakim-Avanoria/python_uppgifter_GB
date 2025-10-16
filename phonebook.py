phonebook = {}
while True:
    print("1: lägg till")
    print("2: sök")
    print("3: visa alla")
    print("4: ta bort")
    print("0: sluta")

    val = input("> ")

    if val == "1":
        n = input("Namn: ")
        t = input("Tel: ")
        phonebook[n] = t
    elif val == "2":
        n = input("Namn: ")
        print(phonebook.get(n, "Ej hittad"))
    elif val == "3":
        if not phonebook:
            print("Inga kontakter än")
        else:
            for key, val in phonebook.items():
                print(key, ":", val)
    elif val == "4":
        n = input("Namn: ")
        if n in phonebook: del phonebook[n]
        else: print("Ej hittad")
    elif val == "0":
        break