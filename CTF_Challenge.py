from string import ascii_lowercase, ascii_uppercase

flag = open('flag.txt', 'r').read().strip()
msg = "You've solved the beginner crypto challenge! The flag is {}. Now get out some pen and paper for the rest of them, they won't all be this easy :).".format(flag)

def eNCryPt(msg):
    out = ''
    for i, c in enumerate(msg):
        if c in ascii_lowercase:
            alph = ascii_lowercase
            
        elif c in ascii_uppercase:
            alph = ascii_uppercase 
            
            
        else:
            out += c
            continue
        out += alph[(alph.index(c) + i) % len(alph)] #0+1%26 1mod(26) 

    return out

print(eNCryPt(msg)) 
#function decrypt   
def  Decrypt(ct): 
    out ='' 
    for x,y in enumerate(ct) : 
        if y in ascii_lowercase : 
            alph=ascii_lowercase 
        elif y in ascii_uppercase : 
            alph =ascii_uppercase 
        else : 
            out +=y
            continue 
        out+=alph[(alph.index(y)-x) % len(alph)] 
    return out  

print(Decrypt("Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv tahtrn{dbci_rez_0011}. Pra mlb yff gdcv iyi xlc qcsiw mwa etr gujl ia qfdm, wlje exx'f oab tx odfq ebub :).")) 
    
# output  : 
#Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv tahtrn{dbci_rez_0011}. Pra mlb yff gdcv iyi xlc qcsiw mwa etr gujl ia qfdm, wlje exx'f oab tx odfq ebub :) 
#plain text  
# You've solved the beginner crypto challenge! The flag is oualid{root_amg_0011}. Now get out some pen and paper for the rest of them, they won't all be this easy 
 