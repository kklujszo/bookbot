
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    dict_of_letters = count_characters(file_contents)
    sorted_list = create_list_of_letters(dict_of_letters)
    report(file_contents, sorted_list)

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    out_dict = {}
    file_content = file_contents.lower()
    
    for letter in file_content:
        if letter not in out_dict:
            out_dict.update({letter: 1})
        else:
            out_dict[letter] += 1
    return out_dict
    

def create_list_of_letters(dict_of_letters):
    out_list = []
    for key in dict_of_letters:
        if key.isalpha():
            new_dict = {"letter" : key, "num" : dict_of_letters[key]}
            out_list.append(new_dict)
            print(new_dict)

    sorted_list = sorted(out_list, reverse=True, key=lambda x: x['num'])
    return(sorted_list)

def report(file_contents, new_sorted_list):
    word_number = count_words(file_contents)
    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f'{word_number} words found in the document')
    for item in new_sorted_list:
        new_letter = item['letter']
        new_number = item['num']
        print(f'The {new_letter} character was found {new_number} times')
    print("--- End report ---")



main()