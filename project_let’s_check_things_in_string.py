"""I create a function that is able to check if a user’s name is located within their greeting
I wrote a function called check_for_name that takes two strings as parameters named sentence and name
The function should return True if name appears in sentence in all lowercase letters, all uppercase letters,
or with any mix of uppercase and lowercase letters.
The function should return False otherwise."""


def check_for_name(sentence, name):
    return name.lower() in sentence.lower()


# test the function at work
test = check_for_name("Albert bine ai venit in grupul nostru", "AlBerT")
print(test)


"""now I am going to create a function that extract every letter from an odd indices of a string and returns the
 resulting string."""


def every_other_letter(word):
    count_letters = ""
    for ch in range(0, len(word)):
        if ch % 2 != 0:
            count_letters += word[ch]
    return count_letters


# test the function at work
test = every_other_letter("Hello word")
print(test)


"""Instead of selecting every other letter, if we want to reverse the entire string"""


def string_reverse(string):
    reversed_string = ""
    for ch in range(len(string)-1, -1, -1):
        reversed_string += string[ch]
    return reversed_string


# test the function at work
test = string_reverse("Hello world")
print(test)


"""we’re going to switch the first letters of each word and return the two new words as a single string separated by
 a space."""


def make_spoonerism(word1, word2):
    first_ch_word1 = word1[0]
    reminder_ch_word1 = word1[1:]
    first_ch_word2 = word2[0]
    reminder_ch_word2 = word2[1:]
    return first_ch_word2 + reminder_ch_word1 + " " + first_ch_word1 + reminder_ch_word2


test = make_spoonerism("ana", "baba")
print(test)


"""This function should add exclamation points to the end of word until word is 20 characters long. If word is already
 at least 20 characters long, just return word."""


def add_exclamation(word):
    new_word = word[:20].ljust(20, "!")
    return new_word


test = add_exclamation("now")
print(test)





