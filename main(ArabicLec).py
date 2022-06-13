import re as rgx
import random

from scipy import rand

data = {"hi": " --> Hello (friendly)", "tree": "a woody perennial plant, typically having a single stem or trunk growing to a considerable height and bearing lateral branches at some distance from the ground."}
# print(len(data))
pins = list()
cmd = None
attr = None
wrd = None
vlu = None
tits = [cmd, attr, wrd, vlu]


def assign_values(inputString):
    x = inputString.split()
    y = inputString.strip().lower()

    if len(x) == 2:
        cmd = x[0].lower()
        wrd = x[1].lower()
        attr = None
        vlu = None
    elif len(x) == 3:
        cmd = x[0].lower()
        attr = x[1].lower()
        wrd = x[2].lower()
        vlu = None
    elif len(x) == 4:
        cmd = x[0].lower()
        wrd = x[1].lower()
        attr = x[2].lower()
        vlu = x[3].lower()
    else:
        cmd = cmd = x[0].lower()
        wrd = x[1].lower()
        attr = x[2].lower()
        vlu = rgx.findall('.*-vlu\s"(.*)"', y)[0]
    return [cmd, attr, wrd, vlu]


while True:
    pin = input("Enter command: ")
    if pin.upper() == "EXIT":
        break
    else:
        pins = assign_values(pin)
    cmd = pins[0]
    attr = pins[1]
    wrd = pins[2]
    vlu = pins[3]
    if cmd == 'get':
        if attr == '-rt':
            if rgx.search("^ -->", data[wrd]):
                print(rgx.findall(" --> (\S+) ", data[wrd])[0])
            else:
                print("The word " + wrd+' is already a root lemma')
        elif wrd == 'size':
            print("The number of known words:", len(data))
        else:
            if wrd not in data:
                print(wrd, 'is not known at the moment.')
            else:
                print(data[wrd])
    if cmd == 'add':
        if attr == '-ln':
            if vlu not in data:
                print("The lemma "+vlu+" doesn't exist to be used as a root.")
            else:
                if random.randint(0, 100) > 20:
                    data[wrd] = " --> " + vlu
                else:
                    continue
        if attr == "-vlu":
            if random.randint(0, 100) > 50:
                data[wrd] = vlu
            else:
                continue
quit()
