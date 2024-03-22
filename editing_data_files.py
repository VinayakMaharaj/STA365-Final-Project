import pandas as pd

def add_game_time_elapsed(df):
    """Add game_time_elapsed variable to given pandas df and return
    in a game there are 4 quarters/periods of 12 minutes each 
    (if the game is tied after 4 quarters then there are overtime periods of 5 minutes each)
    so if its period 2 with 5 minutes left, then 19 total minutes have elapsed
    """
    
    # intialize new column with -1 values
    df["GAME_TIME_ELAPSED"] = -1
    
    # if there have have been more than 4 periods (aka overtime), then dont change anything. 
    # otherwise, calculate how many minutes have been played
    df["GAME_TIME_ELAPSED"] = df["GAME_TIME_ELAPSED"].where(df["PERIOD"] > 4, other = (df["PERIOD"] - 1)*12 + (12 - df["GAME_CLOCK_DECIMAL"]))
    
    # if there have have been less than 5 periods (no overtime), then dont change anything. 
    # otherwise, calculate how many minutes have been played
    df["GAME_TIME_ELAPSED"] = df["GAME_TIME_ELAPSED"].where(df["PERIOD"] < 5, other = (df["PERIOD"] - 5)*5 + (5 - df["GAME_CLOCK_DECIMAL"]) + 48)
    return df


if __name__ == "__main__":
    csv_v1 = pd.read_csv("C://Users//kusha//OneDrive//Desktop//Uni//Winter_2024//STA365//STA365-Final-Project//shot_logs_final_v1.csv")
    add_game_time_elapsed(csv_v1).to_csv("C://Users//kusha//OneDrive//Desktop//Uni//Winter_2024//STA365//STA365-Final-Project//shot_logs_final_v1.csv")

    csv_v2 = pd.read_csv("C://Users//kusha//OneDrive//Desktop//Uni//Winter_2024//STA365//STA365-Final-Project//shot_logs_final_v2.csv")
    add_game_time_elapsed(csv_v2).to_csv("C://Users//kusha//OneDrive//Desktop//Uni//Winter_2024//STA365//STA365-Final-Project//shot_logs_final_v2.csv")
