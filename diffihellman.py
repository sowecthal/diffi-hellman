from random import randint
from sympy import isprime
from sympy.ntheory.residue_ntheory import primitive_root
from sympy.ntheory.generate import randprime
from simplecrypt import encrypt, decrypt

message = input("Enter message: ")

P = randprime(10**58, 10**59)
while not (((P - 1) % 2 == 0) and isprime((P - 1) // 2)):
    P = randprime(10**58, 10**59)
    G = primitive_root(P)	
print ("P : ", P, "\nG : ", G)

		
a_private_number = randint(10**58, 10**59)
print("Private key a: ", a_private_number)

b_private_number = randint(10**58, 10**59)
print("Private key b: ", b_private_number) 
 
a_open_number = pow(G, a_private_number, P)
print("Open key A: ", a_open_number)

b_open_number = pow(G, b_private_number, P)
print("Open key B: ", b_open_number)

a_shared_key = pow(a_open_number, b_private_number, P)
print("Secret key A: ", a_shared_key)

b_shared_key = pow(b_open_number, a_private_number, P)
print("Secret key B: ", b_shared_key)


enc_secret_key = encrypt(str(a_shared_key), message)
print("Encrypted msg: ", enc_secret_key)
 
dec_secret_key =  decrypt(str(a_shared_key), enc_secret_key).decode()
print("Decrypted msg: ", dec_secret_key)
		
 

 


 
