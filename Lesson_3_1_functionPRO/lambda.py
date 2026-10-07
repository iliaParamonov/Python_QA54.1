def double(x):
    return x*2

double_lambda = lambda x:x*2
double_lambda2 = lambda x:x*2 if x>0 else -x

print(double(4))
print(double_lambda(4))
print(double_lambda2(-2))

print()

add = lambda x,y:x+y
print(add(3,4))

is_even = lambda p: p%2==0
print(is_even(8))
print(is_even(5))

def double(x):
    return x*2

double_lambda = lambda x:x*2
double_lambda2 = lambda x:x*2 if x>0 else -x

print(double(4))
print(double_lambda(4))
print(double_lambda2(-2))

print()
add = lambda x,y:x+y
print(add(3,4))

is_even = lambda p: p%2==0
print(is_even(8))
print(is_even(5))

grades = [90,75,88,63,100,81]
even = list(filter(lambda x:x%2==0,grades))
odd = list(filter(lambda x:x%2!=0,grades))

print("четные оцнки: ",even)
print("нечетные оценки: ",odd)
print()

numbers = [1,2,3,4,5,6]

squ = map(lambda x:x**2,numbers)
print(squ)
print(list(squ))
print()

def to_upper(s):
    return  s.upper()
status = ["passed","failed","skip"]
upper_status = list(map(to_upper,status))
print(upper_status)