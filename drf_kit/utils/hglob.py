import glob


def glob_with_sub_directories(pathname, modules=[]):
    modules = modules + glob.glob(pathname)

    last_backslash_index = pathname.rfind('/')
    current_dir = pathname[:last_backslash_index]
    filename = pathname[last_backslash_index+1:]

    sub_dirs = glob.glob('{}/*/'.format(current_dir))
    for sub_dir in sub_dirs:
        pathname = sub_dir + filename
        modules = glob_with_sub_directories(pathname, modules)

    return modules
