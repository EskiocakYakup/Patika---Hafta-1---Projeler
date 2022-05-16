# 1 flattening a list

def flatten(input_list):
    output = []
    for item in input_list:
        if type(item) == type([]):
            output.extend(flatten(item))
        else:
            output.append(item)
    return output

# 2 reversing a list

def revlist(input_list):
    
    for index in range(len(input_list)):
        if type(input_list[index]) == type([]):
            input_list[index] = input_list[index][::-1]

    return input_list[::-1]
