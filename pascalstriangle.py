#this program calculates the rows of Pascal's triangle


import inpcon_posint as icpi


while True:
    solution1=[1,1]


    
    inptext='Which row do you want to see?: '
        
    inp=icpi.inputcontrol(inptext)

    
    if inp==0:
        print(1)
        print()
        print()
        continue

    elif inp==1:
        print(solution1)
        print()
        print()
        continue
    
    

    lastlist=solution1


    for l in range(2,inp+1,1):
        nextlist=[]

        for i in range(0,l+1,1):
            
            nextlist.append(1)

        for k in range(1,(len(nextlist)-1),1):
            nextlist[k]=lastlist[k]+lastlist[k-1]

        lastlist=nextlist
        

    print(nextlist)
    print()
    print()







