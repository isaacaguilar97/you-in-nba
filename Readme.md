## PROJECT DESCRIPTION  
The purpose of this project is to create a Dashboard in Streamlit that helps anyone interested in improving their basketball skills, know where to focus their training based on their height, desired position, and desired performance.  

 ## CONTENT  
NBA_project.ipynb: Where all the code resides  
feedback: Folder with text files containg peer feedback to improve the project process  
data: Folder with tables containing saved data from API  
.gitignore: files I don't want to show up in my repository  


## DATA SUMMARY  
**Season:** 2023  
**NBA teams:** 11  
**Number of Players:** 30  
**Columns:** 32  
**API:** "https://rapidapi.com/api-sports/api/api-nba"  
**Restrictions:** There is a limit of 100 queries per day for the free version of the API. I formated the script so we could add more players and teams to the final_table.csv  

## Helpful Descriptions  
*POSITIONS*  
- PG - Point Guard: The primary ball handler, responsible for setting up plays and often the smallest player on the team.
- SG - Shooting Guard: Often a strong scorer and perimeter shooter. May also be involved in bringing the ball up the court.
- SF - Small Forward: A versatile player who can score both inside and outside. Small forwards are often good at rebounding and defending.
- F - Forward: This is a generic term for a player who plays in the forward position. It could refer to either a small forward or power forward.
- G - Guard: Similar to "F," this is a generic term for a player who plays in the guard position. It could refer to either a point guard or shooting guard.
- PF - Power Forward: Typically a strong and physical player who plays close to the basket. They are often involved in rebounding and scoring in the post.

*STATS*  
- PTS - Points: The total number of points a player scores during a basketball game.
- MIN - Minutes: The total time a player spends actively participating in a basketball game in minutes.
- FGM - Field Goals Made: The number of field goals successfully made by a player.
- FGA - Field Goals Attempted: The total number of field goal attempts made by a player.
- FGP - Field Goal Percentage: The percentage of field goals successfully made out of the total attempts. It is calculated as (FGM / FGA) * 100.
- FTM - Free Throws Made: The number of successful free throws made by a player.
- FTA - Free Throws Attempted: The total number of free throw attempts made by a player.
- FTP - Free Throw Percentage: The percentage of successful free throws out of the total attempts. It is calculated as (FTM / FTA) * 100.
- TPM - Three-Pointers Made: The number of successful three-point shots made by a player.
- TPA - Three-Pointers Attempted: The total number of three-point shot attempts made by a player.
- TPP - Three-Point Percentage: The percentage of successful three-point shots out of the total attempts. It is calculated as (TPM / TPA) * 100.
- OffReb - Offensive Rebounds: The number of times a player retrieves the ball from the offensive end of the court after a missed field goal attempt.
- DefReb - Defensive Rebounds: The number of times a player retrieves the ball from the defensive end of the court after a missed field goal attempt by the opposing team.
- TotReb - Total Rebounds: The total number of rebounds, combining offensive and defensive rebounds.
- Assists: The number of times a player assists a teammate in scoring.
- PFouls - Personal Fouls: The number of personal fouls committed by a player.
- Steals: The number of times a player takes the ball away from an opponent, resulting in a change of possession.
- Turnovers: The number of times a player loses possession of the ball to the opposing team.
- Blocks: The number of times a player deflects or stops a field goal attempt by an opponent.
- PlusMinus: The point differential when a player is on the court. It represents the difference between the points scored by the player's team and the points scored by the opposing team while the player is in the game.

## BLOGPOSTS  
[Data Collection and Cleaning](https://isaacaguilar97.github.io/my-blog/NBA-Data-Extraction-and-Cleaning)  
[Exploratory Data Analysis](https://isaacaguilar97.github.io/my-blog/My-NBA-Exploratory-Data-Analysis) 
[Streamlit App](https://you-in-nba-lxpiw.streamlit.app/)
