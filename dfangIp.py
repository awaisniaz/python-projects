def ip_address(addresses):
    new_address = ""
    split_adress = addresses.split('.')
    separator = "[.]"
    new_address = separator.join(split_adress)
    print(new_address)
    
ip_address('1.2.3.4')