# input control if input is a positive integer 


import sys


def inputcontrol(inptext):
    
    while True:
		
            print('Enter "q" to exit.')
            inp=input(inptext)

	
            if inp=='q':
                sys.exit()


            try:
			
                inp=int(inp)


            except:
                print()
                print('Error: Please enter an integer.')
                print()
                continue

            if inp<0:
                
                print()
                print('Error: Your number is smaller than zero!')
                print()
                continue

			
            return inp

