def kiemtrasoNT(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

number = int(input('Nhập một số nguyên: '))
if kiemtrasoNT(number):
    print(number, 'là số nguyên tố')
else:
    print(number, 'không phải là số nguyên tố')