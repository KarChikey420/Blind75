def isAnagram(s, t) :
        str1=sorted(s)
        str2=sorted(t)

        if str1==str2:
            return True
        return False