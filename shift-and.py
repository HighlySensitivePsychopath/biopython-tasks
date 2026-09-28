def precompute_masks(pattern, alphabet):
    m=len(pattern)
    char=''
    mask=[0 for c in alphabet]
    for i in range(0,m):
        char=pattern[i]
        mask[char] = mask[char] | (1<<i)
    return mask

def shift_and_all_occurences(text, pattern):
    n=len(pattern)
    m=len(pattern)

    if m>64: return -1

    alphabet = [A, U, T, G, C]
    mask=precompute_masks(pattern, alphabet)

    d=0 # state vector