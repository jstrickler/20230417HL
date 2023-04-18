
MIN_LENGTH=20
INPUT_FILE = "DATA/words.txt"
OUTPUT_FILE = "long_words.txt"

word_count = 0
with open(INPUT_FILE) as words_in:
    with open(OUTPUT_FILE, 'w') as words_out:
        for raw_word in words_in:
            word = raw_word.rstrip()
            if len(word) > MIN_LENGTH:
                print(word)
                words_out.write(raw_word)
                word_count += 1

print(f"{word_count} words are greater than {MIN_LENGTH} characters")