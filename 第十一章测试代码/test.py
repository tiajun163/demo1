def get_name(firs,last,lst=''):
    if lst:
        full_name=firs+last+lst
    else:
        full_name=firs+last
    return  full_name.title()
# con=get_name('arl','ser')
# print(con)