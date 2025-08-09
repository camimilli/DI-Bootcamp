# # Import the whole module 
# import operators

# print(operators.addOperator(5,10))
# print(operators.addOperator(10,2))


# # Import specific functions
# from operators import addOperator, divideOperator

# print(addOperator(5,10))
# print(addOperator(10,2))

# Import using alias 
import operators as op 

print(op.addOperator(5,10))
print(op.divideOperator(10,2))