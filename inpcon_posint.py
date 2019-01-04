# input control if input is a positive integer 


import sys


def inputcontrol(inptext):
    
    while True:
		
            print('Enter "q" to exit.')
            print('Please enter a positive integer.')
            print()
            inp=input(inptext)

	
            if inp=='q':
                sys.exit()


            try:
			
                inp=int(inp)


            except:
                print()
                print('Error: Please enter a positive integer.')
                print()
                print()
                continue

            if inp<0:
                
                print()
                print('Error: Your integer is smaller than zero! Please enter a positive one.')
                print()
                print()
                continue

			
            return inp

