import os

def concatenate(input_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file in os.listdir(input_dir):
            if file.endswith('.txt'): 
                file_path = os.path.join(input_dir, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"--- Content of {file} ---\n")  
                        outfile.write(infile.read())
                        outfile.write("\n\n") 
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

# Example usage
input = r"C:\Users\Vampatapu Koushik\handson/1st Day"  
output = "concat.txt" 

concatenate(input, output)
print(f"All .txt files have been combined into {output}")
