def main():
    # Read Contents
    with open(r"books/frankenstein.txt") as f:
        file_contents = f.read()

    # Get wordcount
    word_num = get_word_count(file_contents)
    print(word_num)

    # Get lettercount
    letters = get_letter_count(file_contents)
    print(letters)

# Get rid of newline chars, seperate words into list,
# get rid of unnecessary whitespace,
# return a list of words, and the string without newline chars
def clean_text(string):
    string = string.replace("\n", " ")
    words = string.split(" ")
    while "" in words:
        words.remove("")
    return words, string

# Get length of list of words
def get_word_count(string):
    words = clean_text(string)[0]
    return len(words)

# Get string w/o newline chars, iterate through chars,
# ignore whitespace, convert letter to lowercase,
# increment counter for current letter.
def get_letter_count(string):
    letter_count = {}
    string = clean_text(string)[1]
    for char in string:
        char = char.lower()
        if not char.isalpha():
            pass
        elif char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1
    return letter_count

main()