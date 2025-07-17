#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 14:44:50 2025

@author: srothman
"""

import streamlit as st
# Add CSS to force text wrapping (but keep default layout)
st.markdown(
    """
    <style>
    .block-container {
        overflow-wrap: break-word;
        word-wrap: break-word;
        hyphens: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)
from QuestionsSolutions_Q1toQ30 import (
    question_1, question_2, question_3, question_4, question_5,
    question_6, question_7, question_8, question_9, question_10,
    question_11, question_12, question_13, question_14, question_15,
    question_16, question_17, question_18, question_19, question_20,
    question_21, question_22, question_23, question_24, question_25,
    question_26, question_27, question_28, question_29, question_30,
    question_1_solution, question_2_solution, question_3_solution, question_4_solution, question_5_solution,
    question_6_solution, question_7_solution, question_8_solution, question_9_solution, question_10_solution,
    question_11_solution, question_12_solution, question_13_solution, question_14_solution, question_15_solution,
    question_16_solution, question_17_solution, question_18_solution, question_19_solution, question_20_solution,
    question_21_solution, question_22_solution, question_23_solution, question_24_solution, question_25_solution,
    question_26_solution, question_27_solution, question_28_solution, question_29_solution, question_30_solution
)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "intro"
if "question_number" not in st.session_state:
    st.session_state.question_number = 1
if "name" not in st.session_state:
    st.session_state.name = ""
if "email" not in st.session_state:
    st.session_state.email = ""


import streamlit as st
import csv
from datetime import datetime
import os

CSV_FILE = "student_info.csv"  # File to save student info

# Save student info (no duplicates)
def save_student_info(name, email, exam_date):
    file_exists = os.path.isfile(CSV_FILE)

    # Check if email already exists
    if is_duplicate(email):
        st.warning("This email is already saved.")
        return

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Email", "Exam Date", "Timestamp"])  # Header
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([name, email, exam_date, timestamp])
    st.success("✅ Student info saved successfully!")

def is_duplicate(email):
    try:
        with open(CSV_FILE, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if email.lower() == row[1].lower():  # Case-insensitive match
                    return True
    except FileNotFoundError:
        return False
    return False

# App UI
def intro_page():
    st.markdown("<h1 style='text-align: center;'>CST Math Review: Welcome!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Dr. Rothman</h3>", unsafe_allow_html=True)
    st.write("These practice questions for the mathematics portion of the New York State Content Specialty Exam (CST)")
    st.write("reflect feedback from LIU Post students who have successfully passed this exam.")
    st.write("It is our hope that you will share your exam experience with as an aid to future LIU Post test takers.")
    st.write("Please enter your information before starting the quiz.")
    st.write("This information will only be used to contact you about your CST Exam experience.")
   

    # Input fields directly tied to session_state
    name = st.text_input("Enter your full name:", key="name")
    email = st.text_input("Enter your email address:", key="email")
    exam_date = st.text_input("When do you plan to take the CST State Exam?", key="exam_date")

    # Start Quiz button
    if st.button("Start Quiz"):
        # Check all fields are filled
        if name and email and exam_date:
            # Save info to CSV
            save_student_info(name, email, exam_date)

            # Move to quiz
            st.session_state.page = "quiz"
            st.session_state.question_number = 1  # Start at Question 1
            st.rerun()
        else:
            st.warning("Please fill in all fields before starting.")



    st.write(f"CSV file will be saved to: `{os.path.abspath(CSV_FILE)}`")


def quiz_page():
    q_num = st.session_state.question_number
    st.header(f"Question {q_num}")
    
    # Call the appropriate question function
    if q_num == 1:
        question_1()
    elif q_num == 2:
        question_2()
    elif q_num == 3:
        question_3()
    elif q_num == 4:
        question_4()
    elif q_num == 5:
        question_5()
    elif q_num == 6:
        question_6()
    elif q_num == 7:
        question_7()
    elif q_num == 8:
        question_8()
    elif q_num == 9:
        question_9()
    elif q_num == 10:
        question_10()
    elif q_num == 11:
        question_11()
    elif q_num == 12:
        question_12()
    elif q_num == 13:
        question_13()
    elif q_num == 14:
        question_14()
    elif q_num == 15:
        question_15()
    elif q_num == 16:
        question_16()
    elif q_num == 17:
        question_17()
    elif q_num == 18:
        question_18()
    elif q_num == 19:
        question_19()
    elif q_num == 20:
        question_20()
    elif q_num == 21:
        question_21()
    elif q_num == 22:
        question_22()
    elif q_num == 23:
        question_23()
    elif q_num == 24:
        question_24()
    elif q_num == 25:
        question_25()
    elif q_num == 26:
        question_26()
    elif q_num == 27:
        question_27()
    elif q_num == 28:
        question_28()
    elif q_num == 29:
        question_29()
    elif q_num == 30:
        question_30()
    else:
        st.success("You’ve completed all 30 questions! 🎉")
        return
    
    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Show Solution"):
            show_solution(q_num)
    with col2:
        if st.button("Next Question"):
            st.session_state.question_number += 1
            st.rerun()


def show_solution(q_num):
    # Call the appropriate solution function
    if q_num == 1:
        question_1_solution()
    elif q_num == 2:
        question_2_solution()
    elif q_num == 3:
        question_3_solution()
    elif q_num == 4:
        question_4_solution()
    elif q_num == 5:
        question_5_solution()
    elif q_num == 6:
        question_6_solution()
    elif q_num == 7:
        question_7_solution()
    elif q_num == 8:
        question_8_solution()
    elif q_num == 9:
        question_9_solution()
    elif q_num == 10:
        question_10_solution()
    elif q_num == 11:
        question_11_solution()
    elif q_num == 12:
        question_12_solution()
    elif q_num == 13:
        question_13_solution()
    elif q_num == 14:
        question_14_solution()
    elif q_num == 15:
        question_15_solution()
    elif q_num == 16:
        question_16_solution()
    elif q_num == 17:
        question_17_solution()
    elif q_num == 18:
        question_18_solution()
    elif q_num == 19:
        question_19_solution()
    elif q_num == 20:
        question_20_solution()
    elif q_num == 21:
        question_21_solution()
    elif q_num == 22:
        question_22_solution()
    elif q_num == 23:
        question_23_solution()
    elif q_num == 24:
        question_24_solution()
    elif q_num == 25:
        question_25_solution()
    elif q_num == 26:
        question_26_solution()
    elif q_num == 27:
        question_27_solution()
    elif q_num == 28:
        question_28_solution()
    elif q_num == 29:
        question_29_solution()
    elif q_num == 30:
        question_30_solution()


def main():
    if st.session_state.page == "intro":
        intro_page()
    elif st.session_state.page == "quiz":
        quiz_page()


if __name__ == "__main__":
    main()




