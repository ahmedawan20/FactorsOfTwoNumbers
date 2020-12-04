C= int(input("Please enter a number C:"))
D= int(input("Please enter a number D:"))

for i in range(1,C+1):
    if C%i==0:
        print(i,"is a factor of",C)

        
for i in range(1,D+1):
    if D%i==0:
        print(i,"is a factor of", D)
