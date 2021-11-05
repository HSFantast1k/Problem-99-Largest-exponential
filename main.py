max_number_base = [0, 0]
numbers_power_count = 0
max_number_count = 0
with open('p099_base_exp.txt') as base:
    for line in base:
        numbers_power_count += 1
        numbers_power = line.replace('\n', '').split(',')
        number = int(numbers_power[0])
        power_number = int(numbers_power[1])
        if number ** power_number > max_number_base[0] ** max_number_base[1]:
            max_number_count = numbers_power_count
            max_number_base = [number, power_number]
            print(f"Max_number {max_number_count}")
        else:
            print(f"Обработано чисел {numbers_power_count}")
