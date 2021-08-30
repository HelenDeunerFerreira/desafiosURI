# You, who is a Jade's friend and a Computer Science student, decided to make a small program that,
# based on her analise made in the last two nights, informs the phase in which the moon is.
# If the visible portion of the moon is between 0 and 2%, for example, is new moon ("nova" in portuguese).
# If it is between 3 and 96% is crescent moon ("crescente" in portuguese), if it is between 97 and 100%
# is full moon ("cheia" in portuguese) and it is between 3 and 96 % (decreasing) is waning moon
# ("minguante" in portuguese).

# The input consists of a single line containing two integer numbers.
# The first number corresponds to the percentage observed by Jade at night two days ago.
# The second value corresponds to the percentage observed by jade the night before.

dias = input()


def luas1():
    num1 = ''
    if dias > '':
        for i in range(0, len(dias), 1):
            if dias[i] == ' ':
                break
            else:
                num1 += dias[i]
    if num1 > '':
        return int(num1)
    else:
        return 0


def luas2():
    num2 = ''
    if dias > '':
        for i in range(0, len(dias), 1):
            if dias[i] == ' ':
                x = i + 1
                for x in range(x, len(dias), 1):
                    num2 += dias[x]
    if num2 > '':
        return int(num2)
    else:
        return 0


dia1 = luas1()
dia2 = luas2()

if dia1 < dia2:
    if dia2 <= 2:
        print('nova')
    elif 2 <= dia2 <= 96:
        print('crescente')
    elif (97 <= dia2 <= 100):
        print('cheia')
else:
    if dia2 <= 2:
        print('nova')
    elif 2 <= dia2 <= 96:
        print('minguante')
    elif (97 <= dia2 <= 100):
        print('cheia')
