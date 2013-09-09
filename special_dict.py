import pickle 

class BigDict(object):
    #have a hash that distinguishes files from this specific one? 
    def __init__(self):
        self.all_keys = set()
        pass

    def __getitem__(self, item):

        if item in self.all_keys:
            with open('.bd'+repr(hash(self)) + '_' + str(item), 'r') as f:
                return pickle.load(f)
                       
        else:
            raise KeyError

    def __setitem__(self, item, value):
        self.all_keys.add(item)
        with open('.bd' + repr(hash(self)) + '_' + str(item), 'w') as f:
            pickle.dump(value, f)

    def __repr__(self):
        return "<BigDict {}>".format(hash(self))

    def __len__(self):
        return len(self.all_keys)

    def keys(self): #Is this a bad idea? Maybe, but I like the idea of replicating
        #All of the functionality of a normal dictionary (except speed of course)
        return list(self.all_keys)

    def values(self): #Warning: probably horrible runtime
        vals = []
        for key in self.all_keys:
            vals.append(self[key])
        return vals

    def items(self):
        #Also horrible runtime
        itms = []
        for key in self.all_keys:
            itms.append((key, self[key]))


