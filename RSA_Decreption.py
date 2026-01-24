from sympy import mod_inverse

def Decryption_RSA(c):
    n = int(input("Enter n: "))
    e = int(input("Enter e: "))
    q = int(input("Enter q: "))
    p = int(input("Enter p: "))
   
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)

    m = pow(c, d, n)

    return m   # ← correct way
c = int(input("Enter c:"))
m =Decryption_RSA(c)   
hex_message = hex(m)[2:]  # remove '0x'   
try:
    plaintext = bytes.fromhex(hex_message).decode('utf-8')
except UnicodeDecodeError:
    plaintext = bytes.fromhex(hex_message).decode('utf-8', errors='ignore')
print(f'the plaing text is {plaintext}')  




    


