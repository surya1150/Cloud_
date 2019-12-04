s = input("Enter the Name:")
l = s.split()
l2 = []
for i in range(len(l)):
    l2.append(l[i][::-1])
result = ''.join(l2)                
print(l2)
