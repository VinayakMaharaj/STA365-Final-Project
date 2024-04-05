This file explains our data files and scripts in detail. For list of all variables, see below.

### Data Files
**The data file used in the analysis, "hhs_filter.csv", is merely a transformed version of the two datasets mentioned below**. This section explains exactly how we created this file:

The dataset was originally taken from [Kaggle](https://www.kaggle.com/datasets/dansbecker/nba-shot-logs), saved as "shot_logs.csv". We made the following changes and saved it as "shot_logs_final_v2.csv":
- Deleted columns "MATCHUP", "W", "FINAL_MARGIN", "SHOT_RESULT", "TOUCH TIME", "CLOSEST_DEFENDER_PLAYER_ID", "PTS", 
- Added columns "DEFENDER_HEIGHT_CM", "DEFENDER_WEIGHT_KG", "PLAYER_HEIGHT", "PLAYER_WEIGHT", from [here]("https://www.kaggle.com/datasets/justinas/nba-players-data")
- added columns "GAME_HALF", "GAME_CLOCK_DECIMAL"
- Added indicator variables and helper variables for sorting (these were removed anyway).
- Added a column to index our shots starting at 0
- Calculated the total shots taken that game for each player, added as "GAME_SHOTS_TAKEN"
- Calculated the total shots taken that season for each player, added as "SEASON_SHOTS_TAKEN"
- reformatted values of "CLOSEST_DEFENDER" and renamed to "REFORMATED_DEF_NAME"
- Added column "GAME_TIME_ELAPSED" using 'game_time_elapsed.py' from 'data_scripts'
- Added columns "SHOT_STREAK", "HOT_HAND_SHOT_STREAK2", "HOT_HAND_SHOT_STREAK3"

Other data files are simply variations of the same file. The only significant changes that were made were sorting to make python scripts run faster, and filtering out players who averaged less than 10 field goal attempts a game. This initial filter was quickly made irrelevant since we later decided to only include shots from players who took the most shots on a hot hand (we call these "hot hand shots", or "HHS"). To do this, the script "total_hhs_data.py" was used to calculate total number of hot hand shots for each player, and the columns "num_HHS" and "num_not_HHS" were added and saved to "num_hhs_sort.csv". Once this file was sorted by "num_HHS", we used "hhs_filter.py" to only keep shots from 15 players that had the most HHS and saved this to 'hhs_filter.csv'. The original sorting used in "shot_logs_final_v2.csv" was restored.

In short, we only introduced new data from the two links given above, ALL other variables were calculated manually from the existing data in either Excel or Python (see python scripts in 'data_scripts').


### List of All Variables

Here is a list of all the variables that were used over the course of this project. Any other variables not found from the two given links were calculated manually by iterating over the data set (again, scripts can be found in the "data_scripts" folder). 

- **GAME_ID**: A unique ID for that game.
- **LOCATION**: Is the game being played at that player's team's arena (home), or in the other team's arena (Away)? "H" for home, "A" for away.
- **SHOT_NUMBER**: $i^{th}$ shot taken by player in that game.
- **PERIOD**: Which period the shot takes place in (there are four periods in a standard game; if the game is tied at the end of the fourth period then overtime periods are used to determine the winner).
- **GAME_HALF**: 1 if first half (first two periods), 2 if second half (third period or later).
- **GAME_CLOCK**: Time left in the period (minutes and seconds). There are 12 minutes in a regular period, 5 minutes in overtime periods.
- **GAME_CLOCK_DECIMAL**: Time left in the period (minutes).
- **SHOT_CLOCK**: Time left in the shot clock (each team has a maximum of 24 seconds to score in a possession). Filled in missing data with GAME_CLOCK_DECIMAL values since they corresponded to new possessions with less than 24 seconds remaining in the quarter. 
- **DRIBBLES**: Number of dribbles taken by that player.
- **SHOT_DIST**: Distance from basket when shooting in feet.
- **PTS_TYPE**: 2 pointer or 3 pointer.
- **SHOT_RESULT**: Did the shot go in or not.
- **REFORMATED_DEF_NAME**: Name of the defender guarding the player who shoots.
- **DEFENDER_HEIGHT_CM**: Height of defender in cm.
- **DEFENDER_WEIGHT_KG**: Weight of defender in kg.
- **CLOSEST_DEFENDER_PLAYER_ID**: ID of defender guarding/is closest to the shooter.
- **CLOSE_DEF_DIST**: Distance from closest defender in feet.
- **FGM**: Was the field goal made or not.
- **player_name**: Name of the player shooting the ball.
- **player_id**: Unique ID of the player shooting the ball.
- **PLAYER_HEIGHT**: Height of the player in cm.
- **PLAYER_WEIGHT**: Weight of the player in kg.
- **EXCLUDE**: Exclude the player or not (based off of the average number of shots).
- **SEASON_SHOTS_TAKEN**: Number of shots taken by that player over the entire season.
- **GAME_SHOTS_TAKEN**: Number of total shots taken by the player in that game.
- **SHOT_STREAK**: Streak of shots made consecutively (including the current shot).
- **HOT_HAND_SHOT_STREAK2**: Do they have a streak of at least 2 shots before the current one?
- **HOT_HAND_SHOT_STREAK3**: Do they have a streak of at least 3 shots before the current one?
- **GAME_TIME_ELAPSED**: Number of minutes played in the game thus far (in decimal form).
- **num_HHS**: Number of shots taken by player in the dataset where the player was on a "hot hand" (previously made three consecutive shots)
- **num_not_HHS** Number of shots taken by player in the dataset when the player was not on a "hot hand"
