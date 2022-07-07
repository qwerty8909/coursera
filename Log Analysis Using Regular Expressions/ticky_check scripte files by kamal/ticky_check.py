import re
import sys
import csv
import operator
import os

# Open file and store it's content in a variale

dict_errors = {}
dict_per_user = {}
user_count = []


def open_file(log_file):
    with open(log_file, "r") as f:
        data = f.readlines()
    return data

# grab paterns i each line / line by line


def generate_dict(data_lines):

    for line in data_lines:
        # Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)
        pattern_error = re.search(r"ticky: ERROR ([\w ]*)", line)
        # pattern_info = re.search(r" INFO: ([\w ]*)", line)
        pattern_user = re.search(r" \(([\w\. ]*)\)", line)

        # generate Errors dictionary
        if pattern_error != None:
            if pattern_error.group(1) not in dict_errors.keys():
                dict_errors[pattern_error.group(1)] = 1
            else:
                dict_errors[pattern_error.group(1)] += 1

        # generate Per_user dictionary // patern_user[1] = slice of username from each line.
        if pattern_user != None:
            if pattern_user.group(1) not in dict_per_user.keys():
                dict_per_user[pattern_user.group(1)] = {}
                dict_per_user[pattern_user.group(1)]['INFO'] = 0
                dict_per_user[pattern_user.group(1)]['ERROR'] = 0
                # Count elements for each user
                if pattern_error != None:
                    dict_per_user[pattern_user.group(1)]["ERROR"] = 1
                else:
                    dict_per_user[pattern_user.group(1)]["INFO"] = 1
            else:
                if pattern_error != None:
                    dict_per_user[pattern_user.group(1)]["ERROR"] += 1
                else:
                    dict_per_user[pattern_user.group(1)]["INFO"] += 1
    print(dict_per_user)
    # Sort dictionaries and generate CSV file.
    errors_list = sorted(
        dict_errors.items(), key=operator.itemgetter(1), reverse=True)
    errors_list.insert(0, ('Error', 'Count'))
    print("\nERRORS Dictionay::::::\n")
    print(errors_list)
    print("\nUsers Dictionay::::::\n")
    per_user_list = sorted(dict_per_user.items(), key=operator.itemgetter(0))
    per_user_list.insert(0, ('Username', {'INFO', 'ERROR'}))
    print(per_user_list)

    # Writing errors csv file
    with open("error_message.csv", "w") as f:
        writer = csv.writer(f)
        for key, value in errors_list:
            writer.writerow([key, value])
    # Writing per_user csv file
    with open("user_statistics.csv", "w") as f2:
        writer = csv.writer(f2)
        for i, key in per_user_list:
            if i != "Username":
                for j, x in key.items():
                    if len(user_count) == 2:
                        user_count.clear()
                    user_count.append(x)
                writer.writerow([i, user_count[0], user_count[1]])

        # [key + ',' + str(value['INFO']) + ',' + str(value['ERROR'])])


def main():

    log_file = sys.argv[1]
    # erros_html_file = sys.argv[2]
    # users_html_file = sys.argv[3]

    data_lines = open_file(log_file)
    generate_dict(data_lines)


if __name__ == "__main__":
    main()

