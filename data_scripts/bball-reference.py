import pandas as pd

# min. field goal attempts per game
FGA_THRESHOLD = 10



if __name__ == '__main__':
    df = pd.read_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project/data_files/shot_logs_final_v2.csv")
    fga_df = pd.read_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project//data_files/fga_sort.csv", encoding_errors='ignore')
    weird_names = []
    # figure out ? in player names
    players = fga_df["Player"][fga_df["FGA"] < FGA_THRESHOLD]
    for player in players:
        try:
            df = df.drop(df[df["player_name"] == player].index)
            print(player)
        except:
            weird_names.append(player)
            print(player)
            continue
        finally:
            df.to_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project/data_files/players_are_filtered.csv")
        
    # print(fga_df["Player"][20])