import pandas as pd
# min. field goal attempts per game
FGA_THRESHOLD = 10



if __name__ == '__main__':
    # a convoluted solution than standard pandas operations but has lwoer time complexity (on average at least) :)
    df = pd.read_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project/data_files/shot_logs_final_v2_name_sort.csv")
    fga_df = pd.read_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project/data_files/fga_sort.csv", encoding_errors='ignore')
    failed_threshold = fga_df["Player"][fga_df["FGA"] < FGA_THRESHOLD]
    failed_threshold = [x.lower() for x in failed_threshold]
    weird_names = []
    for player in failed_threshold:
        if "?" in player:
            weird_names.append(player)
    
    
    row_indices = []
    bool_dict = {}
    big_df_players = df["player_name"]
    for i in range(len(big_df_players)):
        player = big_df_players[i]
        seen_player = player in bool_dict 
        if seen_player and bool_dict[player]:
            row_indices.append(i)
        elif not seen_player:
            if player in failed_threshold:
                bool_dict[player] = True
                row_indices.append(i)
            else:
                bool_dict[player] = False

    df.drop(index=row_indices, inplace=True)
    df.to_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project/data_files/fga_filter.csv")
    pd.Series(data=weird_names).to_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project/data_files/weird_names.csv")
    