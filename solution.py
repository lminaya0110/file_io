# ----PART 1: 

with open("abespeech.txt") as file_ref:
    for line_no, line in enumerate(file_ref, 1):
        print(f'{line_no}: {line[::-1]}')
        

# ----PART 2: 


