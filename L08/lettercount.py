def letter_count(string):
    letter = [*string]
    letterset = set(letter)
    new_dict={l:letter.count(l) for l in letterset}
    return new_dict
print(letter_count("hello"))