# In this problem you have to read an integer value and calculate the smallest possible number of
# banknotes in which the value may be decomposed.
# The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.


import sys


def verificaValor():
    global valorSaque
    valorSaque = int(input())
    if valorSaque >= 1 and valorSaque <= 1000000:
        print(valorSaque)
    else:
        sys.exit(0)
    return valorSaque


verificaValor()

contador1 = 0
contador2 = 0
contador5 = 0
contador10 = 0
contador20 = 0
contador50 = 0
contador100 = 0

while valorSaque > 0:
    if valorSaque >= 100:
        contador100 = contador100 + 1
        valorSaque -= 100
    elif valorSaque >= 50:
        contador50 = contador50 + 1
        valorSaque -= 50
    elif valorSaque >= 20:
        contador20 = contador20 + 1
        valorSaque -= 20
    elif valorSaque >= 10:
        contador10 = contador10 + 1
        valorSaque -= 10
    elif valorSaque >= 5:
        contador5 = contador5 + 1
        valorSaque -= 5
    elif valorSaque >= 2:
        contador2 = contador2 + 1
        valorSaque -= 2
    elif valorSaque >= 1:
        contador1 = contador1 + 1
        valorSaque -= 1


def notasSaque():
    print(contador100, "nota(s) de R$ 100,00")
    print(contador50, "nota(s) de R$ 50,00")
    print(contador20, "nota(s) de R$ 20,00")
    print(contador10, "nota(s) de R$ 10,00")
    print(contador5, "nota(s) de R$ 5,00")
    print(contador2, "nota(s) de R$ 2,00")
    print(contador1, "nota(s) de R$ 1,00")


notasSaque()


# num = int(input())
# print(num)
# print("{} nota(s) de R$ 100,00".format(int(num/100)))
# ans = num % 100
# print("{} nota(s) de R$ 50,00".format(int(ans/50)))
# ans = ans % 50
# print("{} nota(s) de R$ 20,00".format(int(ans/20)))
# ans = ans % 20
# print("{} nota(s) de R$ 10,00".format(int(ans/10)))
# ans = ans % 10
# print("{} nota(s) de R$ 5,00".format(int(ans/5)))
# ans = ans % 5
# print("{} nota(s) de R$ 2,00".format(int(ans/2)))
# ans = ans % 2
# print("{} nota(s) de R$ 1,00".format(int(ans/1)))
