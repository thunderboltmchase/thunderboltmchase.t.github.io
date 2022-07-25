def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
         print("False")
         break
    else:
        print("Prime")
        
    
is_prime(18)
