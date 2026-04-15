def xor(string , key  ): 
    flag ='' 
    for c in string : 
         flag +=chr(ord(c)^key) 
    return  f'the flag is : 'f'crypto{"{"}' +flag + f'{'}'}' 
print(xor("label",13)) 
#print(''.join(chr(ord(c) ^ 13) for c in 'label')) 
""" 

Given the string label, XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}.
The Python pwntools library has a convenient xor() function that can XOR together data of different types and lengths. But first, you may want to implement your own function to solve this.
"""
# chr(Number) chr function convert number to character  
# ord (character) ord is function convert character to number 