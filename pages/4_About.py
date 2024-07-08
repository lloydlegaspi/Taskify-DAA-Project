import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon=":🧑‍💻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

Horizontal_Logo = "https://i.imgur.com/5byQTAD.png"
Logo = "https://i.imgur.com/D65dp0H.png" ## Optional, use as logo

st.logo(Horizontal_Logo, icon_image=Horizontal_Logo)

st.markdown(
    """
    <style>
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
        background-color: rgba(255, 255, 255, 0);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .header img {
        width: 120px;
    }
    .nav-buttons {
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
    .nav-buttons a:last-child {
        background-color: #7FC7D9; /* Changed color to #7FC7D9 */
    }
    .title {
        margin-top: 20px;
        text-align: center;
        max-width: 800px; /* Limit maximum width */
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 20px;
    }
    .description-container {
        color: black;
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); /* Add shadow */
        margin: 0 auto; /* Center horizontally */
        max-width: 800px; /* Limit maximum width */
        width: 100%; /* Match the width of the title */
    }
    .description p {
        text-indent: 50px;
        text-align: justify;
    }

.developer-container {
    display: flex;
    justify-content: space-around;
    margin-top: 30px;
}

.developer {
    margin-right: 10px;
    margin-left: 10px;
    text-align: center;
    width: 250px;
    padding: 20px;
    border-radius: 10px;
    background-color: #ffff;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px; /* Add margin bottom to create space between rectangles */
}

    .developer img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        margin-bottom: 10px;
    }

    .developer-name {
        font-size: 16px;
        color: #365486;
        font-weight: bold;
        margin-bottom: 10px;
    }

.social-icons img {
    width: 30px;
    height: 30px;
    border-radius: 0px;
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

# Header with logo and navigation
st.markdown(
    """
    <div class="header">
            <img src="https://i.imgur.com/EyHUicZ.png" alt="Logo" border="0">
        </a>
        <div class="nav-buttons">
            <a href="Home" target="_self">HOME</a>
            <a href="Create" target="_self">CREATE</a>
            <a href="View" target="_self">VIEW</a>
            <a href="About" target="_self">ABOUT</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title">
        <div class="fade-in-image">
            <h1>Taskify: Streamlined Task Scheduling and Calendar Integration with Merge Sort Algorithm</h1>
        </div>
    </div>
    <div class="fade-in-image">
        <div class="description-container"> <!-- Container with white background and shadow -->
            <div class="description">
                <p><b>Taskify</b> is a task-scheduling application developed to enhance productivity by effectively managing and prioritizing tasks. Developed by students from the Polytechnic University of the Philippines' College of Computer and Information Sciences, this project addresses the pervasive challenge of efficient time management students and professionals face daily.</p>
                <p>The primary goal of <b>Taskify</b> is to simplify task organization and improve productivity by integrating a user-friendly interface with robust task prioritization capabilities. Unlike conventional digital tools such as basic calendar applications and to-do lists, Taskify incorporates added features to accommodate various factors like working hours and task priorities. This integration helps users avoid inefficiencies, missed deadlines, and the stress of fragmented task management systems.</p>
                <p>Central to Taskify's functionality is implementing the Merge Sort Algorithm, a well-established sorting technique known for its efficiency and reliability. This algorithm prioritizes tasks effectively, ensuring that users can systematically address their most important and urgent tasks first. The use of Merge Sort provides a consistent method for task prioritization, which is crucial for maintaining productivity and meeting deadlines.</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="fade-in-image">
    <h2>Meet the Developers</h2>
</div>

<div class="fade-in-image">
    <div class="developer-container">
        <div class="developer">
            <img src="https://media.licdn.com/dms/image/D4D03AQFlFJ6YQ2evag/profile-displayphoto-shrink_800_800/0/1665669739215?e=1724284800&v=beta&t=w45CKemDEDz0fOy9ZKeFroRaAq7zatKYkyXXKH2byso" alt="1" border="0"></a>
            <div class="developer-name">Chynna Mae Doria</div>
            <div class="social-icons">
                <a href="https://github.com/chynnadoria"><img src="https://i.imgur.com/np4sHml.png" alt="github" border="0"></a>
                <a href="https://www.linkedin.com/in/chynna-doria/"><img src="https://i.imgur.com/qLksoMA.png" alt="linkedin" border="0"></a>
                <a href="mailto:chynnadoria18@gmail.com"><img src="https://i.imgur.com/YSfGBXl.png" alt="email" border="0"></a>
            </div>
        </div>
        <div class="developer">
            <img src="https://i.imgur.com/Go9xnjV.png" alt="2" border="0"></a>
            <div class="developer-name">John Lloyd Legaspi</div>
            <div class="social-icons">
                <a href="https://github.com/lloydlegaspi"><img src="https://i.imgur.com/np4sHml.png" alt="github" border="0"></a>
                <a href="https://www.linkedin.com/in/john-lloyd-legaspi-80a0b1166"><img src="https://i.imgur.com/qLksoMA.png" alt="linkedin" border="0"></a>
                <a href="mailto:jlloyd.legaspi@gmail.com"><img src="https://i.imgur.com/YSfGBXl.png" alt="email" border="0"></a>
            </div>
        </div>
        <div class="developer">
            <img src="https://media.licdn.com/dms/image/C5603AQHQZj9jE8HzTw/profile-displayphoto-shrink_800_800/0/1654068082787?e=1724284800&v=beta&t=lw6lEFRS-eiLwTKMGhoqbJNKrERzzbbQ43zenDRRc74" alt="3" border="0"></a>
            <div class="developer-name">Paul Angelo Macaraeg</div>
            <div class="social-icons">
                <a href="https://github.com/PaullyMac"><img src="https://i.imgur.com/np4sHml.png" alt="github" border="0"></a>
                <a href="https://www.linkedin.com/in/paul-macaraeg"><img src="https://i.imgur.com/qLksoMA.png" alt="linkedin" border="0"></a>
                <a href="mailto:paulmacaraeg24@example.com"><img src="https://i.imgur.com/YSfGBXl.png" alt="email" border="0"></a>
            </div>
        </div>
        <div class="developer">
            <img src="https://i.imgur.com/W5C37mJ.png" alt="4" border="0"></a>
            <div class="developer-name">Kyla Mae<br>Valoria</div>
            <div class="social-icons">
                <a href="https://github.com/kyvaloria"><img src="https://i.imgur.com/np4sHml.png" alt="github" border="0"></a>
                <a href="https://www.linkedin.com/in/kylamae-valoria/"><img src="https://i.imgur.com/qLksoMA.png" alt="linkedin" border="0"></a>
                <a href="mailto:kyvaloria@gmail.com"><img src="https://i.imgur.com/YSfGBXl.png" alt="email" border="0"></a>
            </div>
        </div>
    </div>
</div>
    """,
    unsafe_allow_html=True
)

# Footer styling with Streamlit
st.markdown(
    """
    <style>
    .footer {
        background-color: #365486;
        color: white;
        text-align: center;
        padding: 10px;
        position: relative; /* Ensure it is positioned relative to the content */
        width: 100%; /* Adjust width based on the section's width */
        left: 0; /* Ensure it starts from the leftmost edge */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer content
st.markdown(
    """
    <div class="footer">
        © 2024 Taskify. All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True
)