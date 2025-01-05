#!/bin/env python3 
from elliptical_curves.elliptical_curve import elliptical_curve
from elliptical_curves.elliptical_curve import point
#.elliptical_curve.elliptical_curve as ec 
def main():
    print("DHEC start")

    p = 17  
    a = 2 
    b = 2
    G = point(5,1)
    n = 10
    h = 10

    alice = elliptical_curve(p,a,b,G,h) 
    bob = elliptical_curve(p,a,b,G,h) 

    #1. 
    print("generate cyclic group") 
    alice.calculate_cyclic_group()
    bob.calculate_cyclic_group()
    
    #2
    input("generate secret")
    alice.generate_secret()
    bob.generate_secret() 

    #3
    input("generate public point")
    alice.calculate_public_point() 
    bob.calculate_public_point() 
    AP = alice.get_public_point()
    BP = bob.get_public_point()
    
    print("Alice: ")
    AP.pr()
    print("Bob: ")
    BP.pr()
   
    
    #4
    input("generate shared secret")
    bob.calculate_shared_Point(AP)
    alice.calculate_shared_Point(BP)
    AS = alice.get_shared_secret_point()
    BS = bob.get_shared_secret_point()
    
    print("Alice: ")
    AS.pr()
    print("Bob: ")
    BS.pr()

    #
    input("shared secret point should be equal")

if __name__ == "__main__":
    main()
