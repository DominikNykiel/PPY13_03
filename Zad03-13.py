#Zad1

a = b = c = "tekst"
print("Wyswietlam wszystkie zmienne:")
print(a)
print(b)
print(c)
print("Porównuję pierwszą z drugą i druga z trzecią")
print(a == b)
print(b == c)

print("Typ i id obiektu a:")
print(type(a), " : ", hex(id(a)))
print("Typ i id obiektu b:")
print(type(a), " : ", hex(id(a)))
print("Typ i id obiektu c:")
print(type(a), " : ", hex(id(a)))

print("\nZamieniamy wartość trzeciej zmiennej na Java11\n")

print("Porównuję pierwszą z drugą i druga z trzecią")

c = "Java11"

print(a == b)
print(b == c)

print("Typ i id obiektu a:")
print(type(a), " : ", hex(id(a)))
print("Typ i id obiektu b:")
print(type(a), " : ", hex(id(a)))
print("Typ i id obiektu c:")
print(type(a), " : ", hex(id(a)))

# Zad2
import sys

quotient1 = input("Podaj pierwszą liczbę\n")

try:
    a = int(quotient1)
except ValueError:
    try:
        a = float(quotient1)
    except ValueError:
        print("Nieprawidłowa liczba")
        sys.exit()
quotient2 = input("Podaj drugą liczbę\n")

try:
    a = int(quotient2)
except ValueError:
    try:
        a = float(quotient2)
    except ValueError:
        print("Nieprawidłowa liczba")
        sys.exit()

calcsym = input("Podaj znak działania\n")
print(quotient1, calcsym, quotient2, " = ", end=" ")
if calcsym == "+":
    print(float(quotient1) + float(quotient2))
elif calcsym == "-":
    print(float(quotient1) - float(quotient2))
elif calcsym == "*":
    print(float(quotient1) * float(quotient2))
elif calcsym == "/":
    print(float(quotient1) / float(quotient2))
elif calcsym == "//":
    print(float(quotient1) // float(quotient2))
elif calcsym == "%":
    print(float(quotient1) % float(quotient2))
elif calcsym == "**":
    print(float(quotient1) ** float(quotient2))
else:
    print("Nieprawidlowy znak działania!")

# Zad3

dictquest1 = {
    "1": "oglądanie telewizji/filmów/seriali",
    "2": "czytanie książek/czasopism",
    "3": "słuchanie muzyki",
    "4": "spotkania z rodziną/przyjaciółmi",
    "5": "podróżowanie",
    "6": "uprawianie sportu",
}

dictquest2 = {
    "1": "podczas podróży",
    "2": "w czasie wolnym(po pracy, na urlopie)",
    "3": "podczas pracy/nauki(to ich element)",
    "4": "w ogóle nie czytam",
}

dictquest3 = {
    "1": "chęć poszerzenia wiedzy",
    "2": "czytanie mnie relaksuje/odpręża",
    "3": "fakt, że czytanie jest modne",
    "4": "konieczność nauki w związku z wykonywaną pracą/studiami",
    "5": "czytanie to moje hobby",
    "6": "odczuwam presję rodziny/środowiska, żeby czytać",
}

dictquest4 = {
    "1": "papierowej (tradycyjnej)",
    "2": "e-booki(książki elektroniczne) na komputerze",
    "3": "e-booki na tablecie/telefonie",
    "4": "e-booki na specjalnym czytniku(np.Kindle)"
}

#dictquest5 = {
#    "1": "0",
#    "2": "żadnej w całości",
#    "3": "1",
#    "4": "2 lub 3",
#    "5": "4-10",
#    "6": "powyżej 10",
#}
#
#dictquest6 = {
#    "1": "codziennie",
#    "2": "raz w tygodniu",
#    "3": "raz w miesiącu",
#    "4": "raz na kilka miesięcy",
#    "5": "raz na pół roku",
#    "6": "raz na rok",
#    "7": "wcale"
#}
#
#dictquest7 = {
#    "1": "kryminały/thrillery",
#    "2": "romanse",
#    "3": "psychologiczne",
#    "4": "horrory",
#    "5": "naukowe",
#    "6": "dla dzieci i młodzieży",
#    "7": "fantastykę",
#    "8": "biograficzne",
#    "9": "historyczne",
#    "10": "science-fiction",
#    "11": "podróżnicze",
#    "12": "hobbystyczne",
#    "13": "przygodowe",
#    "14": "poezję",
#
#}
imienazwisko = input("pytanie: Jak masz na imię i nazwisko?\n")
print("odpowiedź: ", imienazwisko.title())

print("pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:\n ")

for keys,values in dictquest1.items():
    print(keys)
    print(values)

odp1 = input()

while (dictquest1.get(odp1) == None):
    odp1 = input("Ponownie wprowadz odpowiedż:\n")
print("odpowiedź: ", dictquest1.get(odp1))

print("pytanie: W jakich okolicznościach czytasz książki najczęściej?\n ")

for keys,values in dictquest2.items():
    print(keys)
    print(values)

odp2 = input()

while (dictquest1.get(odp2) == None):
    odp2 = input("Ponownie wprowadz odpowiedz:\n")
print("odpowiedź: ", dictquest2.get(odp2))

print("pytanie: 3 Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? \n")

for keys,values in dictquest3.items():
    print(keys)
    print(values)

odp3 = input()

while (dictquest1.get(odp3) == None):
    odp3 = input("Ponownie wprowadz odpowiedz:\n")
print("odpowiedź: ", dictquest3.get(odp3))

print("pytanie: Po książki w jakiej formie sięgasz najczęściej?\n ")

for keys,values in dictquest4.items():
    print(keys)
    print(values)

odp4 = input()

while (dictquest1.get(odp4) == None):
    odp4 = input("Ponownie wprowadz odpowiedz:\n")
print("odpowiedź: ", dictquest4.get(odp4))

