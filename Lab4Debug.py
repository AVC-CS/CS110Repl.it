"""
	ax2 + bx + c = 1 
 	
    Roots of Quadratic Equation
	x = (-b ± √ (b2 - 4ac) )/2a
"""

# 2x2 + 10x + 2 = 0
# A = 2, B = 10, C = 2
import math

a = 2
b = 10
c = 2

term1 = -b
term2 = b**2 - (4 * a * c)
term2 = math.sqrt(term2)
term3 = 2 * a

x1 = (term1 + term2) / term3
x2 = (term1 - term2) / term3
print(x1, x2)
