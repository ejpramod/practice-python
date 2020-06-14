while True:
    print("/********* FACTORIAL*********/")
    numb=eval(input("enter the factorial number="))
    for val in range(1,numb):
      numb=numb*val
    print(numb)