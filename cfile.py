
class CFile():
    def __init__(self):
        pass

    def create(self, file_path):

        import os

        self.file_path = os.path.realpath(file_path) # C:/desktop/folder/file.py
        self.file = self.file_path.split('/')[-1] # file.py
        self.file_name = self.file.split('.')[0] # file
        self.file_ext = self.file.split('.')[1] # py

        try:
            with open(self.file_path, 'r') as file:
                return self
        except FileNotFoundError:
            with open(self.file_path, 'w') as file:
                return self

    def copy_to(self, folder_path):

        with open(self.file_path, 'r') as file:
            file_content = file.read()

        with open(folder_path + '/' + self.file, 'w') as file:
            file.write(file_content)

        return self

    def copy_as(self, new_file_path):

        with open(self.file_path, 'r') as file:
            file_content = file.read()

        with open(new_file_path, 'w') as file:
            file.write(file_content)

        return self

    def delete(self):
        import os
        try:
            os.remove(self.file_path)
            print(f'Deleted {self.file_path}')
        except FileNotFoundError:
            print(f'"{self.file_path}" cannot be found')

    def move_to(self, new_folder_path):
        import os
        new_file_path = new_folder_path + '/' + self.file
        self.copy_to(new_folder_path)
        self.delete()
        self.file_path = new_file_path
        self.file_path = os.path.realpath(self.file_path)
        return self

    def rename_to(self, new_file):
        import os
        try:
            os.rename(self.file, new_file)
            self.file_path = self.file_path.replace(self.file, new_file)
            self.file_path = os.path.realpath(self.file_path)
            self.file = new_file
            self.file_name = self.file.split('.')[0] # file
            self.file_ext = self.file.split('.')[1] # py
            return self
        except FileExistsError:
            print(f'{self.file} already exists')
            return self

    def read_from(self):
        with open(self.file_path,'r') as file:
            content = file.read()
        return content

    def write_to(self, content):
        with open(self.file_path,'a') as file:
            file.write(str(content))
        return self

    def clear(self):
        with open(self.file_path,'w') as file:
            pass
        return self