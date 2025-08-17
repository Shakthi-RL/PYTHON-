def timeConversion(s):
    tym=s.split(':')
    hrs=int(tym[0])
    mint=tym[1]
    sec=tym[2][:-2]
    median=tym[2][-2:]
    
    if median=='PM' and hrs!=12:
        hrs+=12
    elif median=='AM' and hrs==12:
        hrs=0
    con_hrs=str(hrs).zfill(2)
    return f"{con_hrs}:{mint}:{sec}:{median}"
    
s = input().strip()
timeConversion(s)