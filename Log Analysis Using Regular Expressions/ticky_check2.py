import re
import sys
import operator
import csv


def users_statistics_object_creator(data):
    # users will contain data about each user.
    # Object format:
    # {
    #   "username": {
    #                 "INFO": X,
    #                 "ERROR": # Y
    #               }
    # }

    users = {}

    pattern = r"ticky: (INFO|ERROR) .* \((.*)\)"

    for log_line in data:
        # Search for the pattern and update the users objects with data about each user
        err_type, username = re.search(pattern, log_line).groups()
        if err_type == "INFO":
            if username in users.keys():
                users[username][err_type] += 1
            else:
                users[username] = {"INFO": 1, "ERROR": 0}
        else:
            if username in users.keys():
                users[username][err_type] += 1
            else:
                users[username] = {"INFO": 0, "ERROR": 1}
    return users


def errors_object_creator(data):

    # errors_count will contain data about each error encountered
    # Object format:
    # {
    #   "error_description": X
    # }
    errors_count = {}

    pattern_errors_description = r"ticky: ERROR (.*) "

    for log_line in data:
        # Search for errors pattern and update errors_count with data about each errror
        err_result = re.search(pattern_errors_description,
                               log_line)
        if err_result is not None:
            err_descr = err_result.groups()[0]
            if err_descr in errors_count.keys():
                errors_count[err_descr] += 1
            else:
                errors_count[err_descr] = 1
    return errors_count


def users_statistics(users):
    """Return a list of tuples with format like ("username", X, Y) where X are info_logs and Y are error_logs"""
    sorted_users = sorted(users.items(), key=operator.itemgetter(0))
    usernames = [u[0] for u in sorted_users]
    infos = [i[1]["INFO"] for i in sorted_users]
    errors = [e[1]["ERROR"] for e in sorted_users]

    result_statistics = list(zip(usernames, infos, errors))

    return result_statistics


def errors_format_order(errors_count):
    """Return a list of tuples with format like ("error_description", X) where X is how many times that error appears"""
    ordered = sorted(errors_count.items(),
                     key=operator.itemgetter(1), reverse=True)
    return ordered


def save_to_csv(list_to_write, filename, header):
    """Create the csv file"""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header)
        for row in list_to_write:
            writer.writerow(row)


def main():

    try:
        f = open(sys.argv[1])
        data_content = f.readlines()
        f.close()

        users_data = users_statistics_object_creator(data_content)
        errors_data = errors_object_creator(data_content)

        users_stats_to_list = users_statistics(users_data)
        errors_count_to_list = errors_format_order(errors_data)

        save_to_csv(users_stats_to_list, "user_statistics.csv",
                    ["Username", "INFO", "ERROR"])
        save_to_csv(errors_count_to_list,
                    "error_message.csv", ["Error", "Count"])
        print("Files successfully created")
        sys.exit(0)
    except IndexError:
        print("Missing argument")
        sys.exit(2)
    except IOError:
        print("Error occurred with the file")
        sys.exit(1)


if __name__ == '__main__':
    main()