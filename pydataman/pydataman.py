folder = "Data"
extension = ".fiad"

constraint = "7384ht4eh88t75egvrehg7h78thge5t9834j89ertu8"


def is_android():
    try:
        from ctypes import windll
    except:
        return True
    return False

            
def save(name, data):
    # Create the root directory if it doesn't exist
    import os
    if not os.path.exists('Data'):
        import ctypes
        
        if not is_android():
            if not os.path.exists(folder):
                os.makedirs(folder)
            ctypes.windll.kernel32.SetFileAttributesW(folder, 2)

        else:
            if not os.path.exists(folder):
                os.makedirs(folder)
                
    if type(data) is list:
        import pickle
        with open(folder+"\\"+name+extension, 'wb') as fp:
            pickle.dump(data, fp)
            fp.close()
        f = open(folder+"\\"+name+constraint+extension, "w")
        f.write("list")
        f.close()
        
    elif type(data) is dict:
        import pickle
        with open(folder+"\\"+name+extension, 'wb') as fp:
            pickle.dump(data, fp)
            fp.close()
        f = open(folder+"\\"+name+constraint+extension, "w")
        f.write("dict")
        f.close()
        
    elif type(data) is set:
        import pickle
        with open(folder+"\\"+name+extension, 'wb') as fp:
            pickle.dump(data, fp)
            fp.close()
        f = open(folder+"\\"+name+constraint+extension, "w")
        f.write("set")
        f.close()
        
    elif type(data) is tuple:
        import pickle
        with open(folder+"\\"+name+extension, 'wb') as fp:
            pickle.dump(data, fp)
            fp.close()
        f = open(folder+"\\"+name+constraint+extension, "w")
        f.write("tuple")
        f.close()
        
    else:      
        data = data
        f = open(folder+"\\"+name+extension, "w")
        f.write(str(data))
        f.close()
        g = open(folder+"\\"+name+constraint+extension, "w")
        if type(data) is int:
            g.write("int")
        elif type(data) is float:
            g.write("float")
        elif type(data) is str:
            g.write("str")
        elif type(data) is bool:
            g.write("bool")
        g.close()



def read(name):
    # Create the root directory if it doesn't exist
    import os
    if not os.path.exists('Data'):
        import ctypes
        
        if not is_android():
            if not os.path.exists(folder):
                os.makedirs(folder)
            ctypes.windll.kernel32.SetFileAttributesW(folder, 2)

        else:
            if not os.path.exists(folder):
                os.makedirs(folder)
                
    f = read_str(name+constraint)
    if ("list" == f) or ("set" == f) or ("tuple" == f) or ("dict" == f):
        import pickle
        with open (folder+"\\"+name+extension, 'rb') as fp:
            itemlist = pickle.load(fp)
            fp.close()
        return (itemlist)

    if ("int" == f) or ("float" == f) or ("str" == f) or ("bool" == f):
        g = open(folder+"\\"+name+extension, "r")
        data = g.read()
        g.close()

        if "int" == f:
            return int(data)
        elif "float" == f:
            return float(data)
        elif "str" == f:
            return str(data)
        elif "bool" == f:
            return bool(data)


def read_str(name):
    # Create the root directory if it doesn't exist
    import os
    if not os.path.exists('Data'):
        import ctypes
        
        if not is_android():
            if not os.path.exists(folder):
                os.makedirs(folder)
            ctypes.windll.kernel32.SetFileAttributesW(folder, 2)

        else:
            if not os.path.exists(folder):
                os.makedirs(folder)
                
    f = open(folder+"\\"+name+extension, "r")
    data = f.read()
    f.close()
    return str(data)


def exists(name):
    # Create the root directory if it doesn't exist
    import os
    if not os.path.exists('Data'):
        import ctypes
        
        if not is_android():
            if not os.path.exists(folder):
                os.makedirs(folder)
            ctypes.windll.kernel32.SetFileAttributesW(folder, 2)

        else:
            if not os.path.exists(folder):
                os.makedirs(folder)
                
    return os.path.isfile(folder+"\\"+name+extension)


def get_all_as_dict():
    # Create the root directory if it doesn't exist
    import os
    if not os.path.exists('Data'):
        import ctypes
        
        if not is_android():
            if not os.path.exists(folder):
                os.makedirs(folder)
            ctypes.windll.kernel32.SetFileAttributesW(folder, 2)

        else:
            if not os.path.exists(folder):
                os.makedirs(folder)
    variables = {}
    names = os.listdir(folder)
    for i in names:
        var_name = i.replace(extension, "")
        if var_name.endswith(constraint):
            continue
        variables[var_name] = read(var_name)

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
        

    def upload(self, name, file):
        self.storage.child(name+"\\"+file).put(file)
        

    def download(self, name, path):
        import os
        files = list(self.all_vars().keys())
        finaName = ""
        found = False
        for file in files:
            if file.startswith(name):
                fileName = files[files.index(file)]
                found = True            
        else:
            if not found: raise Exception("The file name not found")
        
        path = name + '\\' + path
        self.storage.child(fileName).download(path, os.path.basename(fileName))
        

    def all_vars(self):
        files = {}
        for file in self.storage.list_files():
            files[file.name.split('\\')[0]] = file.name.split('\\')[1]
        return files
    

    def exists(self, name):
        if name in self.get_all_file_names():
            return True
        else: return False


    def download_all(self, path):
        import os
        files = self.all_vars()
        for file in files:
            print(file, os.path.join(path, os.path.basename(files.get(file))))
            directory = os.path.join(path, os.path.basename(files.get(file)))
            self.download(file, directory)





if __name__ == "__main__":
    #data = CloudVariable('https://vari-1fdcf-default-rtdb.asia-southeast1.firebasedatabase.app/')
    #data.save("Name", "Fiad")
    #data.save("Number", 5)
    #data.save("FLOAT", 0.555)
    #print(data.read("Name"))
    #print(data.exists("FLOAT"))
    #print(data.get_all_as_dict())

    #data = LocalVariable()
    #data.save("Num", 9)
    #print(data.get_all_as_dict())
    #print(data.read_list("Name"))
    #print(data.read("Num"))

    firebaseConfig = {
        "apiKey": "AIzaSyBy37khExSIw-XZK2kT17_P1jPSxDt2rjQ",
        "authDomain": "variables-2d2a3.firebaseapp.com",
        "databaseURL": "https://variables-2d2a3-default-rtdb.asia-southeast1.firebasedatabase.app",
        "projectId": "variables-2d2a3",
        "storageBucket": "variables-2d2a3.appspot.com",
        "messagingSenderId": "1058592867243",
        "appId": "1:1058592867243:web:d907865fbabbea2ba208ee",
        "measurementId": "G-C1N0F0ZJ1R",
    }

    data = CloudFile(firebaseConfig, "cred.json")
    #data.upload('setupFile', 'setup.cfg')
    data.download('setupFile', 'setup.cfg')
    #data.download_all("XY")
