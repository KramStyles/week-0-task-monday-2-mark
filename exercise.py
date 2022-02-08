def nameValidator(name):
    """
    This function accepts a name input and validates it. It checks for unnecessary spaces and characters, 
    length of the first and last substrings and returns errors for each violation.
    param: name (str) - Name inputted by user
    return: msg (str) - Error message or the fullname
    """
    msg = ""
    if name.count(' ') != 1:
        msg = "The number of spaces required should just be one"
    else:
        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]
        if first_name.isalpha() and last_name.isalpha():
            if (len(last_name) >= 5 and len(last_name) <= 20) & (len(first_name) >= 5 and len(first_name) <= 20):
                msg = f"{name} is a valid name!"
            else:
                msg = "The length of EACH name must be between 5 and 20 characters!"
        else:
            msg = "Names must only contain alphabets"
    return msg


nom = "Sister Margaret"
print(nameValidator(nom))

