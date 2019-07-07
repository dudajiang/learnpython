a = {
    'int1': 1,
    'int2': 2
}

b = {
    'float1': 1.5,
    'float2': 2.1
}


def getdict(aa, bb):
    _conf_ints = [(key, int(value)) for key, value in aa.items()]
    _conf_floats = [(key, float(value)) for key, value in bb.items()]
    print(aa)
    print(bb)
    print(_conf_ints+_conf_floats)
    return dict(_conf_ints + _conf_floats)

def main():
    cc = getdict(a, b)
    print(cc)


if __name__ == '__main__':
    main()
