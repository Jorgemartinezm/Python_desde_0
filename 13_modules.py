### Modules ###

import modules #! Propio

modules.sumValue(5, 3)
modules.printValue("Hola Python")

from modules import sumValue, printValue #! Propio

sumValue(3, 5)
printValue("Hola Python")

import math #! Del propio python

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE

print(PI_VALUE)