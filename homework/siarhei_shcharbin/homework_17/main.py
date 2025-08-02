import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("path", help="specify path to the folder with log files")
parser.add_argument("text", help="text to find in log files")
args = parser.parse_args()
try:
    files = [f for f in os.listdir(args.path) if os.path.isfile(os.path.join(args.path, f))]
    if not files:
        print(f'No files found in the specified directory: {args.path}')
        exit(0)
    for filename in files:
        file_path = os.path.join(args.path, filename)
        with open(file_path, 'r', encoding='utf-8') as data_file:
            lines = data_file.readlines()
            match_found = False
            for line_number, line in enumerate(lines, start=1):
                start_pos = 0
                while True:
                    index = line.find(args.text, start_pos)
                    if index == -1:
                        break
                    match_found = True
                    start_word = index
                    end_word = index + len(args.text)
                    while start_word > 0 and (line[start_word - 1].isalnum() or line[start_word - 1] == '_'):
                        start_word -= 1
                    while end_word < len(line) and (line[end_word].isalnum() or line[end_word] == '_'):
                        end_word += 1
                    word_with_match = line[start_word:end_word].strip()
                    words = line.strip().split()
                    word_index = words.index(word_with_match) if word_with_match in words else None
                    start = max(0, word_index - 5) if word_index is not None else 0
                    finish = min(len(words), word_index + 6) if word_index is not None else len(words)
                    err_text = " ".join(words[start:finish])
                    print(f'Found match in file "{filename}"')
                    print(f'The error text is "{err_text}"')
                    print(
                        f'Line number: {line_number}, character index: {index}\n'
                    )
                    start_pos = index + 1
            if not match_found:
                print(f'No match found in file "{filename}"\n')
except FileNotFoundError:
    print(f'Error: Folder not found: {args.path}')
except Exception as e:
    print(f'Error while processing files: {e}')
