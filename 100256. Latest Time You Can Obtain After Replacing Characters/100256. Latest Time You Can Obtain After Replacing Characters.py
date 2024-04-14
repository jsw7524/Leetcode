class Solution:
    def findLatestTime(self, s: str) -> str:
        hh, MM = s.split(":")
        if hh[0]=="?" and hh[1]=="?":
            hh=f"{11}"  
        elif hh[0]=="?":
            if hh[1]=="0":
                hh=f"1{hh[1]}"            
            elif hh[1]=="1":
                hh=f"1{hh[1]}" 
            else:
                hh=f"0{hh[1]}"
                
        elif hh[1]=="?":
            if hh[0] == "0":
                hh=f"{hh[0]}9"
            else:
                hh=f"{hh[0]}1"
        
        if MM[0]=="?" and MM[1]=="?":
            MM="59"
        elif MM[0]=="?":
            MM=f"5{MM[1]}"
        elif MM[1]=="?":
            MM=f"{MM[0]}9"
            
        return f"{hh}:{MM}"
    
sln=Solution()

assert "02:29"==sln.findLatestTime(s = "?2:2?")

assert "10:40"==sln.findLatestTime(s = "?0:40")
assert "03:12"==sln.findLatestTime(s = "?3:12")
assert "09:59"==sln.findLatestTime(s = "0?:5?")
assert "11:54"==sln.findLatestTime(s = "1?:?4")


