#-*- encoding: utf-8 -*-

import alpha as AL


def main():
    print("i\'m user")

    userobject = AL.ALPHA()
    print(userobject)

    getprint = userobject.collect()
    getprint("senddata")



if __name__ == '__main__':
    main()
