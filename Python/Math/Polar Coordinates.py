from cmath import polar

z = complex(input())
[print(i) for i in (polar(complex(z.real, z.imag)))]
