class LocalVariable:
    
    def __init__(self):
        self.folder = "Data"
        self.extension = ".fiad"
        import os
        import ctypes
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        ctypes.windll.kernel32.SetFileAttributesW(self.folder, 2)

            
    def save(self, name, data):
        if type(data) is list:
            import pickle
            with open(self.folder+"\\"+name+self.extension, 'wb') as fp:
                pickle.dump(data, fp)
                fp.close()
        elif type(data) is dict:
            import pickle
            with open(self.folder+"\\"+name+self.extension, 'wb') as fp:
                pickle.dump(data, fp)
                fp.close()
        elif type(data) is set:
            import pickle
            with open(self.folder+"\\"+name+self.extension, 'wb') as fp:
                pickle.dump(data, fp)
                fp.close()
        elif type(data) is tuple:
            import pickle
            with open(self.folder+"\\"+name+self.extension, 'wb') as fp:
                pickle.dump(data, fp)
                fp.close() 
        else:      
            data = str(data)
            f = open(self.folder+"\\"+name+self.extension, "w")
            f.write(data)
            f.close()


    def read_int(self, name):
        f = open(self.folder+"\\"+name+self.extension, "r")
        data = f.read()
        f.close()
        return int(data)


    def read_float(self, name):
        f = open(self.folder+"\\"+name+self.extension, "r")
        data = f.read()
        f.close()
        return float(data)


    def read_str(self, name):
        f = open(self.folder+"\\"+name+self.extension, "r")
        data = f.read()
        f.close()
        return str(data)


    def read_bool(self, name):
        f = open(self.folder+"\\"+name+self.extension, "r")
        data = f.read()
        f.close()
        return bool(data)


    def read_list(self, name):
        import pickle
        with open (self.folder+"\\"+name+self.extension, 'rb') as fp:
            itemlist = pickle.load(fp)
            fp.close()
        return list(itemlist)


    def read_set(self, name):
        import pickle
        with open (self.folder+"\\"+name+self.extension, 'rb') as fp:
            itemlist = pickle.load(fp)
            fp.close()
        return set(itemlist)


    def read_tuple(self, name):
        import pickle
        with open (self.folder+"\\"+name+self.extension, 'rb') as fp:
            itemlist = pickle.load(fp)
            fp.close()
        return tuple(itemlist)


    def read_dict(self, name):
        import pickle
        with open (self.folder+"\\"+name+self.extension, 'rb') as fp:
            itemlist = pickle.load(fp)
            fp.close()
        return dict(itemlist)




class CloudVariable:
    
    def __init__(self, url):
        from firebase import firebase
        self.firebase = firebase.FirebaseApplication(url, None)


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



if __name__ == "__main__":
    data = CloudVariable('https://variables-2d2a3-default-rtdb.asia-southeast1.firebasedatabase.app/')
    #data.save("Name", "Fiad")
    #data.save("Number", 5)
    data.save("FLOAT", 0.555)
    print(data.read("FLOAT"))

    #data = LocalVariable()
    #print(data.read_int("Number"))
