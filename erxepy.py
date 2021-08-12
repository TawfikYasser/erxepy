"""
This is 'erxepy' module,
by using this module you can create your complex 'Regular Expression' in just few seconds.
"""

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
    print("Welcome to 'erxepy 0.0.7'")
    print("-------------------")
    print("Note: you can choose more than one expression.")
    print("Choose number from the following: ")
    print("-----------------------------------")
    # While loop to show the list of available regular expressions for the user to choose from them.
    while more:
        show_rxs()
        user_input = input(">> ")
        if user_input == "0":
            return result
        if user_input not in regexs:
            print("Option doesn't found!")
            continue
        result += combine_regex(user_input,regex)
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
    print("+ [0] Exit ---------------------------------------------------------------------------+")
    print("+----------------------------------+-------------------+----------------+-------------+")
    print("| [1] Any character except newline | [2] The character | [3] The string | [4] a or b  |")
    print("+-------------------+---------------+---------------+------------+--------------------+")
    print("| [5] 0 or more a's | [6] 0 or more | [7] 1 or more | [8] 0 or 1 | [9] Exactly 2      |")
    print("+----------------------+----------------+--------------+------------------------------+")
    print("| [10] Between 2 and 5 | [11] 2 or more | [12] Up to 5 | [13] One digit               |")
    print("+--------------------+---------------------+------------------------------------------+")
    print("| [14] One non-digit | [15] One whitespace | [16] One non-whitespace                  |")
    print("+-------------------------+-----------------------------+-----------------------------+")
    print("| [17] One word character | [18] One non-word character | [19] Start of string        |")
    print("+-------------------------------------------------------------------------------------+")
    print("| [20] End of string                                                                  |")
    print("+-------------------------------------------------------------------------------------+")
    #END OF FUNCTION 


if __name__ == "__main__":
    # For testing only.
    print(f"Your Regular Expression (For 0111 2497-156): {make_regex()}")
