import pickle 

class BigDict(object):
    #have a hash that distinguishes files from this specific one? 
    def __init__(self):
        pass
    def __getitem__(self, item):
        try:
            with open('bd_'+item, 'r') as f:
                return pickle.load(f)
                       
        except IOError:
            raise KeyError

    def __setitem__(self, item, value):
        with open('bd_'+item, 'w') as f:
            pickle.dump(value, f)
    def __repr__(self):
        return "<BigDict of type {}>".format(self.dtype)
    def __len__(self):
        with open('bd_' + item, 'r') as f:
            #Other thought: keep this as sa member of the class
            return len(pickle.load(f))

