# capital letters to small

def conversion(letter):
    ascii_value=ord(letter)
    if ascii_value<97:
        ascii_value=ascii_value+32
        return chr(ascii_value)
    else:
        ascii_value=ascii_value-32
        return chr(ascii_value)
    
c=conversion('a')    
print(c)