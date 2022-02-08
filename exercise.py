def nameValidator(name):
    """

    """
    msg = ""
    if name.count(' ') != 1:
        msg = "The number of spaces required should just be one"
    else:
        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]
        if first_name.isalpha() and last_name.isalpha():
            if (len(last_name) >= 5 and len(last_name) <= 21) & (len(first_name) >= 5 and len(first_name) <= 21):
                msg = f"{name} is a valid name!"
            else:
                msg = "The length of EACH name must be between 5 and 21 characters!"
        else:
            msg = "Names must only contain alphabets"
    return msg


nom = "Sister Margaret"
print(nameValidator(nom))

