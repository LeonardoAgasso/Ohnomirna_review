#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
from matplotlib_venn import venn2


def venn_diagram(list1, list2):
    venn =venn2(subsets = (set(list1), set(list2)), set_labels = ('Ohno-miRNAs', 'Paralog-miRNAs'))

    venn.set_labels[0].set_color('forestgreen')
    venn.set_labels[1].set_color('firebrick')

    venn.patches[0].set_facecolor('forestgreen')
    venn.patches[1].set_facecolor('firebrick')
    venn.patches[2].set_facecolor('darkolivegreen')

    venn.patches[0].set_alpha(0.3)
    venn.patches[1].set_alpha(0.3)
    venn.patches[2].set_alpha(0.6)

    venn.get_label_by_id('10').set_fontsize(10)
    venn.get_label_by_id('01').set_fontsize(10)

    plt.savefig("vennDiagram_ohnoMirnas_paralogMirnas.png")
    plt.show()

def print_output(list1, list2):s
    with open("intersection_ohnoMirnas_paralogMirnas.txt", "w") as f:
        for i in list1:
            if i in list2:
                f.write(i + "\n")

def main():   
    with open(sys.argv[1]) as f:
        list1 = f.read().splitlines()
    with open(sys.argv[2]) as f:
        list2 = f.read().splitlines()

    venn_diagram(list1, list2)
    print_output(list1, list2)


if __name__ == "__main__":
    main()
