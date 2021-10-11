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


    def get_all_as_dict(self):
         import os
         variables = {}
         _list = os.listdir(folder)
         for i in _list:
             var_name = i.replace(extension, "")
             variables[var_name] = self.read_str(var_name)

         return (variables)




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

        del variables['djgndsfihndsiuhndhtujhcfjhgfvyjdi']
        return (variables)


    def read(self, name):
        variables = self.get_all_as_dict()
        return variables.get(name)


    def exists(self, name):
        if name in list(self.get_all_as_dict().keys()):
            return True
        else: return False




class CloudFile:
    
    import os
    
    def __init__(self, config, serviceAccount):
        import pyrebase
        config = config
        
        if config["storageBucket"].startswith("gs://"):
            config["storageBucket"] = config["storageBucket"].removeprefix("gs://")

        config["serviceAccount"] = serviceAccount
        firebase_storage = pyrebase.initialize_app(config)
        self.storage = firebase_storage.storage()
        

    def upload(self, file):
        self.storage.child(file).put(file)
        

    def download(self, name, path = "None123"):
        if name in self.get_all_file_names():
            import os
            if path == "None123":
                path = os.path.basename(name)
                
            self.storage.child(name).download(filename=name, path=path)
            
        else: raise Exception("The file name not found")
        

    def get_all_file_names(self):
        files = []
        for file in self.storage.list_files():
            files.append(file.name)
        return files
    

    def exists(self, name):
        if name in self.get_all_file_names():
            return True
        else: return False


    def download_all(self, path = "None123"):
        import os
        files = self.get_all_file_names()
        for file in files:
            if path == "None123":
                path = os.path.basename(file)
            self.download(file, path)





if __name__ == "__main__":
    data = CloudVariable('https://vari-1fdcf-default-rtdb.asia-southeast1.firebasedatabase.app/')
    #data.save("Name", "Fiad")
    #data.save("Number", 5)
    #data.save("FLOAT", 0.555)
    #print(data.read("Name"))
    #print(data.exists("FLOAT"))
    print(data.get_all_as_dict())

    #data = LocalVariable()
    #data.save("Name", "Fiad")
    #print(data.get_all_as_dict())
    #print(data.read_int("Number"))
