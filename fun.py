

class Collection():
    def __init__(self,base):
        self.base = base
        
    def __getitem__(self,key):
        #print(key)
        if(isinstance(key,int) or isinstance(key,slice)):
            try:
                return[item[key] for item in self.base.values()]
            except:
                raise IndexError('index out of range')
        if(isinstance(key,list) or isinstance(key,tuple) ):
            try:
                output = []
                for subkey in key:
                    partial =  self[subkey]
                    if(isinstance(subkey,slice)):
                        output.extend(partial)
                    else:
                        output += [partial]
                return output
            except:
                raise IndexError('index out of range list')            
        if(isinstance(key,str)):
            if(key not in self.base):
                raise KeyError(f'{key} does not exist in collection')
            return self.base[key]
        raise TypeError('key must be a string or positive integer')
        
    def __repr__(self):
        return f'collection={self.base}'
    
collection =  Collection({'country':['eeuu','canada','colombia','eeuu','canada','colombia'],'state':['california','toronto','bogota','california','toronto','medellin']})    
#print(collection[[slice(0,2),slice(-2,None)]])
print(collection[0:2,-2])

#print(collection[-2:])
