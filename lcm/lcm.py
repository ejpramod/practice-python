
numb1=6
numb2=5
for val in range(1,numb1*numb2+1):
    if val%numb1==0 and val%numb2==0:
        print("lcm is =",val)
        break