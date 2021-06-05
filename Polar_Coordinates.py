Sample Input:
  1+2j
  
Sample Output

 2.23606797749979 
 1.1071487177940904

Note: The output should be correct up to 3 decimal places.
import cmath
import math

eq = input()
pa = cmath.phase(complex(eq))
r = abs(complex(eq))

print("{0}\n{1}".format(r,pa))
