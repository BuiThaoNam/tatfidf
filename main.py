
import tatfidf
import pandas as pd
import operator

def main():
    df = pd.read_csv('data_2020_02_03.csv')
    c = tatfidf.Tatfidf(df)
    c.init()
    c.fit()
    for document in c.top_documents:
        print(document)




if __name__ == '__main__':
    main()
