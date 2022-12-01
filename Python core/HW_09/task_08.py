def get_emails(list_contacts):

    email_list = []

    for item in map(lambda x: x["email"], list_contacts):
        email_list.append(item)

    return email_list
