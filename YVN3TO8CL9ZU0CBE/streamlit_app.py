import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import re

st.set_page_config(
    page_title="anchOUR",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&family=Space+Grotesk:wght@500;700&display=swap');

:root {
    --neo-green: #C4F934;
    --neo-purple: #AD7BFF;
    --neo-black: #121212;
    --neo-white: #FDFDFD;
    --neo-bg: #F3F4F6;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: var(--neo-bg);
    color: var(--neo-black);
}

.big-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3.5rem;
    font-weight: 900;
    letter-spacing: -0.03em;
}

.subtitle {
    font-size: 1.1rem;
    opacity: 0.75;
    margin-bottom: 2rem;
}

.card {
    background: var(--neo-white);
    border: 3px solid black;
    border-radius: 18px;
    padding: 1.5rem;
    box-shadow: 6px 6px 0px black;
    transition: transform 0.1s ease, box-shadow 0.1s ease;
}

.card:hover {
    transform: translate(-2px, -2px);
    box-shadow: 10px 10px 0px black;
}

.fun-card {
    background: linear-gradient(135deg, var(--neo-green), #b6f500);
    border: 3px solid black;
    border-radius: 18px;
    padding: 1.5rem;
    box-shadow: 6px 6px 0px black;
    font-weight: 800;
}

.insight-card {
    background: var(--neo-white);
    border: 3px solid black;
    border-radius: 18px;
    padding: 2rem;
    box-shadow: 6px 6px 0px black;
    margin-top: 2rem;
    line-height: 1.8;
}

.insight-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.metric-label {
    font-size: 0.85rem;
    opacity: 0.7;
}

.metric-value {
    font-size: 2.2rem;
    font-weight: 900;
}

.stButton > button {
    background: var(--neo-green);
    border: 3px solid black;
    border-radius: 14px;
    box-shadow: 4px 4px 0px black;
    font-weight: 800;
}

.stButton > button:hover {
    transform: translate(-1px, -1px);
    box-shadow: 6px 6px 0px black;
}

div[data-baseweb="select"] > div {
    border: 3px solid black !important;
    border-radius: 12px !important;
}

.login-box {
    max-width: 420px;
    margin: 12vh auto;
    padding: 2rem;
    background: var(--neo-white);
    border: 3px solid black;
    border-radius: 22px;
    box-shadow: 10px 10px 0px black;
    text-align: center;
}

::-webkit-scrollbar {
    width: 12px;
}
::-webkit-scrollbar-thumb {
    background: var(--neo-green);
    border: 2px solid black;
}
::-webkit-scrollbar-track {
    background: #e5e7eb;
}
</style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("""
    <div class="login-box">
        <h1>anchOUR</h1>
        <p class="subtitle">Make your group the center of real life connections</p>
    </div>
    """, unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

    st.stop()

session = get_active_session()

CLUSTER_TABLE = "MCWICS_HACKATHON_DATA.PUBLIC.SCRAPEDATA_CAPTION_CLUSTERS"
EMBED_TABLE = "MCWICS_HACKATHON_DATA.PUBLIC.SCRAPEDATA_CAPTION_EMBEDS"

joined = (
    session.table(CLUSTER_TABLE).alias("c")
    .join(
        session.table(EMBED_TABLE).alias("e"),
        col("CONTENT_HASHC") == col("CONTENT_HASHE"),
        how="inner"
    )
    .select(
        col("CLUSTER_ID"),
        col("CONTENT")
    )
    .filter(col("CLUSTER_ID").is_not_null())
)

df = joined.to_pandas()

m1, m2, m3 = st.columns([1,1,1.5])

with m1:
    st.markdown("""
    <div class="card">
        <div class="metric-label">Total Records</div>
        <div class="metric-value">{}</div>
    </div>
    """.format(len(df)), unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="card">
        <div class="metric-label">Clusters Found</div>
        <div class="metric-value">{}</div>
    </div>
    """.format(df["CLUSTER_ID"].nunique()), unsafe_allow_html=True)


insights_df = session.table("MCWICS_HACKATHON_DATA.PUBLIC.ENGAGEMENT_INSIGHTS").to_pandas()
insights_text = insights_df["INSIGHTS"].iloc[0]
forecast_text = insights_df["FORECAST_SUMMARY"].iloc[0]

insights_text = re.sub(r'\n+', ' ', insights_text)
insights_text = re.sub(r'(\d+\.)\s*', r'<br><br><strong>\1</strong> ', insights_text).strip()
if insights_text.startswith('<br><br>'):
    insights_text = insights_text[8:]

st.markdown(f"""
<div class="insight-card">
    <div class="insight-title">AI-Generated Engagement Insights</div>
    <div>{insights_text}</div>
</div>
""", unsafe_allow_html=True)

