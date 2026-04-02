# Hot Hand Insight — Bayesian Analysis of NBA Shooting Patterns
 
A statistical research project applying Bayesian inference to investigate the "Hot Hand Fallacy" in NBA shooting. Built and presented as a final project for STA365 (Bayesian Statistics) at the University of Toronto — presented to the class and the UofT Statistics department head.
 
---
 
## The Research Question
 
The "Hot Hand Fallacy" is the belief that a basketball player who has made several consecutive shots is more likely to make their next shot — that they are "on fire." Classical statistics has largely dismissed this as a cognitive bias. This project asks: **when we properly control for shot difficulty, defender proximity, game context, and player height, does evidence of a hot hand effect actually emerge?**
 
---
 
## Approach
 
We analyzed every shot taken by 15 NBA players during the 2014-15 season who exhibited the most "hot hand streaks" — defined as having made at least 3 consecutive shots prior to the current attempt.
 
Rather than a simple frequency analysis, we built **multivariate Bayesian regression models** in PyMC that account for confounding variables simultaneously, giving a more honest picture of whether streak shooting predicts future success after controlling for context.
 
Three prior specifications were compared to assess robustness:
 
| Model | Prior | Purpose |
|---|---|---|
| Model 1 | Multivariate Normal | Baseline — assumes moderate, symmetric uncertainty across all predictors |
| Model 2 | Horseshoe | Sparse — shrinks irrelevant predictors toward zero; better for high-dimensional settings |
| Model 3 | Spike-and-Slab | Explicit variable selection — forces a binary include/exclude decision per predictor |
 
Comparing these three allowed us to assess whether the hot hand signal was robust across different assumptions about which variables matter, or whether it was an artifact of prior choice.
 
---
 
## Dataset
 
**Primary:** [NBA Shot Logs 2014-15](https://www.kaggle.com/datasets/dansbecker/nba-shot-logs) — every shot attempt in the 2014-15 NBA season through March 4, 2015.
 
**Supplementary:** [NBA Players Data](https://www.kaggle.com/datasets/justinas/nba-players-data) — player physical attributes merged by player ID.
 
Additional engineered variables were computed by iterating over the shot log dataset (see `data_scripts/` for full explanation).
 
---
 
## Variables
 
| Variable | Description |
|---|---|
| `LOCATION` | Home (H) or Away (A) game |
| `SHOT_CLOCK` | Seconds remaining on the shot clock (max 24s) |
| `SHOT_DIST` | Distance from basket at time of shot (feet) |
| `DEFENDER_HEIGHT_CM` | Height of the closest defender (cm) |
| `CLOSE_DEF_DIST` | Distance from closest defender (feet) |
| `PLAYER_HEIGHT` | Shooter's height (cm) |
| `HOT_HAND_SHOT_STREAK3` | Binary — did the player make 3+ consecutive shots before this attempt? |
| `num_HHS` | Total hot hand streak shots taken by the player in the dataset (used for player filtering) |
 
---
 
## Repository Structure
 
```
├── data_files/               # Cleaned and merged datasets
├── data_scripts/             # Scripts for feature engineering and variable construction
│   └── readme.md             # Detailed explanation of engineered variables
├── models/                   # Saved model outputs and posterior samples
├── Video_Notebook_Final.ipynb    # Final analysis notebook (presented version)
├── Video_Notebook_JM_comments.ipynb  # Annotated version with instructor feedback
└── Video_Notebook_old.ipynb  # Iterative development notebook
```
 
---
 
## Tech Stack
 
| Tool | Purpose |
|---|---|
| Python | Primary language |
| PyMC | Bayesian model building and sampling |
| NumPy / Pandas | Data processing and feature engineering |
| SciPy | Statistical testing and diagnostics |
| Matplotlib / ArviZ | Posterior visualization and model diagnostics |
 
---
 
## Sampling & Diagnostics
 
All models were sampled using **Markov Chain Monte Carlo (MCMC)** via PyMC's default NUTS sampler, with **Metropolis-Hastings** used selectively to reduce divergences in the Horseshoe and Spike-and-Slab models. Model divergences were reduced by 20% through prior tuning and sampler configuration.
 
Posterior diagnostics included:
- R-hat convergence checks
- Effective sample size (ESS) evaluation
- Posterior predictive checks
- Trace plot inspection
 
---
 
## Key Design Decisions
 
**Why Bayesian over frequentist?**
Frequentist approaches to the hot hand question typically test a single null hypothesis and discard uncertainty. Bayesian inference gives us a full posterior distribution over the effect size — we can directly ask "how probable is a positive hot hand effect?" rather than just "can we reject zero?"
 
**Why three prior specifications?**
A finding that only appears under one prior is fragile. Comparing Multivariate Normal, Horseshoe, and Spike-and-Slab priors lets us assess whether the hot hand signal is genuine or a prior artifact. Robust findings should be consistent across reasonable prior choices.
 
**Why filter to 15 players?**
Most players never hit three consecutive shots in a stretch long enough to study. Filtering to the 15 players with the most hot hand streak shots gives sufficient within-player data to estimate the effect without conflating player ability differences.
 
---
 
## Authors
 
Team of 4 — University of Toronto, STA365 Bayesian Statistics
