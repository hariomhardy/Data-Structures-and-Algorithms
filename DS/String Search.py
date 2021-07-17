def longestPrefixSufix(m,mlen):
    lps = [0] * mlen
    i = 0; j= 1
    while i < mlen and j<mlen:
        if m[i] == m[j]:
            i+= 1
            lps[j] = i
            j += 1
        else:
            if i != 0:
                i -= 1
            else:
                i = 0
                j += 1

    #print('in LPS',lps)
    return lps

def KMP(n,m):
    nlen = len(n)
    mlen = len(m)

    l = []    ##indexices for match values

    if nlen < mlen:
        return -1
    if nlen == mlen:
        if n == m:
            return [0]
        return -1

    lps = longestPrefixSufix(m,mlen)
    lps[0] = -1

    i = 0;j = -1
    while i < nlen and j < mlen:
        if n[i] == m[j+1]:
            i += 1
            j += 1
            if j == mlen -1:
                l.append(i-j-1)
                j = lps[j]
        elif i < nlen and n[i] != m[j+1]:
            if j != -1:
                j = lps[j]
            else:
                i+= 1

    return l

def rabinKarp(n,m):
    nlen = len(n)
    mlen = len(m)
    l = []

    d = 256; h =1 ; q = 11   ### values to set h = d^(mlen-1) , q = prime number , d = set of alphabets in string
    p = 0; t = 0
    for i in range(mlen-1):
        h = (h*d)%q
    
    for i in range(mlen):
        p = (d*p + ord(m[i]))%q
        t = (d*t + ord(n[i]))%q

    for i in range(nlen-mlen+1):
        if p == t:
            if m == n[i:i+mlen+1]:
                l.append(i)

        else:
            t = (d*(t-h*ord(n[i]))+ord(n[i+mlen]))%q
            if t<0:
                t += q
    return l



txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print(rabinKarp(txt,pat))
        


