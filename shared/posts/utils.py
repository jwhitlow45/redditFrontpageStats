def post_id_to_int(post_id:str) -> int:
    """
        Creates a unique integer id from a post id by treating
        the string as a base-36 number and converting it to decimal

        Arguments: post_id->string

        Returns: dec_value->integer

        Errors: ValueError
    """
    # Reverse string
    post_id = post_id[::-1].lower()
    # Value to keep track of power in 
    dec_value = 0
    # Iterate through post_id converting each number to decimal
    for index, char in enumerate(post_id):
        # Check if character contains non-alphanumeric character
        if not char.isalpha() and not char.isnumeric():
            raise ValueError(f'String {post_id} contains non-\
                alphanumeric characters')

        # Decimal representation of character
        dec_equiv = 0
        if char.isalpha():
            dec_equiv = ord(char)-87
        else:
            dec_equiv = ord(char)-48
        # Add dec_equiv while account for place to dev_value
        dec_value = dec_value+(dec_equiv*(36**index))

    return dec_value