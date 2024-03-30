import pandas as pd

# goes through dataset and adds two variables: total HHS, total non-HHS
# HHS is "hot hand shots"


if __name__ == "__main__":
    ten_fga_df = pd.read_csv("C:\\Users\\kusha\\OneDrive\\Desktop\\Uni\\Winter_2024\\STA365\\STA365-Final-Project\\data_files\\players_are_filtered.csv")
    # keys = players, values = [num hot hand, num not hot hand]
    players = ten_fga_df["player_name"]
    player_dict = {}
    for player in players:
        rows = ten_fga_df["HOT_HAND_SHOT_STREAK3"][ten_fga_df["player_name"] == player]
        row_indices = rows.index
        num_hhs = sum(rows)
        player_dict[player] = {'indices': row_indices, "shot_data": [num_hhs, len(rows) - num_hhs]}
    
    for player in player_dict:
        print(player)
        ind = player_dict[player]['indices']
        ten_fga_df.loc[ind,'num_HHS'] = player_dict[player]['shot_data'][0]
        ten_fga_df.loc[ind,'num_not_HHS'] = player_dict[player]['shot_data'][1]
        
    ten_fga_df.to_csv("C:\\Users\\kusha\\OneDrive\\Desktop\\Uni\\Winter_2024\\STA365\\STA365-Final-Project\\data_files\\added_num_hhs.csv")

    #  first we'll try naive way and see how long it takes


    # for i in range(len(ten_fga_df)):
    #     player = ten_fga_df[i]
    #     seen_player = player in bool_dict 
    #     if seen_player and bool_dict[player]:
    #         row_ind.append(i)
    #     elif not seen_player:
    #         if player in fga_set:
    #             bool_dict[player] = True
    #         else:
    #             bool_dict[player] = False