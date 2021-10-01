# n=int(input("Введите количество измерений: "))
# for i in range(1,n):
#     a=int(input(""))
#     print(i,"измерение: ",a)


measurements = []

measurements_number = int(input("Введите количество измерений электрических сопротивлений: "))
for i in range(measurements_number):
    print("Введите измерение: ", end='')
    measurements.append(float(input()))

print()

for index, measurement in enumerate(measurements, 1):
    print(f'Measurement #{index} R = {measurement} ohms')
