# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())

# print(name)
# print(score)

li = [] 
n = int(input("Enter the number of elements: "))
for i in range(1, n+1): 
    elem = int(input("Enter the elements: ")) 
    li.append(elem) 
li.sort() 

print("The sorted list: ", li) 
print("The second smallest value of this list: ",li[1])