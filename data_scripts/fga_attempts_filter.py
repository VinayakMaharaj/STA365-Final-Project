import pandas as pd
# min. field goal attempts per game
FGA_THRESHOLD = 10



if __name__ == '__main__':
    # a convoluted solution than standard pandas operations but has lwoer time complexity (on average at least) :)
    df = pd.read_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project/data_files/shot_logs_final_v2_name_sort.csv")
    fga_df = pd.read_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project//data_files/fga_sort.csv", encoding_errors='ignore')
    players = fga_df["Player"][fga_df["FGA"] < FGA_THRESHOLD]
    fga_set = set()
    weird_names = []
    

    
    row_ind = []
    bool_dict = {}
    big_df_players = df["player_name"]
    for i in range(len(big_df_players)):
        player = big_df_players[i]
        seen_player = player in bool_dict 
        if seen_player and bool_dict[player]:
            row_ind.append(i)
        elif not seen_player:
            if player in fga_set:
                bool_dict[player] = True
            else:
                bool_dict[player] = False
    

    df = df.drop(index=row_ind)
    df.to_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project/data_files/players_are_filtered.csv")
    pd.Series(data=weird_names).to_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project/data_files/weird_names.csv")
    # for player in players:
    #     try:
    #         df = df.drop(df[df["player_name"] == player].index)
    #         print(player)
    #     except:
    #         weird_names.append(player)
    #         print(player)
    #         continue
    # df.to_csv("C:/Users/kusha/OneDrive/Desktop/Uni/Winter_2024/STA365/STA365-Final-Project/data_files/players_are_filtered.csv")
        
    

    
    # print(fga_df["Player"][20])