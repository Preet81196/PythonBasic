"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 28/05/20
* @decription: Write a Python program to check whether a list contains a sublist.
"""

# given_list = [2, 4, 3, 5, 7]
# first_check = [4, 3] => True
# second_check = [3, 7] => False


def check_sublist_in_list(main_l, sub_l):
    is_sublist = False
    prev_index = None
    current_index = None

    for each in sub_l:
        if each in main_l:
            if prev_index is None and current_index is None:
                prev_index = main_l.index(each)
                current_index = main_l.index(each)
            else:
                current_index = main_l.index(each)
            if current_index == prev_index + 1:
                is_sublist = True
            else:
                is_sublist = False
            prev_index = current_index

    return is_sublist


given_list = [2, 4, 3, 5, 7]
first_check = [4, 3]
second_check = [3, 7]

# print(check_sublist_in_list(given_list, first_check))
# print(check_sublist_in_list(given_list, second_check))


# Another Simple way
# def is_list_gradually_incremental(local_list):
#     """
#     This function checks if a list elements are gradually increasing
#     Like, [0, 1, 2, 3] => True
#     Whereas, [2, 4, 5] => False
#     :param local_list: a list of indices
#     :return: True/False
#     """
#     i = 0
#     while i < len(local_list):
#         if i is not 0 and local_list[i - 1] != local_list[i] - 1:  # current should be greater than 1 of previous
#             return False
#         i += 1
#     return True


def check_with_respective_indexes(mail_l, sub_l):
    ind_list = list()
    for each in sub_l:
        if each in mail_l:
            ind_list.append(mail_l.index(each))

    # return is_list_gradually_incremental(ind_list)
    # Another way to get if loop elements are increasing exactly by
    return all([x == y-1 for x, y in zip(ind_list, ind_list[1:])])


print(check_with_respective_indexes(given_list, first_check))
print(check_with_respective_indexes(given_list, second_check))
