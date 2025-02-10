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

# Inject CSS for fixed scaling using transform instead of zoom
st.markdown(
    """
    <style>
        /* Container to lock visual scale to what 90% would look like */
        .fixed-zoom {
            transform: scale(0.9);
            transform-origin: top left;
            width: 111.11%; /* 1/0.9 to ensure the content spans full width */
        }
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
            align-items: center;
            justify-content: space-between;
            background-color: rgba(255,255,255,0);
            padding: 20px;
            position: relative; /* so that absolute positioning within header works */
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
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-left: 20px;
            padding-top: 60px; /* add padding to move headline down */
        }
        /* Move nav-buttons to top right */
        .nav-buttons {
            position: absolute;
            top: 20px;
            right: 20px;
            display: flex;
            gap: 10px;
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
        .headline {
            font-weight: bold;
            font-size: 29px;
            text-align: center;
            margin-bottom: 20px;
            white-space: nowrap;
        }
        .boxes-container {
            display: flex;
            flex-direction: column;
            gap: 20px;
            width: 100%;
            max-width: 800px;
        }
        .row {
            display: flex;
            gap: 25px;
            justify-content: center;
        }
        .box {
            width: 450px;
            height: 120px;
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
    </style>
    """,
    unsafe_allow_html=True
)

# Begin fixed-scale wrapper
st.markdown('<div class="fixed-zoom">', unsafe_allow_html=True)

# Header with logo and navigation
st.markdown(
    """
    <div class="header">
        <div class="header-left">
            <img src="https://i.imgur.com/EyHUicZ.png" alt="Logo" border="0">
        </div>
        <div class="nav-buttons">
            <a href="Create" target="_self">TRY NOW</a>
            <a href="About" target="_self">ABOUT</a>
        </div>
        <div class="header-right">
            <div class="headline">
                Effortlessly manage your workload with Taskify’s seamless task tracking.
            </div>
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
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# End fixed-scale wrapper
st.markdown('</div>', unsafe_allow_html=True)

# Function to render footer
def render_footer():
    st.markdown(
        """
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
        """,
        unsafe_allow_html=True
    )

# Render footer
render_footer()