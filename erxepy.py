"""
This is 'erxepy' module,
by using this module you can create your complex 'Regular Expression' in just few seconds,
this module uses 're' module in it's underlying code.

"""

# File import
import re

# Dictionary of regular expressions
regexs = {
    "1" : ".",
    "2" : "a",
    "3" : "ab",
    "4" : "|",
    "5" : "*",
    "6" : "*",
    "7" : "+",
    "8" : "?",
    "9" : "{2}",
    "10": "{2,5}",
    "11": "{2,}",
    "12": "{,5}",
    "13": "\d",
    "14": "\D",
    "15": "\s",
    "16": "\S",
    "17": "\w",
    "18": "\W",
    "19": "^",
    "20": "$"
}

def make_regex() -> str :
    """
    erxepy method used to start working with the whole module.
    You can call this method in your code and everythin will work.
    """
    more = True
    regex = ""
    result = ""
    print("Welcome to 'erxepy 0.0.5'")
    print("-------------------")
    print("Note: you can choose more than one expression.")
    print("Choose number from the following: ")
    print("-----------------------------------")
    # While loop to show the list of available regular expressions for the user to choose from them.
    while more:
        show_rxs()
        user_input = input("> ")
        if user_input not in regexs:
            print("Option doesn't found!")
            more = True
            continue

        result += combine_regex(user_input,regex)
        
        ask_more = input(r"Continue? (Y\N) ")
        if ask_more == "Y" or ask_more == "y":
            more = True
            print("#%"*20)
        elif ask_more == "N" or ask_more == "n":
            more = False

    regex = ""
    more = True
    return result # The regular expression you can use anywhere.
    #END OF FUNCTION

def combine_regex(user_input,regex):   
    additional_text_1 = ""
    additional_text_2 = ""
    
    if user_input == "2":
        additional_text_1 = input("Please enter the letter ")
        regex += additional_text_1
    elif user_input == "3":
        additional_text_1 = input("Please enter the string ")
        regex += additional_text_1
    elif user_input == "4":
        additional_text_1 = input("Please enter x in x|y ")
        additional_text_2 = input("Please enter y in x|y ")
        regex += additional_text_1 + "|" + additional_text_2
    elif user_input == "5":
        additional_text_1 = input("Please enter x in x* ")
        regex += additional_text_1 + "*"
    elif user_input == "9":
        additional_text_1 = input("Please enter x in {x} ")
        regex += "{"+additional_text_1+"}"
    elif user_input == "10":
        additional_text_1 = input("Please enter x in {x,y} ")
        additional_text_2 = input("Please enter y in {x,y} ")
        regex += "{"+additional_text_1+","+additional_text_2+"}"
    elif user_input == "11":
        additional_text_1 = input("Please enter x in {x,} ")
        regex += "{"+additional_text_1+",}"
    elif user_input == "12":
        additional_text_1 = input("Please enter x in {,x} ")
        regex += "{,"+additional_text_1+"}"
    else:
        regex += regexs[user_input]

    additional_text_1 = ""
    additional_text_2 = ""
    return regex
    #END OF FUNCTION

def show_rxs():

    print("1) Any character except newline:")
    print("2) The character:")
    print("3) The string:")
    print("4) a or b:")
    print("5) 0 or more a's :")
    print("6) 0 or more")
    print("7) 1 or more")
    print("8) 0 or 1")
    print("9) Exactly 2:")
    print("10) Between 2 and 5:")
    print("11) 2 or more:")
    print("12) Up to 5:")
    print("13) One digit:")
    print("14) One non-digit:")
    print("15) One whitespace:")
    print("16) One non-whitespace:")
    print("17) One word character:")
    print("18) One non-word character:")
    print("19) Start of string:")
    print("20) End of string:")
    #END OF FUNCTION
