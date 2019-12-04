s1 = input("Enter the First String")
s2 = input("Enter the Second String:")
s3 = ''
n1 = len(s1)
n2 = len(s2)
n = min(n1,n2)
for i in range(n):
    s3 += s1[i] + s2[i]

if n1 > n2:
    s3 += s1[n:n1]
else:
    s3 += s2[n:n2]

print(s3)
