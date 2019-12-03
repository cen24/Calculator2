import csv
from FileUtilities.absolutepath import absolutepath

def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class csvreader:
    data = []

    def __init__(self, filepath):
        self.data = []
        try:


            with open(absolutepath(filepath)) as text_data:
                csv_data = csv.DictReader(text_data, delimiter=',')
                for row in csv_data:
                    self.data.append(row)
                pass
        except FileNotFoundError as e:
            print("EXCEPTION Occured FileNotFoundError : Wrong file or file path -->",e)
            assert 0


    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects

