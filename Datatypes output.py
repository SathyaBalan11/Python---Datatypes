#1 String
quote = "Good Things Take Time"
print("Quote:", quote)
print(type(quote))
#output
Quote: Good Things Take Time
<class 'str'>


#2 List
numbers = ["2","1","0","1"]
print("Numbers:", numbers)
print(type(numbers))
#output
Numbers: ['2', '1', '0', '1']
<class 'list'>


#3 Tuple
colors = ("black","white","pink","black")
print("Colors:", colors)
print(type(colors))
#output
Colors: ('black', 'white', 'pink', 'black')
<class 'tuple'>


#4 Set
veggies = {"carrot","potato","beans","carrot"}
print("Veggies:", veggies)
print(type(veggies))
#output
Veggies: {'potato', 'carrot', 'beans'}
<class 'set'>


#5 Dictionary
candidate = {"name": "Shiva", "course": "Computer Science", "name": "Shiva"}
print("Candidate Details:", candidate)
print(type(candidate))
#output
Candidate Details: {'name': 'Shiva', 'course': 'Computer Science'}
<class 'dict'>



#6 Integer
number = 11.0
print("Number:", number)
print(type(number))
#output
Number: 11
<class 'int'>

#7 Float
price = 20.5
print("Price:", price)
print(type(price))
#output
Price: 20.5
<class 'float'>


#8 Complex
number = 3+4j
print("Number:", number)
print(type(number))
#output
Number: (3+4j)
<class 'complex'>



#9 Range
numbers = range(5)
print("Range:", (numbers))
print(type(numbers))
#output
Range: range(0, 5)
<class 'range'>


#Range
numbers = range(5)
print("Range from 0 to 4:", list(numbers))
print(type(numbers))
#output
Range from 0 to 4: [0, 1, 2, 3, 4]
<class 'range'>



#10 Boolean
children = True
childrens = False
print("Children:", children)
print("Childrens:", childrens)
print(type(children))
#output
Children: True
Childrens: False
<class 'bool'>



#11 None
result = None
print("Result:", result)
print(type(result))
#output
Result: None
<class 'NoneType'>
