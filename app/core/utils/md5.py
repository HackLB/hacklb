import hashlib

def getmd5(message):    
    """
    Returns MD5 hash of string passed to it.
    """
    return hashlib.md5(message.encode('utf-8')).hexdigest()

def getfilemd5(path):
    md5 = hashlib.md5()
    with open(path,'rb') as f: 
        for chunk in iter(lambda: f.read(8192), b''): 
             md5.update(chunk)
    return md5.hexdigest()