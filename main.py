def main():
    # Read Contents
    with open(r"books/frankenstein.txt") as f:
        file_contents = f.read()

    # Get wordcount
    word_num = get_word_count(file_contents)
    print(word_num)



def get_word_count(string):
    words = string.split(" ")
    return len(words)


main()