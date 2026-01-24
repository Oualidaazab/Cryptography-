
from sympy import mod_inverse

def Decryption_RSA(c):
    n = int(input("Enter public key n : ")) 
    e = int(input("Enter the public tgexponent : "))
    q = int(input("Enter the first prim number q : "))
    p = int(input("Enter the secand prim number p : "))
   # totion n (phi) 
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
   # the plaintext 
    m = pow(c, d, n)

    return m  
c = int(input("Enter c:")) # CipherText
m =Decryption_RSA(c)   
hex_message = hex(m)[2:]    # change m to hex 
try:
    plaintext = bytes.fromhex(hex_message).decode('utf-8')  
except UnicodeDecodeError:
    plaintext = bytes.fromhex(hex_message).decode('utf-8', errors='ignore')
print(f'the plaing text is {plaintext}')  




    


