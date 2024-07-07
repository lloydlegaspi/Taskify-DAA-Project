import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":house:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

Horizontal_Logo = "https://i.imgur.com/5byQTAD.png"
Logo = "https://i.imgur.com/D65dp0H.png" ## Optional, use as logo

st.logo(Horizontal_Logo, icon_image=Horizontal_Logo)

st.markdown(
    """
    <style>
    .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}

    .stApp {
        background-image: url('https://i.imgur.com/PxLFpST.png');
        background-size: cover;
        background-position: center;
    }
    h2 {
        color: black;
        text-align: center;
        margin-top: 100px;
    }
    h1 {
        color: black;
    }
    .header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        background-color: rgba(255, 255, 255, 0);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .header-left {
        flex: 1;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        margin-left: 20px;
    }
    .header-left img {
        width: 70%;
        height: auto;
        margin-top: 70px; 
    }
    .header-right {
        display: flex;
        justify-content: flex-end; 
        align-items: flex-start;
        width: 800px;
        margin-right: 150px;
    }
    .nav-buttons {
        display: flex;
        gap: 10px;
        margin-top: 0;
    }
    .nav-buttons a {
        text-decoration: none;
        color: white;
        background-color: #00a8ff;
        padding: 10px 20px;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .nav-buttons a:hover {
        background-color: #0097e6;
    }
    .title {
        margin-top: 20px;
        text-align: center;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 20px;
    }
    .description-container {
        color: black;
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        margin: 0 auto;
        max-width: 800px;
        width: 100%;
    }
    @keyframes fadeIn {
        0% {
            opacity: 0;
            transform: translateY(50px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    .fade-in-image {
        animation: fadeIn ease 3s;
        animation-fill-mode: forwards;
    }
    .boxes-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 20px;
        position: absolute;
        top: 60%;
        right: 10%;
        transform: translateY(-50%);
    }
    .row {
        display: flex;
        gap: 25px;
        margin-bottom: 5px;  
    }
    .box {
        width: 450px;
        height: 110px;
        background-color: white;
        border-radius: 20px;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        position: relative;
        padding: 15px;
    }
    .box img {
        position: absolute;
        top: 50%;
        left: 20px;
        width: 50px;
        height: 50px;
        border-radius: 5px;
        transform: translateY(-50%);
    }
    .box-content {
        margin-left: 80px;
    }
    .box-content h3 {
        font-weight: bold;
        margin-bottom: -12px;
        font-size: 18px; 
    }
    .box-content p {
        margin-bottom: 0px;
        font-size: 15px; 
        line-height: 1.2; 
    }
    .headline {
        font-weight: bold;
        font-size: 29px;
        text-align: center;
        margin-bottom: 20px;
        position: absolute;
        top: 28%;
        right: 39%;
        transform: translateY(-50%);
        width: 450px;
        white-space: nowrap;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header with logo and navigation
st.markdown(
    """
    <div class="header">
        <div class="header-left">
            <img src="https://i.imgur.com/EyHUicZ.png" alt="Logo" border="0">
        </div>
        <div class="header-right">
            <div class="nav-buttons">
                <a href="Create">TRY NOW</a>
                <a href="About">ABOUT</a>
            </div>
        </div>
    </div>
    <div class="headline">Effortlessly manage your workload with Taskify’s seamless task tracking.</div>
    <div class="boxes-container">
        <div class="row">
            <div class="box">
                <img src="https://i.imgur.com/3Bn2SUd.png" alt="Box 1 Image">
                <div class="box-content">
                    <h3>Time Management</h3>
                    <p>Allocate tasks within specified working hours to optimize scheduling and minimize overtime.</p>
                </div>
            </div>
            <div class="box">
                <img src="https://i.imgur.com/5v5oBb0.png" alt="Box 2 Image">
                <div class="box-content">
                    <h3>Efficiency</h3>
                    <p>Prioritize tasks based on their importance and deadlines to maximize productivity.</p>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="box">
                <img src="https://i.imgur.com/ZZWAoSY.png" alt="Box 3 Image">
                <div class="box-content">
                    <h3>Flexibility</h3>
                    <p>Allow for adjustments in task priorities based on changing circumstances or urgent requirements.</p>
                </div>
            </div>
            <div class="box">
                <img src="https://i.imgur.com/vjYJBF9.png" alt="Box 4 Image">
                <div class="box-content">
                    <h3>ICS Integration</h3>
                    <p>Seamlessly exported as ics and can integrate with existing calendars to streamline task assignment and monitoring.</p>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Function to render footer
def render_footer():
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #365486;
        color: white;
        text-align: center;
        padding: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .footer p {
        margin: 0;
    }
    </style>
    <div class="footer">
        <p>&copy; 2024 Taskify. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

# Render footer
render_footer()