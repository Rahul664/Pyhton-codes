n = int(input())
cst = list(map(int, input().split()[:n]))
typ = list(map(int, input().split()[:n]))
trns = []
auth = []
auth_trns = []
for i in range(0, n):
    if typ[i] == 1:
        trns.append(cst[i])
    elif typ[i] == 2:
        auth.append(cst[i])
    else:
        auth_trns.append(cst[i])
if len(trns)==0 and len(auth)==0:
    print(min(auth_trns))
elif len(trns)==0 or len(auth)==0:
    print(min(auth_trns))
elif len(auth_trns)==0:
    print(min(auth)+min(trns))
else:
    print(min(min(trns) + min(auth), min(auth_trns)))