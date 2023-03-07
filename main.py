# zad1
print(2**5)
# zad2
print("podaj imie")
imie = input()
print("Witaj " + imie + "!")
# zad3
print(float(input()) + float(input()))
# zad4
print(sum(range(8, 81)))
# zad5
from datetime import date
print(date.fromisoformat("2023-06-06") - date.today())
# zad6
print("podaj pierwszą libczę: ")
a = input()
print("Podaj drugą liczbę")
b = input()
print("""Wybierz opcję działania:
dodawanie: +
odejmowanie: -
mnożenie: *
dzielenie: /""")
x = input()
if x == "+":
    print(int(a) + int(b))
elif x == "-":
    print(int(a) - int(b))
elif x == "*":
    print(int(a) * int(b))
elif x == "/":
    print(float(a) / float(b))
else:
    print("Nie wybrałes odpowiedniego znaku!!")
