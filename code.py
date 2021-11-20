import string


def collector(input, output):
    with open(input, encoding="utf-8") as file:
        inptext = file.read()
        inptext = [i.strip(string.punctuation + "–")
                   for i in inptext.lower().split()]
        inptext = [i for i in inptext if i]
    k = {}
    for w in inptext:
        k[w] = k.get(w, 0) + 1
    outtext = []
    for w, count in k.items():
        outtext.append(f"{w} {str(count)}")
    with open(output, "w", encoding="utf-8") as file:
        file.write("\n".join(outtext) + "\n")


collector('input.txt', 'output.txt')
