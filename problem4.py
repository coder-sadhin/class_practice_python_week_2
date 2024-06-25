inp = input()
spos = input()
if(inp[0]=="["):
    inp=eval(inp)

char_at_pos = lambda r, s: r[1::2] if s == "even" else r[0::2]
print(char_at_pos(inp,spos))