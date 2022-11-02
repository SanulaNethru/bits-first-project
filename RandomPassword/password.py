import random

characters= ['!','@','#','$','%','^','&','*','+',':','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h']
lenght = int (input ('number of characters'))

random.shuffle(characters) #feature of the random function
char = (characters[0:lenght]) #index out first character to the lenght entered charjoint = ''.join(char) #joins the individual elements of char into one string print (charjoint)
