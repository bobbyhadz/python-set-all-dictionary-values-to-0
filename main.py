# Set all dictionary values to 0 in Python

my_dict = {
    'bobby': 1,
    'hadz': 2,
    'com': 3,
}

my_dict = dict.fromkeys(my_dict, 0)
print(my_dict)  # 👉️ {'bobby': 0, 'hadz': 0, 'com': 0}
