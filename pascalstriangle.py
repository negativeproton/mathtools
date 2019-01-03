#this program calculates the rows of Pascal's triangle

import sys

while True:
    solution1=[1,1]

    j=False
    while j==False:

        print('Enter "q" to exit.')
        inp=input('Which row do you want to see?: ')
        if inp=='q':
            sys.exit()


        try:
            
            inp=int(inp)

            if inp<0:
                print()
                print('Error: Your number is smaller than zero!')
                print()
                continue

            j=True
            
        except:
            print()
            print('Error: Please enter an integer.')
            print()

    if inp==0:
        print(1)
        print()
        print()

    elif inp==1:
        print(solution1)
        print()
        print()


    else:

        lastlist=solution1


        for l in range(2,inp+1,1):
            
            nextlist=[]

            for i in range(0,l+1,1):
                nextlist.append(1)

            for k in range(1,(len(nextlist)-1),1):
                nextlist[k]=lastlist[k]+lastlist[k-1]

            lastlist=nextlist
        

        print (nextlist)
        print()
        print()

        



