# ----PART 1: 

# with open("abespeech.txt") as file_ref:
#     for line_no, line in enumerate(file_ref, 1):
#         print(f'{line_no}: {line[::-1]}')
        

# ----PART 2: 

with open("smedlybutler.txt", encoding="utf8") as fn:
    lst = []
    for line in fn:
        for word in line.split():
            if len(word) > 9:
                lst.append(word)
                print(lst)