#!/usr/bin/python
############################################################################ 
#####This program takes a string and prints a pyramid by printing first character one time and second character 2 timesetc.. within the number of spaces of length of the given string###
############################################################################
seq="abcdefghijklmnopqrstuvwxyz"
spaces=""
letters_str=""
for letter in seq: #runs for length of seq

    for i in range(1, len(seq) - seq.index(letter)): #uses a backwards for loop to add the number of spaces required and decrease the number of spaces by one each time
        spaces += " " #adds spaces to the list concat_space

    for j in range(0, seq.index(letter) + 1): #uses a forward for loop to add the right letter and number of letters to the triangle
        letters_str += letter #adds letters to the list concat_str

    print spaces + letters_str #joins the spaces and the letters together
    spaces = "" #resets for a new line of the triangle
    letters_str="" #resets for a new line of the triangle
