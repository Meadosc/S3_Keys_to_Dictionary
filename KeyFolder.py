
class KeyFolder():
    def __init__(self, key):
        self.key = key
        self.name = key.split('/')[-2]
        self.item_type = 'folder'
        self.items = []
    

    def get_dict_of_object(self):
        key_dict = {}
        key_dict['key'] = self.key
        key_dict['name'] = self.name
        key_dict['type'] = self.item_type 
        key_dict['items'] = self.items
        return key_dict
    

    def __repr__(self):
        print_str = ""
        for attribute, value in self.__dict__.items():
            print_str += f"{attribute}: {value}\n"
        return print_str
    