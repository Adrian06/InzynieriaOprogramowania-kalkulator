def hello(name):
	return "Hello" + str(name)

def podziel(a,b):
	return a/b

def odejmij(a,b):
	return a-b

def dodaj(a,b):
	wynik = float(a) + float(b)
	return wynik

pierwsza  = input()
druga = input()

print(dodaj(pierwsza, druga))
