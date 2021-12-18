import os


def get_file_list(path, type="all"):
    """
    获取文件列表
    """
    file_list = []

    if type == "all":
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                file_list.append((os.path.join(dirpath, filename)))
        return file_list

    if type == "current":
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                file_list.append(file_path)
        return file_list

    raise TypeError("invalid type: {type}")


def get_folder_list(path, type="all"):
    """
    获取文件夹列表
    """
    folder_list = []

    if type == "all":
        for dirpath, dirnames, filenames in os.walk(path):
            for dirname in dirnames:
                folder_list.append((os.path.join(dirpath, dirname)))
        return folder_list

    if type == "current":
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isdir(file_path):
                folder_list.append(file_path)
        return folder_list

    raise TypeError("invalid type: {type}")
