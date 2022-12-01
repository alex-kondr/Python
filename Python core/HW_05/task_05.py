def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):

    jp_list = []
    sg_list = []
    tw_list = []
    ua_list = []
    dict_phone = {}

    for phone in list_phones:

        sanitize_phone = sanitize_phone_number(phone)

        if sanitize_phone.startswith("81"):
            jp_list.append(sanitize_phone)

        elif sanitize_phone.startswith("65"):
            sg_list.append(sanitize_phone)

        elif sanitize_phone.startswith("886"):
            tw_list.append(sanitize_phone)

        else:
            ua_list.append(sanitize_phone)

    dict_phone.update({
        "UA": ua_list,
        "JP": jp_list,
        "TW": tw_list,
        "SG": sg_list
    })

    return dict_phone
