
counter = 100
miles = 1000.0
name = "John"

if counter == 100:
    print("Value of expression is 100")
print("Good Bye!")

while(counter <9):
    print('The count is:',counter)
    counter=counter+1

for letter in 'Python':
    print ('Current Letter',letter)
fruits = ['banana','apple','mango']

for fruit in fruits:
    print ('current fruit: ',fruits)
#Lab1

#Task1:
countryName = input("Enter the country Name: ")
Countries = ["Pakistan","India","Japan","italy","England","Germany"]
AI="Artificial Intelligence"
countrieslen = len(Countries)
x=0
for x in range(countrieslen):
    if countryName in Countries[x]:
    #  Countries[x]== AI
     #   Countries.replace(x,AI)

print(Countries)
#task 2:
Numbers = [5,6,4,2,8,5,9,10,45,26,98,5,3,4,8,25,45,63,5,31,75,14]

print(min(Numbers))
print(sum(Numbers))
Numbers.sort()
print(Numbers)

#task 3
 
def NumbersLessThanTen():
    for x in Numbers:
        if x < 10:
            print(x)

def NumberGreaterThanfourteen():
    for x in Numbers:
        if x > 14:
            print(x)

NumbersLessThanTen()

NumberGreaterThanfourteen()