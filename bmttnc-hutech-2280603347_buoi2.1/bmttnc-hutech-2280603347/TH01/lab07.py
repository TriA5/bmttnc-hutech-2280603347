#nhập các dòng từ người dùng
print('Nhập các dòng từ người dùng:')
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print('Các dòng đã nhập:')
for line in lines:
    print(line.upper())