costs=[5,10,3,4]  #this is the coost of each item
items=[0,1,0,1]  #coeficient (if the item is in the container
value=0
value= sum(costs[i] * items[i] for i in range(4))   
print("for this example the total value of the container is : ", value, "$")