class Latin:
    def latinN(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


while True:
    num = int(input("Δωσε αριθμο απο το 1 - 100000: "))
    if 0 >= num or num > 100000:
        print("O αριθμος που δωσατε δεν ειναι μεσα στις προδιαγραφες.")
        num = int(input("Δωστε αριθμο απο το 1 - 100000: "))
    else:
        break

print(Latin().latinN(num))