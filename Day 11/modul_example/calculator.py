"""
    In this program we will import the functinality of ' calfuns ' module.
    MODULE :- Breaking down the same logic code separate pythonfile.
           : Module provides a flaxibility to organize the code in a logical way.
"""
import calfuns as cl

x=10
y=8

addition = cl.add(x,y)
print(addition)

subtraction = cl.sub(x,y)
print(subtraction)

mutliplication = cl.mul(x,y)
print(mutliplication)

divition = cl.div(x,y)
print(divition)