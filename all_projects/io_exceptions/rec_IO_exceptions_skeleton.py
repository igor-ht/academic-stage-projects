import copy
import string

#########################################
# Question 1 - do not delete this comment
#########################################
def say_hi(in_file, out_file):
    with open(in_file, 'r') as f:
        data = f.read()
    with open(out_file, 'w') as j:
        j.write(f'Hi {data}')
    f.close()
    j.close()
    print(f'The file {out_file} was created.')

#########################################
# Question 2 - do not delete this comment
#########################################
def get_most_common_word(in_file):
    alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
    d = {}
    word = str()
    try:
        print(f'Analyzing the file {in_file}.')
        with open(in_file, 'r', encoding='utf-8') as f:
            data = f.read()
            for char in data:
                if char.lower() in alphabet:
                    word += char.lower()
                elif len(word) > 0:
                    d[word] = d.get(word, 0) + 1
                    word = str()
        f.close()
    except IOError:
        print('No words.')
    finally:
        print(f'The file has been analyzed.')
        if len(d) >= 1:
            sorted_keys = sorted(d.keys(), key=d.get, reverse=True)
            print(f'The world "{sorted_keys[0]}" is written {d[sorted_keys[0]]} times in the text.')

#########################################
# Question 3 - do not delete this comment
#########################################
def decode(in_file, out_file):
    try:
        alphabet = list(string.ascii_lowercase)
        with open(in_file, 'r', encoding='utf-8') as f:
            data = f.read()
        with open(out_file, 'w', encoding='utf-8') as j:
            new_data = ''
            for char in data:
                indx = 0
                if char in alphabet:
                    indx = alphabet.index(char) + 1
                    if indx >= 26:
                        indx %= 26
                    new_data += alphabet[indx]
                elif char.lower() in alphabet and char.isupper():
                    indx = (alphabet.index(char.lower()) + 1)
                    if indx >= 26:
                        indx %= 26
                    new_data += alphabet[indx].upper()
                else:
                    new_data += char
            j.write(new_data)
        f.close()
        j.close()
        print(f'The file was deciphered.')
    except IOError:
        print(f'Can`t decipher {in_file} due to an IO Error.')
    finally:
        print(f'The file {in_file} was analyzed.')

#########################################
# Bonus Question - do not delete this comment
#########################################
def verify_circle(in_file):

    try:
        with open(in_file,'r', encoding='utf-8') as f:
            data = f.read()
            f.close()

        lines_lst = []
        for n in data.split('\n'):
            for v in n:
                if not v.isnumeric():
                    raise TypeError
            lines_lst.append(int(n))

        c = 0
        checker = 0
        check_lst = copy.copy(lines_lst)
        while checker < len(lines_lst):
            num1 = lines_lst[c]
            check_lst.remove(num1)
            checker += 1
            c = num1 - 1

        if checker == len(lines_lst) and len(check_lst) == 0:
            print(f'The file {in_file} is a circle file.')
        else:
            print(f'The file {in_file} is a non circle file.')
    except TypeError:
        print(f'The file has not valid numbers. They need to be integers and bigger than 0.')
    except:
        print('The file is a non circle file.')
    finally:
        print(f'The file {in_file} was analyzed.')

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################             

#say_hi('q1.txt', 'out_file.txt')
#print()
#get_most_common_word('q2_trump.txt')
#print()
#decode('q3.txt', 'q3_after.txt')
#print()
#verify_circle('q5_circle.txt')
#print()
#verify_circle('q5_non_circle.txt')
#print()
#verify_circle('q5_non_circle2.txt')