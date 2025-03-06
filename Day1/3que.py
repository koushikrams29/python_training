import os

def find_largest_file(directory):
    max_size =0
    max_file=""

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > max_size:
                max_size = file_size
                max_file = file_path

    return max_file,max_size

# Example usage
directory = r"C:\Users\Vampatapu Koushik\handson/1st Day"  # Replace with the actual directory path
largest_file, max_size = find_largest_file(directory)
if largest_file:

    print(f"Largest file: {largest_file}")
    print(f"Size: {max_size} bytes")
else:
    print("No files")
