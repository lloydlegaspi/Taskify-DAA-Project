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
    
    # Display tasks in a DataFrame
    if 'tasks' in st.session_state and st.session_state.tasks:  
        tasks_df = pd.DataFrame(st.session_state.tasks) 
        tasks_df['due_date'] = tasks_df['due_date'].apply(lambda x: x.strftime('%Y-%m-%d')) # Format due date
        tasks_df['priority'] = tasks_df['priority'].map({1: 'High', 2: 'Medium', 3: 'Low'}) # Map priority values
        # Rename columns to proper casing
        tasks_df.rename(columns={
            'task_name': 'Task',
            'due_date': 'Due Date',
            'priority': 'Priority',
            'duration': 'Duration'
        }, inplace=True)
        st.dataframe(tasks_df, hide_index=True, use_container_width=True) # Display tasks in a DataFrame
    else:
        st.write('No tasks added yet.')

    # Button to toggle the display of the task sections
    if st.session_state.show_tasks_sections: 
        if st.button('Process Tasks'):
            if not st.session_state.tasks:
                st.error('No tasks to process')
            else:
                calendar = assign_to_calendar(st.session_state.tasks, st.session_state.working_hours) # Assign tasks to calendar
                st.session_state.calendar = calendar # Store the calendar in session state
                st.success('Tasks processed and assigned to calendar!')

        container = st.container(border=True)

        # Display the calendar
        if 'calendar' in st.session_state and st.session_state.calendar:
            container.title('Scheduled Calendar')
            calendar_df = pd.DataFrame(st.session_state.calendar, columns=['Task Name', 'Start Time', 'End Time']) # Create DataFrame
            calendar_df['Start Time'] = pd.to_datetime(calendar_df['Start Time']) # Convert to datetime format
            # calendar_df = calendar_df.sort_values(by='Start Time', ascending=True) # Sort by start time
            calendar_df['Start Time'] = calendar_df['Start Time'].dt.strftime('%Y-%m-%d %I:%M %p') # Format start time
            container.dataframe(calendar_df, hide_index=True, use_container_width=True) # Display calendar in DataFrame

        if st.button('Export to .ICS'):
            calendar = ics.Calendar()
            local_timezone = pytz.timezone('Asia/Manila')  # Set to your local timezone

            for event in st.session_state.calendar: # Iterate through the calendar events and add them to the .ics file
                task_event = ics.Event(
                    name=event[0],
                    begin=local_timezone.localize(datetime.strptime(event[1], '%Y-%m-%d %H:%M:%S')), 
                    end=local_timezone.localize(datetime.strptime(event[2], '%Y-%m-%d %H:%M:%S'))
                )
                calendar.events.add(task_event)
            
            with open('schedule.ics', 'w') as f: # Write the calendar to a .ics file
                f.writelines(calendar)
            with open('schedule.ics', 'rb') as f: # Download the .ics file
                container.download_button('Download ICS file', f, file_name='schedule.ics')

# Function to sort tasks by due date and priority using merge sort
def merge_sort(tasks, key): 
    if len(tasks) <= 1: # Base case: if the length of the list is less than or equal to 1, return the list
        return tasks

    mid = len(tasks) // 2 # Find the middle of the list
    left_half = merge_sort(tasks[:mid], key) # Recursively sort the left half
    right_half = merge_sort(tasks[mid:], key) # Recursively sort the right half

    return merge(left_half, right_half, key) # Merge the sorted halves

# Function to merge two sorted lists
def merge(left, right, key):
    sorted_list = [] # Initialize an empty list to store the sorted elements
    i = j = 0 # Initialize pointers for left and right lists

    while i < len(left) and j < len(right): # Compare elements from both lists and append the smaller element to the sorted list
        if left[i][key] < right[j][key]: # If the element in the left list is smaller, append it to the sorted list
            sorted_list.append(left[i])
            i += 1
        elif left[i][key] > right[j][key]: # If the element in the right list is smaller, append it to the sorted list
            sorted_list.append(right[j]) 
            j += 1
        else:
            sorted_list.append(left[i]) # If the elements are equal, append the element from the left list
            i += 1

    while i < len(left): # Append the remaining elements from the left list to the sorted list
        sorted_list.append(left[i])
        i += 1

    while j < len(right): # Append the remaining elements from the right list to the sorted list
        sorted_list.append(right[j])
        j += 1

    return sorted_list 

# Function to sort tasks by due date and priority
def sort_tasks(tasks):
    tasks = merge_sort(tasks, 'due_date') # Sort tasks by due date
    start = 0 # Initialize the start index

    while start < len(tasks): # Iterate through the sorted tasks
        end = start 
        while end < len(tasks) and tasks[end]['due_date'] == tasks[start]['due_date']: # Find the end index of tasks with the same due date
            end += 1

        if end - start > 1: # If there are multiple tasks with the same due date, sort them by priority
            tasks[start:end] = merge_sort(tasks[start:end], 'priority') 

        start = end # Move the start index to the next due date

    return tasks

# Helper function to check if a time slot is free
def is_time_slot_free(calendar, start_time, end_time):
    for event in calendar:
        event_start = datetime.strptime(event[1], '%Y-%m-%d %H:%M:%S') # Convert event start time to datetime object
        event_end = datetime.strptime(event[2], '%Y-%m-%d %H:%M:%S') # Convert event end time to datetime object
        if not (end_time <= event_start or start_time >= event_end): # Check if the time slot overlaps with an existing event
            return False
    return True

# Function to assign tasks to a calendar based on working hours
def assign_to_calendar(tasks, working_hours):
    calendar = []

    # Set current_time to the start of the next working day
    current_time = datetime.now() + timedelta(days=1)
    current_time = current_time.replace(hour=working_hours['start_time'].hour, minute=0, second=0, microsecond=0)

    sorted_tasks = sort_tasks(tasks) # Sort tasks by due date and priority

    for task in sorted_tasks:
        duration = timedelta(hours=task['duration']) # Get task duration
        assigned = False # Initialize assigned flag
        
        while duration > timedelta(0): # Iterate until the task duration is fully assigned
            start_datetime = current_time # Set the start time of the task
            end_datetime = current_time + duration # Set the end time of the task
            
            # Calculate the end of the working day
            end_of_working_day = current_time.replace(hour=working_hours['end_time'].hour, minute=0, second=0, microsecond=0) 
            
            # Check if task fits within working hours and time slot is free
            if (working_hours['start_time'].time() <= start_datetime.time() < working_hours['end_time'].time() and
                is_time_slot_free(calendar, start_datetime, min(end_datetime, end_of_working_day))):
                
                if end_datetime <= end_of_working_day: # If task fits within the working day
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
