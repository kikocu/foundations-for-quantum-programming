costs=[5,10,3,4]  #this is the coost of each item
items=[0,1,0,1]  #coeficient (if the item is in the container
valor=0
for i in range(len(items)):
        valor=valor + (-items[i] * costs[i])
print(valor)