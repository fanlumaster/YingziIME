import os.path

txt_path = os.path.join(os.path.dirname(__file__), './ciku.txt')
res_path = os.path.join(os.path.dirname(__file__), './ciku02.txt')

with open(txt_path, 'rb+') as myfile:
    bin_content = myfile.read()
    real_content = bin_content.decode()
    real_arr = real_content.split(', ')


print(len(real_arr))

with open(res_path, 'ab+') as myfile:
    for line in real_arr:
        cur_line = line+'\n'
        myfile.write(cur_line.encode())
