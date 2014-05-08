def main():
    all = {}
    f = open("pinyin.txt")
    f2 = open("PYTable.txt", "w")
    for l in f:
        l = l.strip()
        if not l: continue
        ll = l.split()
        w = ll[0]
        all = []
        f2.write(w)
        f2.write("\t")
        for py in ll[1:]:
            if py[0] not in all:
                all.append(py[0])
        f2.write("\t".join(all))
        f2.write("\n")

    f.close()
    f2.close()

if __name__ == '__main__':
    main()
