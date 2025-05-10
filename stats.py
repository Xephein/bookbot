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