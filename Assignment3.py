
def count_substring(input, sub):
    count = 0
    input_len = len(input)
    sub_len = len(sub)
    
    for ch in range(0, input_len):
        if input[ch] == sub[0]:
            if input[ch:ch + sub_len] == sub:
                count += 1
    return count

x = input("Enter a string : ")
y = input("Enter a sub string : ")
print(count_substring(x,y))