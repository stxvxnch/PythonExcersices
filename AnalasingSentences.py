from itertools import count

print("Willkommen zum Textanalyse-Tool!")
text = input("Gib deinen Text ein: ")

def get_zeichen_with_leerzeichen():
    print(" - Zeichen (inkl. Leerzeichen): " + str(len(text)))

def get_zeichen_without_leerzeichen():
    count = 0
    for character in text:
        if character == " ":
            continue
        else:
            count += 1

    print(" - Zeichen (ohne Leerzeichen): " + str(count))

print("Analyse abgeschlossen")
get_zeichen_with_leerzeichen()
get_zeichen_without_leerzeichen()


