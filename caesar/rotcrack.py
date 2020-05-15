# Using methods discussed here:
# https://eddmann.com/posts/implementing-rot13-and-rot-n-caesar-ciphers-in-python/

def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

msg = input("Enter CipherText: ")

for x in range(26):
    res = rot_alpha(x+1)(msg)
    print('ROT #%s: %s' % (x, res))