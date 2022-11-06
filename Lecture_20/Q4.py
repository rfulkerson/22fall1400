def song_length(mins, sec):
    calc = mins * 60 + sec
    return calc
    
m = int(input("Min: "))
s = int(input("Sec: "))

r = song_length(s,m)


print(f"Length: {r}")