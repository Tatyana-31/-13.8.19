tickets = int(input("Введите количество билетов, которое хотите приобрести на мероприятие:"))
age = list(map(int, input("Укажите через пробел возраст посетителей: ")))
price = int(input())
if 0 <= age <= 18:
    print("0")
elif 18 <= age <= 25:
    print("990")
elif age >= 25:
    print("1390")
if tickets > 3:
    print("Сумма к оплате с учетом скидки: ", sum(price) - ((sum(price) / 100) * 10), "рублей")
else:
    print("Сумма к оплате: ", sum(price), "рублей")

