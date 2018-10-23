class Vovel(object):
    def __getattribute__(self, name):
        if  set(name).issubset('eioau'):
            return str(name)
        else:
            raise AttributeError("Vovel instance has no attribute '{}'".format(name))
