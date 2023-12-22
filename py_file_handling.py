# Python Script to Update an Allow List Based on a Remove List

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()


def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write('\n'.join(data))


def update_allow_list(allow_list, remove_list):
    return [ip for ip in allow_list if ip not in remove_list]


# Replace these file paths with the actual paths on your system
allow_list_file = 'allow_list.txt'
remove_list_file = 'remove_list.txt'

# Read the current allow list and the remove list from files
current_allow_list = read_file(allow_list_file)
remove_list = read_file(remove_list_file)

# Update the allow list by removing IPs present in the remove list
updated_allow_list = update_allow_list(current_allow_list, remove_list)

# Write the updated allow list back to the file
write_file(allow_list_file, updated_allow_list)

print("The allow list has been successfully updated.")
