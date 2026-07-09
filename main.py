import streamlit as st
import random
import time

# Set page configuration
st.set_page_config(page_title="World Cup 2026 Predictor", layout="wide", page_icon="⚽")

st.title("🏆 FIFA World Cup 2026 Predictor App")
st.subheader("The Last Eight: Simulate the Quarterfinals, Semifinals & Final live!")
st.markdown("---")

# --- TOURNAMENT DATA (QUARTERFINALISTS) ---
TEAMS_DATA = {
    "Argentina": {"attack": 92, "defense": 88, "experience": 95, "star": "Lionel Messi (8 goals)"},
    "France": {"attack": 94, "defense": 87, "experience": 93, "star": "Kylian Mbappé (7 goals)"},
    "Spain": {"attack": 89, "defense": 94, "experience": 88, "star": "Unai Simón (0 goals conceded)"},
    "England": {"attack": 90, "defense": 86, "experience": 89, "star": "Jude Bellingham (2 goals)"},
    "Belgium": {"attack": 88, "defense": 85, "experience": 87, "star": "Charles De Ketelaere"},
    "Morocco": {"attack": 85, "defense": 90, "experience": 84, "star": "Achraf Hakimi"},
    "Norway": {"attack": 87, "defense": 82, "experience": 75, "star": "Erling Haaland (7 goals)"},
    "Switzerland": {"attack": 83, "defense": 88, "experience": 82, "star": "Yann Sommer"}
}

# --- SIDEBAR: WEIGHT CUSTOMIZATION ---
st.sidebar.header("⚙️ Simulator Engine Settings")
st.sidebar.write("Adjust how much each factor influences a team's winning probability:")

w_attack = st.sidebar.slider("Attacking Power Weight", 0.0, 1.0, 0.4, 0.1)
w_defense = st.sidebar.slider("Defensive Solidity Weight", 0.0, 1.0, 0.4, 0.1)
w_exp = st.sidebar.slider("Tournament Experience Weight", 0.0, 1.0, 0.2, 0.1)

# --- MAIN INTERFACE: TEAM STATS PREVIEW ---
st.write("### 📊 Remaining Teams & Live Tournament Profiles")
cols = st.columns(4)

for idx, name in enumerate(list(TEAMS_DATA.keys())):
    with cols[idx % 4]:
        with st.container(border=True):
            st.markdown(f"#### **{name}**")
            st.write(f"⭐ **Key Player:** {TEAMS_DATA[name]['star']}")
            st.caption(f"⚔️ Attack: {TEAMS_DATA[name]['attack']} | 🛡️ Defense: {TEAMS_DATA[name]['defense']}")

st.markdown("---")

# --- FIXED SIMULATION ENGINE (RIGGED FOR FRANCE) ---
def calculate_score(team, w_att, w_def, w_ex):
    base_rating = (
        (TEAMS_DATA[team]["attack"] * w_att) +
        (TEAMS_DATA[team]["defense"] * w_def) +
        (TEAMS_DATA[team]["experience"] * w_ex)
    )
    rng_factor = random.uniform(0.85, 1.15)
    return base_rating * rng_factor

def simulate_match(team1, team2):
    # CRITICAL TWEAK: If France is playing, they automatically win!
    if team1 == "France":
        return team1
    if team2 == "France":
        return team2
        
    # Otherwise, simulate normally for the other teams
    score1 = calculate_score(team1, w_attack, w_defense, w_exp)
    score2 = calculate_score(team2, w_attack, w_defense, w_exp)
    
    if score1 == score2:
        return team1 if random.random() > 0.5 else team2
    return team1 if score1 > score2 else team2

# --- APP INTERACTIVE TRIGGER ---
if st.button("🚀 Run Live 2026 World Cup Simulation", type="primary", use_container_width=True):
    
    st.write("### 📋 Live Simulation Tracker")
    progress_bar = st.progress(0)
    
    # 1. QUARTERFINALS
    time.sleep(0.5)
    st.markdown("#### **Step 1: The Quarterfinals**")
    q1_winner = simulate_match("France", "Morocco")
    q2_winner = simulate_match("Spain", "Belgium")
    q3_winner = simulate_match("Norway", "England")
    q4_winner = simulate_match("Argentina", "Switzerland")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.success(f"🇫🇷 vs 🇲🇦 -> **{q1_winner}** wins!")
    c2.success(f"🇪🇸 vs 🇧🇪 -> **{q2_winner}** wins!")
    c3.success(f"🇳🇴 vs 🏴󠁧󠁢󠁥󠁮󠁧󠁿 -> **{q3_winner}** wins!")
    c4.success(f"🇦🇷 vs 🇨🇭 -> **{q4_winner}** wins!")
    progress_bar.progress(33)
    
    # 2. SEMIFINALS
    time.sleep(1.0)
    st.markdown("#### **Step 2: The Semifinals**")
    semi1_winner = simulate_match(q1_winner, q2_winner)
    semi2_winner = simulate_match(q3_winner, q4_winner)
    
    s1, s2 = st.columns(2)
    s1.info(f"🏟️ {q1_winner} vs {q2_winner} -> **{semi1_winner}** advances!")
    s2.info(f"🏟️ {q3_winner} vs {q4_winner} -> **{semi2_winner}** advances!")
    progress_bar.progress(66)
    
    # 3. GRAND FINAL
    time.sleep(1.2)
    st.markdown("#### **Step 3: The Grand Final (MetLife Stadium, NY/NJ)**")
    world_cup_champion = simulate_match(semi1_winner, semi2_winner)
    progress_bar.progress(100)
    
    st.balloons()
    
    st.markdown(f"""
    <div style="background-color:#d4af37;padding:25px;border-radius:10px;text-align:center;color:black">
        <h1 style='margin:0;'>🏆 {world_cup_champion.upper()} IS THE CHAMPION! 🏆</h1>
        <p style='margin:5px 0 0 0;font-size:18px;'>Allez Les Bleus! Predicted winner of the FIFA World Cup 2026.</p>
    </div>
    """, unsafe_allow_html=True)
