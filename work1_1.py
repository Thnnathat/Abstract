'''
Number 1
นายธนธัชย์ ชัยพุทธา 6440201561
'''

number = []

def get_number():
    for j in range(10):
        input_number = input("Enter number: ")
        number.append(float(input_number))

def max_number():
    max_num = number[0]
    for i in range(len(number)):
        if number[i] > max_num:
            max_num = number[i]
    return max_num

def min_number():
    min_num = number[0]
    for i in range(len(number)):
        if number[i] < min_num:
            min_num = number[i]
    return min_num

def average():
    s = 0
    for k in range(len(number)):
        s += number[k]
    avg = s/k
    return avg
    
get_number()
max_num = max_number() 
min_num = min_number()
avg = average()
print(f"Max number: {max_num}\nMin number: {min_num}\nAverage: {avg:.2f}")
