def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

print(is_palindrome("Anita lava la tina")) 
print(is_palindrome("hola como estas"))   
