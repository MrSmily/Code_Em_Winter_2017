#Dimension
dimensions = (20, 50)

print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 270

for Dude in dimensions:
    print(Dude)

print(str(dimensions[0])+"x"+str(dimensions[1]))
print()
for i in range(dimensions[1]-2):
    print("x"+(dimensions[0]-2)*""+"x")
print("x"* dimensions[0])
