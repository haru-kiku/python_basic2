def calculation_total(numbers):
    total = 0

    for num in numbers: # total = total + num
        total += num
    return total

def calculation_max(numbers):
    max_number = numbers[0]

    for num in numbers[1:]:
        if num > max_number:
            max_number = num
    return max_number

def calculation_min(numbers):
    min_number = numbers[0]

    for num in numbers[1:]:
        if num < min_number:
            min_number = num 
    return min_number
        
def calculation_avg(numbers):
    total = calculation_total(numbers)
    return total // len(numbers)
       


input_deta = input("データを入力してください(スペース区切り)")  # "1 3 5 7"
numbers_str = input_deta.split(" ")  # ["1","3","5","7"]

numbers = []
for num_str in numbers_str:
    int_num = int(num_str)

    numbers.append(int_num)
# [1]
# [1,3]
# [1,3,5]
# numbers = [1,3,5,7]
total = calculation_total(numbers)
maximum = calculation_max(numbers)
minimum = calculation_min(numbers)
average = calculation_avg(numbers)

print(f"合計値: {total}")
print(f"最大値: {maximum}")
print(f"最小値: {minimum}")
print(f"平均値: {average}")
