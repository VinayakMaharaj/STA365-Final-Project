# Hot Hand Fallacy Analysis Using Bayesian Inference

In this project, we aim to analyze the "Hot Hand Fallacy" in basketball using Bayesian inference. This file the variables we used in our analysis. The dataset was originally taken from [Kaggle](https://www.kaggle.com/datasets/dansbecker/nba-shot-logs). It details every single shot taken by NBA players in the 2014-15 season until March 04, 2015. We added a few extra variables that were calculated by iterating over this dataset (for full explanation, see 'data_scripts/readme.md').

### List of Variables Used in Analysis

 Here is a list of all the variables included in our models (full list of all variables examined or used throughout the course of this project can be found further below).

- **LOCATION**: Is the game being played at that player's team's arena (home), or in the other team's arena (Away)? "H" for home, "A" for away.
- **SHOT_CLOCK**: Time left in the shot clock (each team has a maximum of 24 seconds to score in a possession).
- **SHOT_DIST**: Distance from basket when shooting in feet.
- **DEFENDER_HEIGHT_CM**: Height of defender in cm.
- **CLOSE_DEF_DIST**: Distance from closest defender in feet.
- **PLAYER_HEIGHT**: Height of the player in cm.
- **HOT_HAND_SHOT_STREAK3**: Do they have a streak of at least 3 shots before the current one?

In our models, we also used the following variable to only select the shots taken by the 15 players who went on a "hot hand streak" the most throughout that season:
- **num_HHS**: Number of shots taken by player in the dataset where the player was on a "hot hand" (previously made three consecutive shots)

