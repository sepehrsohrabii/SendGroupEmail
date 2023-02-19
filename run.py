from get_send_data import get_data
from get_users_from_googlesheets import get_users
from sendemail import get_email_info


# list divider
def divide_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


# 1.Get Users from Google Sheets
users_list = get_users()
links_list = get_data()
# 2.How many users do you want to be in one server
users_per_server = int(input('How many users do you want to be in one server? (Enter 0 for unlimited) '))
divided_users_list = divide_list(users_list, users_per_server)

# 3.Configure servers

i = 1
j = 0
for item in divided_users_list:
    server_name = f'server{i}'
    check = int(
        input(f'If you want to skip sending {server_name}\'s outline configuration press 0 if not press 1: '))
    if check == 1:
        for user in item:
            name = user["name"]
            email = user["email"]
            user_link = links_list[j]
            print(name, user_link)
            get_email_info(name, email, user_link)

    i += 1
    j += 1
