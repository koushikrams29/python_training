import os

def combine(root, output_file,file_filter=None):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for subdir, _, files in os.walk(root):
            for file in files:
                if not file.endswith('.txt') and (not file_filter or file_filter in file):
                    continue
            
                file_path = os.path.join(subdir, file)
            
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"--- content of {file_path}---\n")
                        outfile.writelines(infile.readlines())
                        outfile.write("\n\n")
                except UnicodeDecodeError:
                    print(f"Skipping binary file or unreadable file: {file_path}")
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

source=r"C:\Users\Vampatapu Koushik\handson/1st Day"
output="c.txt"
combine(source,output)
print(f"All files combined into {output}")


