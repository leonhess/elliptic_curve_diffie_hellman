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
    curve = elliptical_curve(p,a,b,G,h) 
    
    curve.calculate_cyclic_group()
    curve.generate_secret()
    curve.calculate_secret_point() 
    # receive public point of bob 
    AP = point(10,6)

    curve.calculate_shared_Point(AP)

if __name__ == "__main__":
    main()
