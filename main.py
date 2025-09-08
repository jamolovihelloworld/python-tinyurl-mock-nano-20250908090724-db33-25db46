import hashlib
s='nanojamol'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
