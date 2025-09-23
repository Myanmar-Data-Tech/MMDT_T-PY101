import sys
import os

if len(sys.argv) != 3:
    
    print(f"Usage: {sys.argv[1]} input_file")
    print(f"Usage: {sys.argv[2]} output_file")
    sys.exit(1)  # 1 indicates error

else:
    print(f"the script file is {sys.argv[0]}.")
    print(f"the input file is {sys.argv[1]}.")
    print(f"the output file is {sys.argv[2]}.")


print(f"Opening file {sys.argv[1]}.")

if not os.path.exists(sys.argv[1]):  # Make sure file exists
    print("File does not exist.")
    sys.exit(1)  # 1 indicates error

f = open(sys.argv[1], "r")

with open(sys.argv[1], "r") as test_open:
    text = test_open.read()
    word_list = text.split()
    word_dict = {}
    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1

print(f"Writing vocabulary to {sys.argv[2]}.")
with open(sys.argv[2], "w") as vocab_file:
    for word, count in sorted(word_dict.items(), key=lambda item: item[1], reverse=True):
        vocab_file.write(f"{word}\t{count}\n")
