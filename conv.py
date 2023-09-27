import fire

def convert_hex_dec(conv=None, input=None):
    """
    Convert data between hexadecimal and decimal.

    Parameters:
    - conv (str): The type of conversion, either 'hex2dec' or 'dec2hex'.
    - input (str): The string containing the data to convert.

    Returns:
    - str: The converted data as a string.
    """
    switch_dict = {
        'hex2dec': lambda x: str(int(x, 16)),
        'dec2hex': lambda x: hex(int(x))[2:]
    }
    print(f"input {input}, {type(input)}")
    
    if conv == 'hex2dec' and isinstance(input, int):
        hex_string = str(input)
        input = hex_string  # change to hex string not int type
    func = switch_dict.get(conv, None)

    if func:
        return conv + ": " + func(input)
    else:
        return "Invalid conversion type. Use 'hex2dec' or 'dec2hex'."

if __name__ == '__main__':
    fire.Fire(convert_hex_dec)

