import hashlib
s='projamol'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
