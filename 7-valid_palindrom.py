def isPalindrome(self, s: str) -> bool:
        char = "".join(c.lower() for c in s if c.isalnum())
        n=len(char)
        l=0
        r=n-1

        while l<r:
            if char[l]!=char[r]:
               return False
            l+=1
            r-=1
        return True