import sys

script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    
def print_line(line, encoding, errors):
    next_lang = line.strip() # not sure what is line.strip
    raw_bytes = next_lang.encode(encoding, errors=errors) # encode function
    cooked_string = raw_bytes.decode(encoding, errors=errors) # decode function

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)
