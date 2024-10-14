numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

oddeven = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(oddeven)

numbers2 = [1,2,3,4,5,6,7,8,9,10]

threemul= [num for num in numbers2 if num%3==0 ]
print(threemul)