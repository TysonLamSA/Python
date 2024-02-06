#iterable in Python
num = [1,2,3,4,5,6,7,8,9,10]
print(num)
num1 = [x**2 for x in num]
print(num1)

#Assign in tuples
tup = ("21st","Jan",1990)
print(type(tup))
day, month, year = tup
print(day)
print(month)
print(year)


people = [
    ('George', 'Larry','Tymme'),
    ('Abotris','Hyme','SpaceQ'),
    ('Monocla','Hyst','Aswquire'),
    ('Trenble','Leo','Hyratreo')]
for first_name, last_name, org in people:
    print("{} {}".format(first_name, last_name))
    
people1 = [
    ('Joe', 'Schmoe','Burbank','CA'),
    ('Mary','Rattburger','Madison','WI'),
    ('Jose','Ramirez','Ames','IA')]
    
print(people1[0])
print(people1[1])
print(people1[2])
def person_record(first_name1,last_name1,city,state):
    print("{} {} live in {}, {}".format(first_name1,last_name1,city,state))
for person in people1:
    person_record(*person)
    
#Sorted => list
#Sorted using key => For example:
#def ignore_case(item):
#   return item.lower()
#  => Ignore whether upper or lower case. Sort the list.

#Function 1: Sort fruit
fruit = [
    'Apple',
    'lime',
    'pagaya',
    'pear',
    'Tamarind',
    'persimmon',
    'Elderberry',
    'lychee',
    'banana',
    'FIG',
    'BLUEberry',
    'date',
    'Kiwi',
    'Watermelon',
    'Elemon',
    'Kat',
    'Lemon']
print(sorted(fruit))

#Function 2: Skip Upper or Lower case
def ignore_case(item):
    return item.lower()
fruit1 = sorted(fruit, key=ignore_case)
print(fruit1)

#Function 3: Sort by length then name
def ignore_length_and_upperlower(item):
    return (len(item), item.lower())
fruit2 = sorted(fruit, key=ignore_length_and_upperlower)
print(fruit2)


#lambda

addFive = lambda x : x + 5
print(addFive(2))
print(addFive(60))

addTwoNums = lambda x,y : x+y
print(addTwoNums(20,40))

printResult = lambda func, val : print(func(val))
printResult(addFive, 15)
