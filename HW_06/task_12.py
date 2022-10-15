import base64

data = ['andry:uyro18890D', 'steve:oppjM13LL9e']

def encode_data_to_base64(data):

    data_b64 = []

    for item in data:

        item_bytes = item.encode()
        item_b64_bytes = base64.b64encode(item_bytes)
        b64_item = item_b64_bytes.decode()
        data_b64.append(b64_item)        

    return data_b64

print(encode_data_to_base64(data))

    


