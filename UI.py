import streamlit as st
import pandas as pd
import os

def add_feedback(name, feedback):
    import csv
    
    # Define the feedback data
    new_feedback = [name, feedback, 'N/A']
    
    # Open the CSV file in append mode ('a') and write the feedback data
    with open('feedback.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_feedback)
    
    # Update the session state DataFrame by reading the updated CSV file
    st.session_state.feedback_df = pd.read_csv('feedback.csv')

def app():
    st.title('Feedback Tracking Dashboard')

    # Initialize an empty DataFrame to store feedback if it doesn't exist yet
    if 'feedback_df' not in st.session_state:
        if os.path.exists('feedback.csv'):
            st.session_state.feedback_df = pd.read_csv('feedback.csv')
        else:
            st.session_state.feedback_df = pd.DataFrame(columns=['Name', 'Feedback', 'Response'])

    # Form for submitting feedback
    with st.form(key='feedback_form'):
        name = st.text_input('Name')
        feedback = st.text_area('Feedback')
        submit_button = st.form_submit_button(label='Submit Feedback')

        if submit_button:
            add_feedback(name, feedback)

    # Display all feedback
    st.subheader('All Feedback')
    st.write(st.session_state.feedback_df)

if __name__ == "__main__":
    app()
