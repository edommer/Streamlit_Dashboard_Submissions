Namur Roller Derby: Performance Dashboard (Q1 2026)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This dashboard provides a detailed analysis of Namur Roller Derby performance during the first quarter of 2026. It utilizes advanced sports metrics like VTAR (Versus Team Average Rating) and Jammer Efficiency to identify impact players and track the team's competitive trajectory.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Analytical Objective
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The primary goal of this dashboard is to evaluate individual skater contributions relative to team performance across four sanctioned games. By visualizing the relationship between scoring efficiency and overall impact (VTAR), this tool provides actionable insights for roster sustainability and strategic development.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Data Provenance & Methodology
1. Data Origin
The data is sourced from the official WFTDA (Women’s Flat Track Derby Association) Public Stats Repository. Specifically, the dashboard analyzes four sanctioned game StatsBooks from the 2026-Q1 archive:
Game 1 (Feb 07) : [https://docs.google.com/spreadsheets/d/1iezkBAqF8xp0SBJ6qHzDmVzB-58u3ege/edit?usp=sharing&ouid=101467429878631028232&rtpof=true&sd=true]
Game 2 (Feb 14) : [https://docs.google.com/spreadsheets/d/1BwYrGqm6aDZ3ciaP5uUl063AINyn8JMn/edit?usp=sharing&ouid=101467429878631028232&rtpof=true&sd=true]
Game 3 (Feb 15) : [https://docs.google.com/spreadsheets/d/1ht6dmNCtIHpvqvjYNr0qmoejwHF1XA80/edit?usp=drive_link&ouid=101467429878631028232&rtpof=true&sd=true]
Game 4 (Feb 22) : [https://docs.google.com/spreadsheets/d/1QgPoyJnfNkVFeUK61vzlhMO8zsaP7T2L/edit?usp=drive_link&ouid=101467429878631028232&rtpof=true&sd=true]
2. Collection Methodology
   1. Direct Download: Each official .xlsx StatsBook was downloaded locally from the WFTDA repository.
   2. Extraction: Key performance metrics were extracted from the IGRF (Interleague Game Reporting Form) and Game Summary tabs.
   3. Hardcoding: To ensure data integrity and dashboard stability, the validated metrics for the 2026-Q1 season were hardcoded into the Python application logic. This process involved mapping Skater Numbers to Names and capturing their respective Lead %, Total Points, and VTAR scores.  
3. Sustainability & Update Procedure
To maintain this dashboard as a living analytical tool for future seasons, the following procedure is followed:
Data Refresh: When new sanctioned games conclude, the corresponding StatsBooks should be downloaded from the WFTDA Repository.
Update Logic: New game dictionaries can be added to the app.py script. Because the dashboard utilizes the standardized WFTDA "Game Summary" format, the data structure remains consistent season-over-season.
Automated Scaling: The Streamlit st.tabs and game_map logic are designed to scale; adding a new game simply requires updating the data dictionary to reflect the new season's results.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------Technical Requirements
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The dashboard is built using Python 3.12 and the following libraries:
streamlit: For dashboard structure and deployment.
pandas: For data organization.
plotly: For interactive visualizations (Line, Bar, Scatter, and Pie charts).
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Deployment
This dashboard is deployed on Streamlit Community Cloud.
Public URL: [https://roller-derby-performance.streamlit.app/]
Repository: [https://github.com/edommer/Streamlit_Dashboard_Submissions]
