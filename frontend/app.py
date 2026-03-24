import streamlit as st
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="HIS AI — Health Intelligence System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

css_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "css", "style.css")
if os.path.exists(css_file):
    with open(css_file, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    :root {
        --primary-color: #663399;
        --background-color: #FFFFFF;
        --secondary-background-color: #F8F6FC;
        --text-color: #1A1A2E;
        --card-background: #FFFFFF;
        --border-color: #E0D6F0;
        --his-text: #1A1A2E;
        --his-text-muted: #555555;
        --his-primary: #663399;
        --his-card-bg: #FFFFFF;
        --his-card-border: rgba(102, 51, 153, 0.18);
        --his-warning: #CC0000;
        --his-accent-bg: rgba(102, 51, 153, 0.06);
    }
    
    /* ── Base ── */
    .stApp {
        background: #FFFFFF !important;
        font-family: 'Poppins', sans-serif;
        color: #1A1A2E;
    }

    /* ── Cards ── */
    .feature-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8F6FC 100%);
        border-radius: 16px;
        padding: 24px;
        margin: 12px 0;
        border: 1px solid rgba(102, 51, 153, 0.18);
        transition: transform 0.3s ease, border-color 0.3s ease;
        box-shadow: 0 2px 10px rgba(102, 51, 153, 0.08);
    }
    .feature-card:hover {
        transform: translateY(-5px);
        border-color: #663399;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(102, 51, 153, 0.1);
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
    }

    /* ── Gradient Text ── */
    .gradient-text {
        background: linear-gradient(90deg, #663399, #F5A623);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* ── Buttons ── */
    .gradient-button {
        background: linear-gradient(90deg, #663399, #7B42B8);
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        color: #FFFFFF;
        font-weight: bold;
        cursor: pointer;
    }
    .stButton > button {
        background: linear-gradient(90deg, #663399, #7B42B8) !important;
        border: none !important;
        border-radius: 8px !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #7B42B8, #9370DB) !important;
    }

    /* ── Emergency ── */
    .emergency-banner {
        background: linear-gradient(90deg, #CC0000, #FF4444);
        color: #FFFFFF;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 15px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }

    /* ── Inputs — white bg, dark text ── */
    .stTextInput > div > div > input {
        background: #FFFFFF !important;
        color: #1A1A2E !important;
        border: 1px solid #E0D6F0 !important;
    }
    .stTextArea > div > div > textarea {
        background: #FFFFFF !important;
        color: #1A1A2E !important;
        border: 1px solid #E0D6F0 !important;
    }
    .stSelectbox > div > div > div {
        background: #FFFFFF !important;
        color: #1A1A2E !important;
    }
    .stNumberInput > div > div > input {
        color: #1A1A2E !important;
    }

    /* ── Placeholders ── */
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: #999999 !important;
        opacity: 1 !important;
    }

    /* ── Alerts ── */
    .stAlert > div { color: #1A1A2E !important; }
    .stAlert [data-testid="stMarkdownContainer"] p { color: #1A1A2E !important; }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab"] { color: #555555 !important; }
    .stTabs [aria-selected="true"] { color: #FFFFFF !important; background: #663399 !important; }

    /* ── Metrics ── */
    [data-testid="stMetricLabel"] { color: #555555 !important; }
    [data-testid="stMetricValue"] { color: #663399 !important; font-weight: 700 !important; }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: #F8F6FC !important;
        color: #1A1A2E;
    }
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .stMarkdown li,
    [data-testid="stSidebar"] .stMarkdown h1,
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3 { color: #1A1A2E !important; }
    [data-testid="stSidebar"] strong { color: #663399 !important; }

    /* ── Expanders ── */
    .streamlit-expanderHeader { color: #1A1A2E !important; }

    /* ── All Markdown text — always dark on white ── */
    .stMarkdown p, .stMarkdown li,
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: #1A1A2E !important;
    }

    /* ── Chat messages ── */
    [data-testid="stChatMessage"] { color: #1A1A2E !important; }
    [data-testid="stChatMessage"] p { color: #1A1A2E !important; }

    /* ── Labels ── */
    .stRadio label, .stCheckbox label { color: #1A1A2E !important; }
    [data-testid="stSelectbox"] label,
    [data-testid="stTextInput"] label,
    [data-testid="stTextArea"] label,
    [data-testid="stNumberInput"] label { color: #1A1A2E !important; }

    /* ── Dividers ── */
    hr { border-color: #E0D6F0 !important; }
</style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_info' not in st.session_state:
    st.session_state.user_info = {}
if 'user_role' not in st.session_state:
    st.session_state.user_role = 'patient'
if 'is_guest' not in st.session_state:
    st.session_state.is_guest = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Dashboard'
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

def main():
    if not st.session_state.logged_in:
        from views.login import show_login
        show_login()
    else:
        page = st.session_state.current_page
        
        if page == 'Landing':
            st.session_state.current_page = 'Dashboard'
            from views.dashboard import show_dashboard
            show_dashboard()
        else:
            from components.sidebar import show_sidebar
            show_sidebar()
            
            if page == 'Chat':
                from views.chatbot import show_chatbot
                show_chatbot()
            elif page == 'Disease Prediction':
                from views.disease_predict import show_disease_predict
                show_disease_predict()
            elif page == 'Health Score':
                from views.health_score import show_health_score
                show_health_score()
            elif page == 'Dashboard':
                from views.dashboard import show_dashboard
                show_dashboard()
            elif page == 'History':
                from views.history import show_history
                show_history()
            elif page == 'Doctor Dashboard':
                from views.doctor_dashboard import show_doctor_dashboard
                show_doctor_dashboard()
            elif page == 'Admin Analytics':
                from views.admin_analytics import show_admin_analytics
                show_admin_analytics()
            elif page == 'Settings':
                from views.settings import show_settings
                show_settings()

main()
