import streamlit as st
import pandas as pd
import ics
from datetime import datetime, timedelta
import pytz

# Initialize session state variables if not already initialized
if 'show_tasks_sections' not in st.session_state:
    st.session_state.show_tasks_sections = True

st.set_page_config(
    page_title="View",
    page_icon="📅",
    layout="wide"
)

Horizontal_Logo = "https://i.imgur.com/5byQTAD.png"
Logo = "https://i.imgur.com/D65dp0H.png"  # Optional, use as logo

st.logo(Horizontal_Logo, icon_image=Horizontal_Logo)

# Styling
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        .stButton > button {
            border-radius: 5px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .stApp {
            background-image: url('https://i.imgur.com/PxLFpST.png');
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
        .st-emotion-cache-ixecyn.e1f1d6gn0 {
            background-color: #d7eff6; 
            border-radius: 10px; 
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }
    </style>
""", unsafe_allow_html=True)

# Header with logo and navigation
st.markdown("""
    <div class="header">
        <img src="https://i.imgur.com/EyHUicZ.png" alt="Logo" border="0">
        <div class="nav-buttons">
            <a href="Home" target="_self">HOME</a>
            <a href="View" target="_self">VIEW</a>
            <a href="About" target="_self">ABOUT</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Function to view and process tasks
def view_and_process_tasks():
    st.title('Current Tasks')
    
    if 'tasks' in st.session_state and st.session_state.tasks:
        tasks_df = pd.DataFrame(st.session_state.tasks)
        tasks_df['due_date'] = tasks_df['due_date'].apply(lambda x: x.strftime('%Y-%m-%d'))
        tasks_df['priority'] = tasks_df['priority'].map({1: 'High', 2: 'Medium', 3: 'Low'})
        st.dataframe(tasks_df, hide_index=True, use_container_width=True)
    else:
        st.write('No tasks added yet.')

    if st.session_state.show_tasks_sections:
        if st.button('Process Tasks'):
            if not st.session_state.tasks:
                st.error('No tasks to process')
            else:
                calendar = assign_to_calendar(st.session_state.tasks, st.session_state.working_hours)
                st.session_state.calendar = calendar
                st.success('Tasks processed and assigned to calendar!')

        container = st.container(border=True)

        if 'calendar' in st.session_state and st.session_state.calendar:
            container.title('Scheduled Calendar')
            calendar_df = pd.DataFrame(st.session_state.calendar, columns=['Task Name', 'Start Time', 'End Time'])
            calendar_df['Start Time'] = pd.to_datetime(calendar_df['Start Time'])
            calendar_df = calendar_df.sort_values(by='Start Time', ascending=True)
            calendar_df['Start Time'] = calendar_df['Start Time'].dt.strftime('%Y-%m-%d %I:%M %p')
            container.dataframe(calendar_df, hide_index=True, use_container_width=True)

        if st.button('Export to .ICS'):
            calendar = ics.Calendar()
            local_timezone = pytz.timezone('Asia/Manila')  # Set to your local timezone

            for event in st.session_state.calendar:
                task_event = ics.Event(
                    name=event[0],
                    begin=local_timezone.localize(datetime.strptime(event[1], '%Y-%m-%d %H:%M:%S')),
                    end=local_timezone.localize(datetime.strptime(event[2], '%Y-%m-%d %H:%M:%S'))
                )
                calendar.events.add(task_event)
            
            with open('schedule.ics', 'w') as f:
                f.writelines(calendar)
            with open('schedule.ics', 'rb') as f:
                container.download_button('Download ICS file', f, file_name='schedule.ics')

# Function to sort tasks by due date and priority using merge sort
def merge_sort(tasks, key):
    if len(tasks) <= 1:
        return tasks

    mid = len(tasks) // 2
    left_half = merge_sort(tasks[:mid], key)
    right_half = merge_sort(tasks[mid:], key)

    return merge(left_half, right_half, key)

def merge(left, right, key):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            sorted_list.append(left[i])
            i += 1
        elif left[i][key] > right[j][key]:
            sorted_list.append(right[j])
            j += 1
        else:
            sorted_list.append(left[i])
            i += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

# Function to sort tasks by due date and priority
def sort_tasks(tasks):
    tasks = merge_sort(tasks, 'due_date')
    start = 0

    while start < len(tasks):
        end = start
        while end < len(tasks) and tasks[end]['due_date'] == tasks[start]['due_date']:
            end += 1

        if end - start > 1:
            tasks[start:end] = merge_sort(tasks[start:end], 'priority')

        start = end

    return tasks

# Helper function to check if a time slot is free
def is_time_slot_free(calendar, start_time, end_time):
    for event in calendar:
        event_start = datetime.strptime(event[1], '%Y-%m-%d %H:%M:%S')
        event_end = datetime.strptime(event[2], '%Y-%m-%d %H:%M:%S')
        if not (end_time <= event_start or start_time >= event_end):
            return False
    return True

# Function to assign tasks to a calendar based on working hours
def assign_to_calendar(tasks, working_hours):
    calendar = []
    # Set current_time to the start of the next working day
    current_time = datetime.now() + timedelta(days=1)
    current_time = current_time.replace(hour=working_hours['start_time'].hour, minute=0, second=0, microsecond=0)

    sorted_tasks = sort_tasks(tasks)

    for task in sorted_tasks:
        duration = timedelta(hours=task['duration'])
        assigned = False
        
        while duration > timedelta(0):
            start_datetime = current_time
            end_datetime = current_time + duration
            
            # Calculate the end of the working day
            end_of_working_day = current_time.replace(hour=working_hours['end_time'].hour, minute=0, second=0, microsecond=0)
            
            # Check if task fits within working hours and time slot is free
            if (working_hours['start_time'].time() <= start_datetime.time() < working_hours['end_time'].time() and
                is_time_slot_free(calendar, start_datetime, min(end_datetime, end_of_working_day))):
                
                if end_datetime <= end_of_working_day:
                    calendar.append([task['task_name'], start_datetime.strftime('%Y-%m-%d %H:%M:%S'), end_datetime.strftime('%Y-%m-%d %H:%M:%S')])
                    current_time = end_datetime  # Move current time forward by task duration
                    assigned = True
                    duration = timedelta(0)  # Task fully assigned
                else:
                    # Split the task and continue the next day
                    calendar.append([task['task_name'], start_datetime.strftime('%Y-%m-%d %H:%M:%S'), end_of_working_day.strftime('%Y-%m-%d %H:%M:%S')])
                    current_time = datetime.combine(current_time.date() + timedelta(days=1), working_hours['start_time'].time())
                    duration -= (end_of_working_day - start_datetime)
            
            else:
                current_time += timedelta(hours=1)  # Move current time forward by an hour
        
        if not assigned:
            # If task couldn't be assigned today and couldn't be split, start it from the beginning of the next day
            current_time = datetime.combine(current_time.date() + timedelta(days=1), working_hours['start_time'].time())

    return calendar

# Call the function to view and process tasks
view_and_process_tasks()

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
