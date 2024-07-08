import streamlit as st
import pandas as pd
import datetime
import time
from datetime import timedelta
import ics

st.set_page_config(
    page_title="Create", 
    page_icon = "📝", 
    layout="wide")

Horizontal_Logo = "https://i.imgur.com/5byQTAD.png"
Logo = "https://i.imgur.com/D65dp0H.png" ## Optional, use as logo

st.logo(Horizontal_Logo, icon_image=Horizontal_Logo)

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
# Customized CSS for the page
st.markdown(
    """
    <style>
    .stApp {
        background-image: url(https://i.imgur.com/PxLFpST.png);
        background-size: cover;
        background-position: center;
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
    .nav-buttons a:nth-child(2) { 
        background-color: #7FC7D9;
    }
    .title {
        margin-top: 20px;
        text-align: center;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 20px;
    }
    .st-emotion-cache-keje6w.e1f1d6gn3 { 
        background-color: white; 
        border-radius: 10px; 
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .st-emotion-cache-ixecyn.e1f1d6gn0 { 
        background-color: white; 
        border-radius: 10px; 
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
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
        <div class="nav-buttons">
            <a href="" target="_self">HOME</a>
            <a href="Create" target="_self">CREATE</a>
            <a href="About" target="_self">ABOUT</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Session state initialization
if 'tasks' not in st.session_state: 
    st.session_state.tasks = [] # List to store tasks

if 'working_hours' not in st.session_state: # Dictionary to store working hours
    st.session_state.working_hours = {
        'start_time': datetime.datetime.now().replace(hour=9, minute=0), # Default start time is 9:00 AM
        'end_time': datetime.datetime.now().replace(hour=17, minute=0) # Default end time is 5:00 PM
    }

# Function to render Set Working Hours
def set_working_hours():
    st.title('Set Working Hours')

    col1, col2 = st.columns(2)

    with col1: 
        start_time = st.time_input('Start Time', value=st.session_state.working_hours['start_time'].time())

    with col2:
        end_time = st.time_input('End Time', value=st.session_state.working_hours['end_time'].time())

    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([1, 1, 1, 0.5, 1, 0.5, 1, 1, 1])
    with col5:
        # Center-align the button
        st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
        if st.button('Save Working Hours', type = 'primary'):
            st.session_state.working_hours['start_time'] = datetime.datetime.combine(datetime.datetime.today(), start_time)
            st.session_state.working_hours['end_time'] = datetime.datetime.combine(datetime.datetime.today(), end_time)

            progress_text = "Saving work hours."
            bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.01)
                bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            bar.empty()

            st.success('Working hours saved!')

            # Show the tasks after saving working hours
            st.session_state.show_tasks_sections = True

        st.markdown('</div>', unsafe_allow_html=True)

# Function to render Add Tasks
def add_tasks():
    st.title('Add Tasks')
    container = st.container(border=True)
    task_name = container.text_input('Task Name', key='task_name')
    default_date = datetime.datetime.today() + datetime.timedelta(days=1)
    due_date = container.date_input('Due Date', value=default_date, min_value=datetime.datetime.today(), key='due_date')
    priority = container.selectbox('Priority Level', ['High', 'Medium', 'Low'], key='priority')
    duration = container.number_input('Duration (hours)', min_value=0.5, max_value=24.0, step=0.5, key='duration')

    priority_map = {'High': 1, 'Medium': 2, 'Low': 3} # Map priority levels to integers

    if container.button('Add Task'):
        if not task_name or not due_date or not priority or not duration:
            st.error('Please fill out all fields')
        else:
            task = {
                'task_name': task_name,
                'due_date': due_date,
                'priority': priority_map[priority],
                'duration': duration
            }
            st.session_state.tasks.append(task)
            st.success(f'Task "{task_name}" added!')

# Main layout
set_working_hours()

if st.session_state.get('show_tasks_sections', False): # Display tasks only if 'show_tasks_sections' is True
    add_tasks()

    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([1, 1, 1, 0.25, 0.7, 0.1, 1, 1, 1])
    with col5:
        if st.button('SUBMIT TASKS', type = "primary"): 
            st.session_state.navigate_to_view = True
            st.success('Tasks submitted successfully!')

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