def reverse_char(char):
    """
    Reverse a char either lower or capital
    """
    alphabets='abcdefghijklmnopqrstuvwxyz'

    if char in alphabets.upper():
        alphabets=alphabets.upper()

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
def atbash(txt):
    for char in txt:
        print(char)

atbash("Hello")