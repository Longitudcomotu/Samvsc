a=["master","online"]

a.insert(1,"code")

for element in a:
    print (element)
    
    
c=[4,5,6]
d= [1,2,3]

c.insert(0,d)

print(c)
    
    
company=["Ulises","Raafa","Javier"]

company.sort()
print(company)
    
company.sort(reverse=True)

print(company)

company.sort(reverse=True, key=len)