"""Testing"""
import re

string : str = "hello"
patter : str = "hello"
print(re.match(string, patter))


# * <--- means that after this character can be the same as many time, example ab*c match abbbbbbbbbbbbbbbc
# + <-----  at least once of this caracter
# {}  <-------- this character should be present
# .  <------ anything in between is valid
# ? <-------  this character is optional
# ^ <-------  starts with, example ^an   in any
# []  <----- range of characters [A-Z]
# 


# \b <---- boundaries, at the beginning and the end of the pattern to match, example for emails

# \d <---- means 0 to 9 in r"\d"
# \D <------ every characters that are not numbers
# \w <------- all the characters
# \W <--------   all non characters (spaces and other like !#.) and special cases like \n
# \s <-------   all the white spaces and \t, \n cases
# \S <--------   all the characters without white spaces
# \S+ <--------   all the characters before and after white spaces, example words
# \A <------ match the beginning of the line

# \w* matches zero or more alphanumerica characters



#  re.match search at the beginning of the string
# re.search look for a match in the whole string
# re.findall look for all the match