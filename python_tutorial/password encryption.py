passwordOut=""
case_changer=ord('a')-ord('A')
encryption_key=(('a','z'),('b','y'),('c','x'),('d','w'),('e','v'),('f','u'),('g','t')
                ,('h','s'),('i','r'),('j','q'),('k','p'),('l','o'),('m','n'),('n','m')
                ,('o','l'),('p','k'),('q','j'),('r','i'),('s','h'),('t','g'),('u','f')
                ,('v','e'),('w','d'),('x','c'),('y','b'),('z','a'))

print("this prog will encrypt and decrypt user password")

which=input("enter (e) to encrypt the passwprd and (d) to decrypt the password")

while which!='d' and which!='e':
    which=input("\n INVALID, enter valid details. enter (e) to encrypt the passwprd and (d) to decrypt the password")
encrypting = (which=='e')#assign true or false
    



password_in=input("enter password:  ")
if encrypting:
    from_index=0
    to_index=1
else:
    from_index=1
    to_index=0
    
case_changer=ord('a')-ord('A')

for ch in password_in:
    letter_found= False
    
    for t in encryption_key:
        if('a'<=ch and ch<='z') and ch==t[from_index]:
            passwordOut=passwordOut+t[to_index]
            letter_found=True
        elif('a'<=ch and ch<='z') and chr(ord(ch)+32)==t[from_index]:
            passwordOut=passwordOut+chr(ord(t([to_index])))-case_changer
            letter_found=True
            
    if not letter_found:
        passwordOut=passwordOut+ch
if encrypting:
    print("your encryptd password is: ",passwordOut)
else:
    print("your decrypted password is: ",passwordOut)
    