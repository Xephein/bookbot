def main():
    # Read Contents
    with open(r"books/frankenstein.txt") as f:
        file_contents = f.read()

    # Get wordcount
    word_num = get_word_count(file_contents)
    print(word_num)

def clean_text(string):
    string = string.replace("\n", " ")
    words = string.split(" ")
    while "" in words:
        words.remove("")
    return words

def get_word_count(string):
    words = clean_text(string)
    return len(words)


main()