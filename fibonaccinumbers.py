import inpcon_posint as icpi

while True:

    #bug: the zero fibonaccinumber is 0
     inptext='Which Fibonacci number do you want to see?: '
     inp=icpi.inputcontrol(inptext)

     if inp==0:
         print(0)
         print()
         print()
         continue

     erg=[0,1]

     for i in range(0,(inp-1),1):
         zahl=erg[len(erg)-1]+erg[len(erg)-2]
         erg.append(zahl)

     print(erg[len(erg)-1])
     print()
     print()

