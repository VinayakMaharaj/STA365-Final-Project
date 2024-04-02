import pandas as pd

N = 50

if __name__ == '__main__':
    df = pd.read_csv("C:\\Users\\kusha\\OneDrive\\Desktop\\Uni\\Winter_2024\\STA365\\STA365-Final-Project\\data_files\\num_hhs_sort.csv")
    drop_index = df.groupby('player_name').head(1).index[N]
    df.drop(index=list(range(drop_index, len(df))), inplace=True)
    df.to_csv("C:\\Users\\kusha\\OneDrive\\Desktop\\Uni\\Winter_2024\\STA365\\STA365-Final-Project\\data_files\\hhs_filter_v2.csv")
