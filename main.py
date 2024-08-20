def reverse_char(char):
    """
    Reverse a char either lower or capital
    """
    alphabets='abcdefghijklmnopqrstuvwxyz'

    if char in alphabets.upper():
        alphabets=alphabets.upper()
    
    #Return char if not valid alphabet
    if char not in alphabets and char not in alphabets.upper():
        return char 

    #find index of character
    index_of_char=alphabets.index(char)
    opposite_index=(26-index_of_char)

    #find opp char based on opposite index
    opp_char=alphabets[opposite_index-1]

    return opp_char

# print(reverse('a')=='z')
# print(reverse('b')=='y')
# print(reverse('c')=='x')
# x=reverse_char('A')
# print(x)
#git add .
#git commit -m"reverse a single character"
#git push
def atbash(txt):
    reverseTxt=""
    for char in txt:
        reverseTxt+= reverse_char(char)
    return reverseTxt
       
y=atbash("Hello 14")
print(y)