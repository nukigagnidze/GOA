# 1
#2  aq codewarse gvqonda
# def find_short(s):
#     list1 = s.split(" ")


#     word_len = len(list1[0])
#     for i in list1:
#         if len(1) < word_len:
#             word_len = len(1)

#     return word_len

# 3
strings = [
    "apple, banana, strabery",
    "dog, cat, tutle",
    "yellow, green, blue",
    "hello word",
    "foo_bar_baz",
    "python#rocks",
    "split#this",
    "A:B:C",
    "hello&ther",
]
separator = ","
split_string = [s.split(separator) for s in string]


for i, split_str in enumerate(split_strings):
    print(f"original: {strings[i]}")
    print(f"split: {split_str})