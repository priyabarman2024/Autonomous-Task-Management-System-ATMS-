import streamlit as st
from agents.task_manager_agent import TaskManagerAgent
from agents.data_collector_agent import DataCollectorAgent
from agents.decision_making_agent import DecisionMakingAgent
from agents.execution_agent import ExecutionAgent
from api_integration.google_calendar import GoogleCalendar
from api_integration.email_integration import EmailIntegration
import datetime

# Initialize agents
task_manager = TaskManagerAgent()
data_collector = DataCollectorAgent()
decision_maker = DecisionMakingAgent()
executor = ExecutionAgent()

# Streamlit UI
st.title("Autonomous Task Management System")

# Task Input
st.header("Task Management")
task_name = st.text_input("Task Name", "Sample Task")
due_date = st.date_input("Due Date", datetime.date(2025, 6, 25))

# Add Task
if st.button("Add Task"):
    task_manager.add_task(task_name, due_date)
    st.success(f"Task '{task_name}' added!")

# Display Tasks
st.subheader("Current Tasks")
tasks = task_manager.get_all_tasks()
if tasks:
    for task in tasks:
        st.write(f"Task: {task['task_name']}, Due: {task['due_date']}, Status: {task['status']}")
else:
    st.write("No tasks yet!")

# Task Evaluation
st.header("Evaluate Tasks")
for task in task_manager.get_all_tasks():
    if task['status'] == 'Pending':
        priority = decision_maker.evaluate_task(task)
        st.write(f"Task: {task['task_name']} - Priority: {priority}")
        if st.button(f"Assign {task['task_name']}"):
            task_manager.assign_task(task['task_name'], executor)
# Example API Integration (Google Calendar)
st.header("Google Calendar Integration")

# Define event details
calendar_event = {
    'summary': 'Team Meeting',
    'start': {'dateTime': '2025-06-26T10:00:00-07:00', 'timeZone': 'America/Los_Angeles'},
    'end': {'dateTime': '2025-06-26T11:00:00-07:00', 'timeZone': 'America/Los_Angeles'}
}

# Create calendar event when button is clicked
if st.button("Create Calendar Event"):
    # Provide the full path to your credentials.json file here
    calendar = GoogleCalendar(r'C:\Users\toffe\OneDrive\Documents\Final_Projects\Agentic_AI\atms_project\credentials.json')
    
    # Create the event using the defined event details
    calendar.create_event(calendar_event)

# Email Integration
st.header("Email Reminders")
recipient_email = st.text_input("Recipient Email", "example@example.com")
email_subject = "Task Reminder"
email_body = "Please complete your tasks!"

if st.button("Send Email Reminder"):
    email_service = EmailIntegration('your_email@gmail.com', 'your_password')
    email_service.send_email(recipient_email, email_subject, email_body)
    st.success("Email sent!")

