import os
import argparse

def logo():
    logo0 = '''
    _______           ______  _____       ____        __ 
   / ____(_)___  ____/ / __ \/ ___/      / __ \__  __/ /_
  / /_  / / __ \/ __  / / / /\__ \______/ / / / / / / __/
 / __/ / / / / / /_/ / /_/ /___/ /_____/ /_/ / /_/ / /_  
/_/   /_/_/ /_/\__,_/\____//____/      \____/\__,_/\__/  
'''
    print(logo0)

def search_files(directory, extensions):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            for extension in extensions:
                if filename.endswith(extension):
                    files.append(os.path.join(root, filename))
    return files

def search_content(file_path, content):
    matching_lines = []
    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                try:
                    if content in line:
                        matching_lines.append((line_num, line))
                except UnicodeDecodeError as e:
                    print("[-] Unicode decode error in file %s, line %d: %s" % (file_path, line_num, e))
        return matching_lines
    except:
        print("[-] Error file %s" % (file_path))

def write_to_file(output_file, file_path, matching_lines):
    with open(output_file, 'a') as f:
        f.write("[+] File Path: %s\n" % file_path)
        f.write("[=] Line Rows: %d\n" % len(matching_lines))
        for line_num, line in matching_lines:
            f.write("[~] In Line %d: %s\n" % (line_num, line.strip()))
        f.write("\n")

def main():
    parser = argparse.ArgumentParser(description="FindOS-Out")
    parser.add_argument("-n", "--name", help="Specify the suffix", required=True)
    parser.add_argument("-c", "--content", help="Specify file content", required=True)
    parser.add_argument("-o", "--output", help="Specify output file", default="findout.txt")
    parser.add_argument("-d", "--directory", help="Target directory", default="./")
    args = parser.parse_args()

    directory = args.directory
    extensions = args.name.split(',')
    content = args.content
    output_file = args.output

    files = search_files(directory, extensions)

    for file_path in files:
        matching_lines = search_content(file_path, content)
        if matching_lines:
            write_to_file(output_file, file_path, matching_lines)

if __name__ == "__main__":
    logo()
    print("[+] Runing Search..")
    main()
    print("[+] Out to findout.txt..")
