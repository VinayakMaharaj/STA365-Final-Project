# Hot Hand Fallacy Analysis Using Bayesian Inference

In this project, we aim to analyze the "Hot Hand Fallacy" in basketball using Bayesian inference.

## Dataset

The dataset was originally taken from [Kaggle](https://www.kaggle.com/datasets/dansbecker/nba-shot-logs). We have slightly modified this in `shot_logs_final_v1.csv` and `shot_logs_final_v2.csv`. The variables for `v2` are explained below.

### Variables

- **GAME_ID**: A unique ID for that game.
- **LOCATION**: Is the game being played at that player's team's arena (home), or in the other team's arena (Away)? "H" for home, "A" for away.
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
