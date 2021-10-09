folder = "Data"
extension = ".fiad"

class LocalVariable:
    
    def __init__(self):
        import os
        import ctypes
        
        if not self.is_android():
            if not os.path.exists(folder):
                os.makedirs(folder)
            ctypes.windll.kernel32.SetFileAttributesW(folder, 2)

        else:
            if not os.path.exists(folder):
                os.makedirs(folder)


    def is_android(self):
        try:
            from ctypes import windll
        except:
            return True
        return False

            
    def save(self, name, data):
        if type(data) is list:
            import pickle
            with open(folder+"\\"+name+extension, 'wb') as fp:
                pickle.dump(data, fp)
                fp.close()
        elif type(data) is dict:
            import pickle
            with open(folder+"\\"+name+extension, 'wb') as fp:
                pickle.dump(data, fp)
                fp.close()
        elif type(data) is set:
            import pickle
            with open(folder+"\\"+name+extension, 'wb') as fp:
                pickle.dump(data, fp)
                fp.close()
        elif type(data) is tuple:
            import pickle
            with open(folder+"\\"+name+extension, 'wb') as fp:
                pickle.dump(data, fp)
                fp.close() 
        else:      
            data = str(data)
            f = open(folder+"\\"+name+extension, "w")
            f.write(data)
            f.close()


    def read_int(self, name):
        f = open(folder+"\\"+name+extension, "r")
        data = f.read()
        f.close()
        return int(data)


    def read_float(self, name):
        f = open(folder+"\\"+name+extension, "r")
        data = f.read()
        f.close()
        return float(data)


    def read_str(self, name):
        f = open(folder+"\\"+name+extension, "r")
        data = f.read()
        f.close()
        return str(data)


    def read_bool(self, name):
        f = open(folder+"\\"+name+extension, "r")
        data = f.read()
        f.close()
        return bool(data)


    def read_list(self, name):
        import pickle
        with open (folder+"\\"+name+extension, 'rb') as fp:
            itemlist = pickle.load(fp)
            fp.close()
        return list(itemlist)


    def read_set(self, name):
        import pickle
        with open (folder+"\\"+name+extension, 'rb') as fp:
            itemlist = pickle.load(fp)
            fp.close()
        return set(itemlist)


    def read_tuple(self, name):
        import pickle
        with open (folder+"\\"+name+extension, 'rb') as fp:
            itemlist = pickle.load(fp)
            fp.close()
        return tuple(itemlist)


    def read_dict(self, name):
        import pickle
        with open (folder+"\\"+name+extension, 'rb') as fp:
            itemlist = pickle.load(fp)
            fp.close()
        return dict(itemlist)

    def exists(self, name):
        import os.path
        return os.path.isfile(folder+"\\"+name+extension)




class CloudVariable:
    
    def __init__(self, url):
        from firebase import firebase
        self.firebase = firebase.FirebaseApplication(url, None)
        try:
            x = self.get_all_as_dict()
        except:
            self.save('djgndsfihndsiuhndhtujhcfjhgfvyjdi', 'riusdgnsfctjhcftjhgcjcgfduidifhjdu')


    def save(self, name, val):
        data = {name:val}
        self.firebase.put('Variables', name, data)


    def get_all_as_dict(self):
        variables = {}
        variables_as_list = []
        recieve = self.firebase.get('', '')
        
        try:
            values = recieve[list(recieve.keys())[0]]
        except AttributeError: raise Exception("Add some variables first")
        
        for i in values.keys():
            variables_as_list.append(values.get(i))
            
        for i in variables_as_list:
            variables.update(i)
            
        return (variables)


    def read(self, name):
        variables = self.get_all_as_dict()
        return variables.get(name)


    def exists(self, name):
        if name in list(self.get_all_as_dict().keys()):
            return True
        else: return False


class integer:
    
    def __new__(self, name):
        import os.path
        self.data = LocalVariable()
        self.name = name
        if os.path.isfile(folder+"\\"+self.name+extension):
            return self.data.read_int(name)
        else:
            raise Exception("No variable named {}, try creating it using LocalVariable().save(name, value)".format(self.name))


class float:
    
    def __new__(self, name):
        import os.path
        self.data = LocalVariable()
        self.name = name
        if os.path.isfile(folder+"\\"+self.name+extension):
            return self.data.read_float(name)
        else:
            raise Exception("No variable named {}, try creating it using LocalVariable().save(name, value)".format(self.name))


class string:
    
    def __new__(self, name):
        import os.path
        self.data = LocalVariable()
        self.name = name
        if os.path.isfile(folder+"\\"+self.name+extension):
            return self.data.read_str(name)
        else:
            raise Exception("No variable named {}, try creating it using LocalVariable().save(name, value)".format(self.name))




if __name__ == "__main__":
    data = CloudVariable('https://vari-1fdcf-default-rtdb.asia-southeast1.firebasedatabase.app/')
    #data.save("Name", "Fiad")
    #data.save("Number", 5)
    #data.save("FLOAT", 0.555)
    #print(data.read("Name"))
    print(data.exists("Name"))

    #data = LocalVariable()
    #print(data.read_int("Number"))

    #print(data.is_android())
