import os

class CountFiles(object):

    def __init__(self, dirname):
        self.dirname = dirname

    def is_dir(self):
        if os.path.isdir(self.dirname):
            return True
        return False

    def is_not_empty(self):
        if os.listdir(self.dirname) != []:
            return True
        return False

    def count_txt_file(self):
        filelist = []
        count = 0

        if not self.is_dir():
            return

        if not self.is_not_empty():
            return

        for filename in os.listdir(self.dirname):
            if filename.endswith('.txt'):
                filelist.append(filename)
                count += 1
        return (count, filelist)


input_path = str(input("Enter directory path: "))
ob = CountFiles(input_path)
print(ob.count_txt_file())
