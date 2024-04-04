# Hot Hand Fallacy Analysis Using Bayesian Inference

In this project, we aim to analyze the "Hot Hand Fallacy" in basketball using Bayesian inference. This file explains the variables used in our analysis.

### Variables kept in analysis

The dataset was originally taken from [Kaggle](https://www.kaggle.com/datasets/dansbecker/nba-shot-logs). It details every single shot taken by NBA players in the 2014-15 season until early March 2015. We added a few extra variables that were calculated by iterating over this dataset (see 'data_scripts' folder). Here is a list of all the variables included in our models (full list of all variables examined or used throughout the course of this project can be found further below).

- **LOCATION**: Is the game being played at that player's team's arena (home), or in the other team's arena (Away)? "H" for home, "A" for away.
- **SHOT_CLOCK**: Time left in the shot clock (each team has a maximum of 24 seconds to score in a possession).
- **SHOT_DIST**: Distance from basket when shooting in feet.
- **DEFENDER_HEIGHT_CM**: Height of defender in cm.
- **CLOSE_DEF_DIST**: Distance from closest defender in feet.
- **PLAYER_HEIGHT**: Height of the player in cm.
- **HOT_HAND_SHOT_STREAK3**: Do they have a streak of at least 3 shots before the current one?

In our models, we also used the following variable to only select the shots taken by the 15 players who went on a "hot hand streak" the most throughout that season:
- **num_HHS**: Number of shots taken by player in the dataset where the player was on a "hot hand" (previously made three consecutive shots)

### List of all variables

Here is a list of all the variables that were ever used over the course of this project. **SEASON_SHOTS_TAKEN** was extracted from this [dataset](https://stathead.com/tiny/ikyTe) for filtering purposes, but was abandoned soon after. Any other variables not found from the two given links were calculated manually by iterating over the data set (again, scripts can be found in the "data_scripts" folder). 

- **GAME_ID**: A unique ID for that game.
- **LOCATION**: (See above)
- **SHOT_NUMBER**: \(i^{th}\) shot taken by player in that game.
- **PERIOD**: Which period the shot takes place in (there are four periods in a standard game; if the game is tied at the end of the fourth period then overtime periods are used to determine the winner).
- **GAME_HALF**: 1 if first half (first two periods), 2 if second half (third period or later).
- **GAME_CLOCK**: Time left in the period (minutes and seconds). There are 12 minutes in a regular period, 5 minutes in overtime periods.
- **GAME_CLOCK_DECIMAL**: Time left in the period (minutes).
- **SHOT_CLOCK**: Time left in the shot clock (each team has a maximum of 24 seconds to score in a possession).
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
