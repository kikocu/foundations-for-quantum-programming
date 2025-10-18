costs=[5,10,3,4]  #this is the coost of each item
items=[0,1,0,1]  #coeficient (if the item is in the container
value=0
for i in range(4):          # Loop from 0 to 3 (Python is 0-indexed)
    value += costs[i] * items[i]
         
print("for this example the total value of the container is : ", value, "$")