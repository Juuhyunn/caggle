import pandas as pd
import matplotlib.pyplot as plt


def process():
    train = pd.read_csv('data/train.csv')
    # 훈련 데이터 확인
    print(train.head(5))
    # 결측치 확인
    # null 값이 있는지 확인
    print(train.isnull().sum())
    '''
    PassengerId      0
    Survived         0
    Pclass           0
    Name             0
    Sex              0
    Age            177
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    dtype: int64
    '''
    # 성별 차트 확인하기
    show_pie_chart(train, 'Sex')


def show_pie_chart(train, col):
    colname_survived = survived_crosstab(train, col)
    pie_chart(colname_survived)
    return colname_survived


def survived_crosstab(df, col_name):
    '''col_name과 Survived간의 교차도표 생성'''
    feature_survived = pd.crosstab(df[col_name], df['Survived'])
    feature_survived.columns = feature_survived.columns.map({0:"Dead", 1:"Alive"})
    return feature_survived


def pie_chart(feature_survived):
    '''
    pie_chart 생성
    pcol, prow = 차트를 출력할 개수. pcol * prow 만큼의 차트 출력
    '''
    frows, fcols = feature_survived.shape
    pcol = 3
    prow = (frows/pcol + frows%pcol)
    plot_height = prow * 2.5
    plt.figure(figsize=(8, plot_height))
    for row in range(0, frows):
        plt.subplot(prow, pcol, row+1)
        index_name = feature_survived.index[row]
        plt.pie(feature_survived.loc[index_name], labels=feature_survived.loc[index_name].index, autopct='%1.1f%%')
        plt.title("{0}' survived".format(index_name))

    plt.show()


if __name__ == '__main__':
    process()