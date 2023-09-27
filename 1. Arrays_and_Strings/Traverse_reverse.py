# Given an array of numbers, replace each even number with two of the same number. e.g, [1,2,5,6,8, , , ,] -> [1,2,2,5,6,6,8,8].Assume that the array has the exact amount of space to accommodate the result.



def clone_even_numbers(lst):
    def find_pos(arr):
        for idx, num in enumerate(arr):
            if num == -1:
                return idx-1
            
    end = len(lst) - 1
    old_val = find_pos(lst)

    while old_val > 0:
        if lst[old_val]%2==0:
            lst[end] = lst[old_val]
            lst[end-1] = lst[old_val]
            end -=2
            old_val -=1 
        else:
            lst[end] = lst[old_val]
            end -=1
            old_val -=1
    return lst


print(clone_even_numbers([1,2,5,6,8,-1,-1,-1]))
# # should output [1,2,2,5,6,6,8,8]






# def clone_even_numbers(lst):
#     idx = get_last_num(lst);
#     end = len(lst)-1 # should be 7 for this example
  
#     while(idx >= 0):
#         # print(lst[end],lst[idx])
#         if lst[idx] % 2 == 0:
#             lst[end] = lst[idx]
#             end -=1
#             lst[end] = lst[idx]
#             end -=1
#         else:
#             lst[end] = lst[idx]
#             end -=1
#         # Missing this line
#         idx -= 1
    
#     return lst

# def get_last_num(arr):
#     i = len(arr) - 1
#     while (i >= 0 and arr[i] == -1):
#         i -= 1
#     return i

# print(clone_even_numbers([1,2,5,6,8,-1,-1,-1]))
# should output [1,2,2,5,6,6,8,8]

    