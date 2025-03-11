import os

def split_file(file_,no_parts): 
    file_size = os.path.getsize(file_)  
    chunk_size = file_size // no_parts   
    
    with open(file_, 'rb') as infile: 
        for i in range(no_parts):
            
            chunk_name = f"{file_}_part{i+1}"
            
            # Write the chunk data to a new file
            with open(chunk_name, 'wb') as chunk_file:
                if i == no_parts - 1:
                    # Write the remainder of the file in the last part
                    chunk_file.write(infile.read())
                else:
                    chunk_file.write(infile.read(chunk_size))
            
            print(f"Generated: {chunk_name}")

original_file =r"C:\Users\Vampatapu Koushik\handson\1st Day\1que.py"
number_of_parts = 5                       

split_file(original_file, number_of_parts)
