import pandas as pd
from matplotlib import pyplot as plt


def trait_irm(file):
    row_file = open("input-data/" + file, "r")
    row_data = row_file.readlines()
    coercivity = row_data[60].split()

    return float(coercivity[-1])


def trait_his(file):
    row_file = open("input-data/" + file, "r")
    row_data = row_file.readlines()
    saturation = row_data[59].split()
    remanence = row_data[60].split()
    coercivity = row_data[61].split()

    return float(saturation[-1]), float(remanence[-1]), float(coercivity[-1])


def create_table(list_his, list_irm, list_name):
    data = []
    columns_name = ["Amostra", "Hc", "Hcr Coercivity (remanent) IRM", "Ms", "Mrs", "Hcr/Hc", "Mrs/Ms"]
    for his, irm, name in zip(list_his, list_irm, list_name):
        hcr = trait_irm(irm)
        ms, mrs, hc = trait_his(his)

        hcr_hc = hcr / hc
        mrs_ms = mrs / ms

        data.append([name, hc, hcr, ms, mrs, hcr_hc, mrs_ms])

    table = pd.DataFrame(data, columns=columns_name)
    table.to_excel("output-data/day_plot_ct.xlsx")
    return table


def plot(table):
    # figure, ax1 = plt.plot(1, figsize=(10, 5))

    plt.scatter(table["Hcr/Hc"], table["Mrs/Ms"], color='royalblue')
    plt.xlabel(r'$H_{cr} / {H_c}$')
    plt.ylabel(r'$M{rs} / M_{s}$')
    plt.xticks([0, 1, 2, 3, 4, 5, 6])
    plt.yticks([0, .1, .2, .3, .4, .5, .6])
    plt.hlines(0.05, -100, 100, color='k', alpha=0.5, linestyle='solid')
    plt.hlines(0.5, -100, 100, color='k', alpha=0.5, linestyle='solid')
    plt.vlines(1.5, -100, 100, color='k', alpha=0.5, linestyle='solid')
    plt.vlines(4, -100, 100, color='k', alpha=0.5, linestyle='solid')
    plt.xlim(0, 6)
    plt.ylim(0, 0.6)

    plt.tight_layout()
    plt.savefig("output-data/dayplot-1.png", dpi=200)
    plt.text(0.65, 0.55, weight="heavy", s='SD')
    plt.text(2.7, .25, weight="heavy", s='PSD')
    plt.text(4.8, .02, weight="heavy", s='MD')
    plt.savefig("output-data/dayplot-2.png", dpi=200)
    plt.close()
