'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python llt.py
    or if it doesn't work use this one:
        python3 llt.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''


print("                        ***** LLT *****\n\n\n")
while True:
    n=int(input("Enter the exponent : "))
    M=2**n-1
	
    
    
    if n < 3:
        print("Exponent must be greater than two")
    elif n%2==0:
        print("Exponent must be an odd number")
    else:
        s=4
			
        
        ctr=1
        while ctr<=(n-1)//2:
            s=((s**2-2)**2-2)%M
            ctr=ctr+1
        if s==M-2:
            print("2^"+str(n)+"-1 is prime")
        else:
            print("2^"+str(n)+"-1 is composite")
    try_again = ""
    # Loop until users opts to go again or quit
    while not(try_again == "1") and not(try_again == "0"):
        try_again = input("Press 1 to try again, 0 to exit. ")
        if try_again in ["1", "0"]:
            continue  # a valid entry found
        else:
            print("Invalid input- Press 1 to try again, 0 to exit.") 
    # at this point, try_again must be "0" or "1"
    if try_again == "0":
        break 