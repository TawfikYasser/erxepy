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

def erxepy(test_str) -> str :
    """
    erxepy method used to start working with the whole module.
    You can call this method in your code and everythin will work.
    """
    
    # Checking that the test string's length is greater than 0
    if len(test_str) > 1:
        
        print("Welcome to 'erxepy'")
        print("-------------------")
        print("Please choose your needed 'Regular Expression' from the following:")
        print("Note: you can choose more than one expression.")

        more = True
        regex = ""

        while more:
            print("Choose number from the following: ")
            print("1) Any character except newline : .")
            print("2) The character : a")
            print("3) The string : ab")
            print("4) a or b : a|b")
            print("5) 0 or more a's : a*")
            print("6) 0 or more")
            print("7) 1 or more")
            print("8) 0 or 1")
            print("9) Exactly 2 : {2}")
            print("10) Between 2 and 5 : {2,5}")
            print("11) 2 or more : {2,}")
            print("12) Up to 5 : {,5}")
            print("13) One digit : \d")
            print("14) One non-digit : \D")
            print("15) One whitespace : \s")
            print("16) One non-whitespace : \S")
            print("17) One word character : \w")
            print("18) One non-word character : \W")
            print("19) Start of string : ^")
            print("20) End of string : $")

            user_input = input("> ")

            if user_input not in regexs:
                print("Worng input")
                more = True
            
            additional_text_1 = None
            additional_text_2 = None

            if user_input == "2":
                additional_text_1 = input("Please enter the letter ")
                regex += additional_text_1
                additional_text_1 = None
            elif user_input == "3":
                additional_text_1 = input("Please enter the string ")
                regex += additional_text_1
                additional_text_1 = None
            elif user_input == "4":
                additional_text_1 = input("Please enter x in x|y ")
                additional_text_2 = input("Please enter y in x|y ")
                regex += additional_text_1 + "|" + additional_text_2
                additional_text_1 = None
                additional_text_2 = None
            elif user_input == "5":
                additional_text_1 = input("Please enter x in x* ")
                regex += additional_text_1 + "*"
                additional_text_1 = None
            elif user_input == "9":
                additional_text_1 = input("Please enter x in {x} ")
                regex += "{"+additional_text_1+"}"
                additional_text_1 = None
            elif user_input == "10":
                additional_text_1 = input("Please enter x in {x,y} ")
                additional_text_2 = input("Please enter y in {x,y} ")
                regex += "{"+additional_text_1+","+additional_text_2+"}"
                additional_text_1 = None
                additional_text_2 = None
            elif user_input == "11":
                additional_text_1 = input("Please enter x in {x,} ")
                regex += "{"+additional_text_1+",}"
                additional_text_1 = None
            elif user_input == "12":
                additional_text_1 = input("Please enter x in {,x} ")
                regex += "{,"+additional_text_1+"}"
                additional_text_1 = None
            else:
                regex += regexs[user_input]
            
            ask_more = input(r"Continue? (Y\N) ")
            if ask_more == "Y" or ask_more == "y":
                more = True
            elif ask_more == "N" or ask_more == "n":
                more = False
                #print(chr(27) + "[2J")
                print(f"Your Regular Expression =>{regex}")
            else:
                print("Worng option.")
                more = True
                
    else:
        print("Sorry!. Your test string is not valid.")

    matched = re.search(regex,test_str)
    print(f"Match result: {matched.group()}")

erxepy("123")