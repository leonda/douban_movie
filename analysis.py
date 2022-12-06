import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def draw(address, year, bottom):

    file = pd.read_csv(address, header=None, names=[
        'MovieName', 'Rating', 'Genre_Main', 'Area', 'ReleaseTime', 'BoxOffice'])
    df = pd.DataFrame(file)
    df1 = df.groupby('Area', as_index=True)['Area'].count()
    df1 = pd.DataFrame(df1)
    df1.columns = ['num']
    x_data = df1.index
    y_data = df1['num']

    # 正确显示中文和负号
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    # 画图，plt.bar()可以画柱状图
    for i in range(len(x_data)):
        plt.bar(x_data[i], y_data[i])
    plt.title("Number of films in " + year)
    plt.xlabel("Area")
    plt.ylabel("Num")
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=bottom)

    plt.show()
    # plt.savefig('./data/' + year + '.png')


if __name__ == '__main__':
    # for year in range(2009, 2023):
    #     address = './data/' + str(year)+'.csv'
    #     draw(address, str(year))
    year = 2014
    bottom = 0.6
    address = './data/' + str(year)+'.csv'
    draw(address, str(year), bottom)
