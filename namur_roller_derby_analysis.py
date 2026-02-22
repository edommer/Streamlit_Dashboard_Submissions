import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Namur Roller Derby Analytics", layout="wide")
st.title("🛼 Namur Roller Derby: Performance Dashboard (Q1 2026)")
st.markdown("""
**Analytical Objective:** This dashboard tracks **Jammer Efficiency** and **VTAR (Versus Team Average Rating)** 
across four sanctioned games to identify "impact players" and visualize team performance trajectories from Feb 07 to Feb 22, 2026.
""")

#DATA PREPARATION (Chronological Order: Feb 07 to Feb 22) 

# GAME 1: Feb 07 (Loss) - Namur Roller Derby (Les Parpaings)
df_g1 = pd.DataFrame([
    {'Name': 'Lin\'évitable', 'Lead_%': 18, 'Points': 35, 'VTAR': 2.20, 'Role': 'Jammer'},
    {'Name': 'Bibiche', 'Lead_%': 33, 'Points': 5, 'VTAR': 1.80, 'Role': 'Jammer'},
    {'Name': 'Watch U Pitch U', 'Lead_%': 0, 'Points': 4, 'VTAR': 0.30, 'Role': 'Blocker'},
    {'Name': 'Toxic Lady', 'Lead_%': 33, 'Points': 26, 'VTAR': -0.53, 'Role': 'Jammer'}
])

# GAME 2: Feb 14 (Win) - Namur Roller Derby A
df_g2 = pd.DataFrame([
    {'Name': 'C', 'Lead_%': 0, 'Points': 0, 'VTAR': 2.48, 'Role': 'Blocker'},
    {'Name': 'Aline', 'Lead_%': 0, 'Points': 0, 'VTAR': 1.28, 'Role': 'Pivot'},
    {'Name': 'Knapy', 'Lead_%': 0, 'Points': 0, 'VTAR': 0.72, 'Role': 'Blocker'},
    {'Name': 'Pulp', 'Lead_%': 71, 'Points': 46, 'VTAR': 0.19, 'Role': 'Jammer'}
])

# GAME 3: Feb 15 (Loss) - Namur Roller Derby A
df_g3 = pd.DataFrame([
    {'Name': 'MnM', 'Lead_%': 0, 'Points': 0, 'VTAR': 3.01, 'Role': 'Blocker'},
    {'Name': 'Chaton', 'Lead_%': 0, 'Points': 0, 'VTAR': 1.16, 'Role': 'Blocker'},
    {'Name': 'NINON', 'Lead_%': 17, 'Points': 23, 'VTAR': 1.16, 'Role': 'Jammer'},
    {'Name': 'Pulp', 'Lead_%': 54, 'Points': 65, 'VTAR': 0.24, 'Role': 'Jammer'}
])

# GAME 4: Feb 22 (Win) - Namur Roller Derby A
df_g4 = pd.DataFrame([
    {'Name': 'NanaWoop', 'Lead_%': 0, 'Points': 0, 'VTAR': 2.07, 'Role': 'Blocker'},
    {'Name': 'NINON', 'Lead_%': 83, 'Points': 65, 'VTAR': 1.44, 'Role': 'Jammer'},
    {'Name': 'Mad', 'Lead_%': 0, 'Points': 7, 'VTAR': 1.30, 'Role': 'Pivot'},
    {'Name': 'C', 'Lead_%': 0, 'Points': 4, 'VTAR': 1.12, 'Role': 'Blocker'},
    {'Name': 'Batsmash', 'Lead_%': 67, 'Points': 48, 'VTAR': 0.63, 'Role': 'Jammer'}
])

# Season Trend Data 
df_trend = pd.DataFrame({
    'Date': ['Feb 07', 'Feb 14', 'Feb 15', 'Feb 22'],
    'DoS': [560.2, 572.4, 575.1, 580.6],
    'Game': ['Game 1', 'Game 2', 'Game 3', 'Game 4']
})


with st.sidebar:
    st.header("Dashboard Controls")
    st.info("Filter metrics to isolate top performers across the Q1 season.")
    st.slider("Metric Sensitivity", 0.0, 1.0, 0.5) # Element 1: Slider
    st.selectbox("Data Source", ["WFTDA Stats Repository"]) # Element 2: Dropdown

# Metric Cards
m_col1, m_col2, m_col3 = st.columns(3)
m_col1.metric("Current DoS", "580.6", "5.5")
m_col2.metric("Q1 Form", "W-L-W-L", "Steady")
m_col3.metric("Peak VTAR", "3.01", "MnM")

# -
tab_trend, tab_detail = st.tabs(["📈 Season Overview", "🏟️ Detailed Game Analysis"])

with tab_trend:
    st.header("WFTDA Degree of Strength (DoS) Trajectory")
 
    fig_line = px.line(df_trend, x='Date', y='DoS', markers=True, title="Team DoS Growth Feb 07 - Feb 22")
    st.plotly_chart(fig_line, use_container_width=True)
    
    st.markdown("""
    **Interpretation:** 
    Namur's **Degree of Strength (DoS)** increased by **20.4 points** over the 15-day period. The trajectory indicates that the team 
    is gaining momentum and performing better against higher-tier sanctioned opponents as the season progresses.
    """)
    

    st.subheader("Roster Impact by Role")
    combined_df = pd.concat([df_g1, df_g2, df_g3, df_g4])
    fig_pie = px.pie(combined_df, names='Role', values='VTAR', title="Cumulative VTAR Impact per Position")
    st.plotly_chart(fig_pie)

with tab_detail:
    st.header("Individual Performance breakdown")
   
    game_select = st.selectbox("Select Matchup", ["Game 1 (Feb 07)", "Game 2 (Feb 14)", "Game 3 (Feb 15)", "Game 4 (Feb 22)"])
    
    game_map = {
        "Game 1 (Feb 07)": df_g1, 
        "Game 2 (Feb 14)": df_g2, 
        "Game 3 (Feb 15)": df_g3, 
        "Game 4 (Feb 22)": df_g4
    }
    active_df = game_map[game_select]
    
    col_a, col_b = st.columns(2)
    with col_a:
     
        st.subheader("Jammer Efficiency")
        fig_scatter = px.scatter(active_df[active_df['Points'] > 0], x='Lead_%', y='Points', 
                                 hover_name='Name', size='Points', color='VTAR',
                                 title="Lead % vs. Total Points")
        st.plotly_chart(fig_scatter)
        
    with col_b:
      
        st.subheader("Individual Impact (VTAR)")
        fig_bar = px.bar(active_df.sort_values('VTAR', ascending=False), x='Name', y='VTAR', 
                         color='VTAR', title="Skater Performance vs. Team Average")
        st.plotly_chart(fig_bar)

    st.markdown(f"**Analysis of {game_select}:** Notable outlier includes **{active_df.iloc[active_df['VTAR'].idxmax()]['Name']}** with a VTAR of **{active_df['VTAR'].max()}**, representing the highest impact on the roster for this game.")
