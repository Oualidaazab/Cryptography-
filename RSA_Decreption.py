
from sympy import mod_inverse
#add encryption function 
def Encryption(plain_text) : 
    e=65537
    plain_text = int(input("enter the number that you want to encrypted") 
    #cypher_text =message**e mod(public_key) 
    #generate a public_key  public_key=p*q 
    p=int(input("enter the first prime number") 
    q=int(input("Enter the secand prime number ") 
    public_key =p*q 
    #encrypte the plain_text  
    cypher_text=plain_text**mod(public_key)  
    return "the cypher_text  is {cyber_text} " 
    
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




    


