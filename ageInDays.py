# Read an integer value corresponding to a person's age (in days) and print
# it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

# Note: only to facilitate the calculation, consider the whole year
# with 365 days and 30 days every month. In the cases of test there will
# never be a situation that allows 12 months and some days, like 360, 363 or 364.
# This is just an exercise
# for the purpose of testing simple mathematical reasoning.

idade = int(input("Sua idade em dias: "))

anos = 0
meses = 0
dias = 0

while idade > 0:
    if idade >= 365:
        idade -= 365
        anos += 1
    elif idade >= 30:
        idade -= 30
        meses += 1
    elif idade > 0:
        idade -= 1
        dias += 1

print(anos, 'ano (s)')
print(meses, 'mes (es)')
print(dias, 'dia (s)')
