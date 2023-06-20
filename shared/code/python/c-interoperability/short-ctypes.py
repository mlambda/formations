import ctypes
 
clibrary = ctypes.CDLL('clibrary.so')
 
addTwoNumbers = clibrary.add
addTwoNumbers.argtypes = [ctypes.c_int, ctypes.c_int]
addTwoNumbers.restype = ctypes.c_int
 
print("Sum of two numbers is :", addTwoNumbers(20, 10))