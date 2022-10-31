#10/31/2022 Class, #Cody Brown

#Counting characters in a word
def histogram(word):
    d = dict()
    for char in word:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

histogram('animal')
#this gives {'a': 2, 'n': 1, 'i': 1, 'm': 1, 'l': 1} on IDLE

#English to Spanish Dictionary
eng2sp = {'one':'uno','two':'dos','three':'tres'}
eng2sp

#to see whether something appears as a value in a dictionary,
#us the method values, which returns a collection of vales and
# then use in the operator
vals = eng2sp.values()
'uno' in vals
#this gives True
'tres' in vals
#this gives True
'fish' in vals
#this gives False

#.get Method
#.get takes a key and default value, and if they key appears in the
#dictionary, .get returns the corresponding value - otherwise it returns
#the defualt fault value
#AKA if you have the key "a" in a dictionary, return the value for key 'a'
#if you don't have the key "a" in the dictionary, return the default
h = {'a':1, 'b':1, 'o':2, 'n':1, 's':2, 'r':2, 'u':2,' t':1}
h

h.get('a',0)
#this gives 1 because 'a' is a key in h and has value 1
h.get('z',0)
#this gives 0 because 0 is the default
h.get('z')
#this returns nothing because there is no key 'z' in h and no defualt was given
h.get('z', 'silly')
#this returns 'silly' because that is the default

#Defining My Own dictionary
my_dict = {'chumlee': 'the best', 'kona': 'the sweetest girl', 'chickens':'goofy'}
my_dict

my_dict.get('elephant', 0)
#this returns 0 because it is not a key in the dictionary
my_dict.get('chumlee', 0)
#this returns 'the best' because it is a key in the dictionary

#Looping and Dictionaries
def print_hist(h):
    for c in h:
        print(c, h[c])

h = {'milk':1, 'butter':2, 'egg':6, 'bread':1, 'cheese':3, 'jam':8}
h
print_hist(h)
#this returns:
# milk 1
# butter 2
# egg 6
# bread 1
# cheese 3
# jam 8

#Using a dictionary in a for statement, it will traverse the keys of
#the dictionary

#Sorting things in a Dictionary with sorted() function
h = sorted(h)
h
#this returns ['bread', 'butter', 'cheese', 'egg', 'jam', 'milk']
#this is a list, which can be dangerous, you can't put it back

#to be continued in lab on Nov 3rd and class Nov 4th
