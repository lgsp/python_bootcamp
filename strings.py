samp_string = "This is a very important string"
print("Length:", len(samp_string))

print(samp_string[0])
print(samp_string[-1])
print(samp_string[0:4])
print(samp_string[8:])
print("Every Other", samp_string)

# a - z 97 - 122
# A - Z 65 - 90

print("A =", ord("A"))
print("65 =", chr(65))

uppercase_word = input("Enter a word: ").upper()
string_of_unicodes = ""
lowercase_word = ""

for letter in uppercase_word:
    string_of_unicodes += str(ord(letter))
    letter_unicode = str(ord(letter))
    print(letter, "=", letter_unicode)
    lowercase_word += chr(ord(letter) + 32)

print(uppercase_word)
print(string_of_unicodes)
print(lowercase_word)

norm_string = input("Enter a string to hide: ")
secret_string = ""
for char in norm_string:
    secret_string += str(ord(char))
    
print("Secret Message:", secret_string)

norm_string = ""
for i in range(0, len(secret_string) - 1, 2):
    char_code = secret_string[i] + secret_string[i + 1]
    norm_string += chr(int(char_code))
    
print("Original Message:", norm_string)    


norm_string = input("Enter a string to hide: ")
secret_string = ""
for char in norm_string:
    secret_string += str(ord(char) - 23)
    
print("Secret Message:", secret_string)

norm_string = ""
for i in range(0, len(secret_string) - 1, 2):
    char_code = secret_string[i] + secret_string[i + 1]
    norm_string += chr(int(char_code) + 23)
    
print("Original Message:", norm_string)    
