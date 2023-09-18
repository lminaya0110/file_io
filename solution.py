# ----PART 1: 

# with open("abespeech.txt") as file_ref:
#     for line_no, line in enumerate(file_ref, 1):
#         print(f'{line_no}: {line[::-1]}')
        

# ----PART 2: 

with open('smedlybutler.txt') as sb:
    smed_dict = { a_line: a_word for a_line in sb
                  for a_word in a_line.split(" ") if len(a_word) > 9}
# Write to file
with open( 'bigwords.txt', 'w') as bw:
    bw.writelines( [ f'Word: {smed_dict[ line_key ]}  Line: {line_key} 'for line_key in smed_dict ] )