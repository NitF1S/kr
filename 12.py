f = open('mat_dv')

def age(11):
    all = []

    for elem in 11:
        all.append(int(elem[3]+ elem[4]))

    for elem in 11:
        if max(all) == int(elem[3]+ elem[4]):
            print('Winner - {elem[2]} - elem{0}elem{1}')

winalg = []
wingeom = []
s = []


for elem in f:
    s = elem.split()

    if max(winalg) == int(s[3]):
        print(f'Winner algebra - {s[0]}[s[1]]')

    if max(wingeom) == int(s[4]):
        print(f'Winner geometry - {s[0]}{s[1]}')


for i in f:
    s = i.split()

    winalg.append(int(s[3]))
    wingeom.append(int(s[3]))

    if s[2] == '8':
        f8.append(s)

    if s[2] == '9':
        f9.append(s)

    if s[2] == '10':
        f9.append(s)

    if s[2] == '11':
        f9.append(s)

print(s)
print(winalg)
print(wingeom)
