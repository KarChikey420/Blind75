def longest_substring(s):
    Charset=set()
    left=0
    ans=0
    
    for right in range(len(s)):
        while s[right] in Charset:
            Charset.remove(s[left])
            left+=1
        Charset.add(s[right])
        ans=max(ans,right-left+1)
    return ans

if __name__=="__main__":
    s="abcabcbb"
    print(longest_substring(s))