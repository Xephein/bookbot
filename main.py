from stats import get_word_count, clean_text
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path_to_book = sys.argv[1]

    # Read Contents
    with open(path_to_book) as f:
        file_contents = f.read()

    # Get wordcount
    word_num = get_word_count(file_contents)

    # Get lettercount
    letters = get_letter_count(file_contents)
    
    # Print report
    print_report(word_num, letters, path_to_book)

# Get rid of newline chars, seperate words into list,
# get rid of unnecessary whitespace,
# return a list of words, and the string without newline chars


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

# Function for sorting the list_to_sort array
def get_dict_element_count(dictionary):
    return dictionary["count"]

# Create a list of dictionaries, to sort by letter count.
# Print results in a neat format.
def print_report(word_count, letter_dict, path):
    list_to_sort = []
    for key in letter_dict:
        list_to_sort.append({"letter": key, "count": letter_dict[key]})
    list_to_sort.sort(reverse=True, key=get_dict_element_count)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for letter in list_to_sort:
        print(f"{letter['letter']}: {letter['count']}")


main()