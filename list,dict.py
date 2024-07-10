l=[('name','sachin'),('age',20),('course','data science')]
d=dict(l)
print(d)
print(d['name'])
print(d.get('name')) #values , keys or all keyword dont use in variable
d['name']='don'   # in - keywords
print(d['name'])
print('don' in d.values())


d=dict(name='schin',age=30,course='data science')
print(d)

#delete ,pop,popitem
keys=['name','age','course']
values=['sachin',32,'data science']
l=dict(zip(keys,values))
print(l)
x = l.pop('course')
print(l)
print(x)
y=l.popitem()
print(y)
print(l)



keys=['a','s','c']
defualtvalue=0
d=dict.fromkeys(keys,defualtvalue)#fromkeys
print(d)


d={'name':'sachin', 'job': 'data analyst', 'age':20}
for x in d:
    print(d[x])

l=d.items()
print(l)



#(1,3,2) - tuple
#[1,1,1] - list
l1=[1,2,3,4,5,6]
l2=[(i,(i**2))for i in l1 if i%2==0]
print(l2)
l1=[1,2,3,4,5,6]
l2=[(i**2)for i in l1 if i%2==0]
print(l2)

x, y, z, n = (int(input()) for _ in range(4))

# Generate all possible coordinates using list comprehension
coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

# Filter out the coordinates where the sum is not equal to n
filtered_coordinates = [coord for coord in coordinates if sum(coord) != n]

print(filtered_coordinates)

str='sachin'
print(str)

list1=[1,2,3,4,5]
list2=[2,5,'true',True]
list1.append(list2)
print(list1)
print(list1[5][3])
list1.insert(3,10)
print(list1)

new_list=[1,2,3,4,5,[2,5,[1,4,5],'true',True]]
new_list[5][2].append(8)
print(new_list)
print(new_list[::-1])

def poly(n):
    i=[]
    for i in n:
        if i == i[::-1]:
            print('poly')
        else:
            print('not poly')
list1=['madam', 'vara', 'madam', 'sachin']

print(poly(list1))


a=[1,2,3,4,5,6,7]
b=[2,4,65,6,6,5,5]
print(max(a,b))

a.reverse()
print(a)

new_list=[1,2,3,4,5,[2,5,[1,4,5],'true',True]]
print(new_list[5][3].upper())
new_list.remove(2) #remove mention a remove element
new_list.pop(0)
print(new_list)
#same for insert and append

list1=[]
list2=[]
while True:
    a=input('enter a name and enter done if it finsih')
    list1.append(a)
    if a.lower() == 'done':
        break
while True:
    b=input('enter a name if u need to remove any name or done to finsh')
    list1.remove(b)
    list2.append(b)
    if b.lower() == 'done':
        break
print('list1=', list1)
print('list2=', list2)
