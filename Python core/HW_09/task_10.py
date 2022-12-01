contacts = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": True,
}]

def get_favorites(contacts):

    favorites_contacts = []

    for item in filter(lambda contact: contact["favorite"], contacts):
        favorites_contacts.append(item)

    return favorites_contacts

print(get_favorites(contacts))
