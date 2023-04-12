# Palindromes for functions

def is_palindrome (string): 
    # backwards = string[::-1]
    # return backwards == string

    return string[::-1].casefold() == string.casefold()



def palindrome_sentence (sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


def banner_text(text):
    screen_width = 80
    if len (text) > screen_width - 4:
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)

    else:
        centered_text= text.center(screen_width-4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten, ")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ")
banner_text("When you're feeling in the dumps, ")
banner_text("Don't be silly chumps, ")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life..")
banner_text("*")

def names(*students):
    for name in students:
        print(f"my name is {name}")


names("leo", "ndemo", "mwangi", "Kimani")

