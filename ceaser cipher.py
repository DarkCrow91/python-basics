art_logo=logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(art_logo)
print("Welcome to the Caesar Cipher program!\n")

print("#note i dont know but first time it doesnt work for some reason, but second time it works fine,\n i think its because of the input function, so just run it twice and it will work fine\n")
alphabet=['a','b','c','d','e','f','g','h','i',
          'j','k','l','m','n','o','p','q','r','s','t'
          ,'u','v','w','x','y','z']

direction=input("type'encode' to encode,type'decode' for decode\n").lower()
text=input("type your message:\n").lower()
shift=int(input("type the shift number: \n"))

def caeser(original_text,shift_amount,encode_or_decode):
    output_text=""
    if encode_or_decode=="decode":
                shift_amount *= -1
                
    for letter in original_text:
        
        if letter not in alphabet:
            output_text += letter
        else:
            

        
            shifted_position=alphabet.index(letter)+shift_amount
            shifted_position%=len(alphabet)
            output_text+=alphabet[shifted_position]

    print(f"here is {encode_or_decode}d message= {output_text}")


should_countinue= True

while should_countinue:

    direction=input("type'encode' to encode,type'decode' for decode\n").lower()
    text=input("type your message:\n").lower()
    shift=int(input("type the shift number: \n"))




    
    caeser(original_text=text,shift_amount=shift,encode_or_decode=direction)

    restart=input("type 'yes' if you want to continue, otherwise type'no'\n").lower()
    if restart=="no":
        should_countinue=False
        print("goodbye")
