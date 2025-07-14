#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 14:44:50 2025

@author: srothman
"""
import streamlit as st
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

# Session state for current question
if 'current_question' not in st.session_state:
    st.session_state.current_question = 1

# Map question numbers to functions
question_functions = {
    1: question_1, 2: question_2, 3: question_3, 4: question_4, 5: question_5,
    6: question_6, 7: question_7, 8: question_8, 9: question_9, 10: question_10,
    11: question_11, 12: question_12, 13: question_13, 14: question_14, 15: question_15,
    16: question_16, 17: question_17, 18: question_18, 19: question_19, 20: question_20,
    21: question_21, 22: question_22, 23: question_23, 24: question_24, 25: question_25,
    26: question_26, 27: question_27, 28: question_28, 29: question_29, 30: question_30,
}

solution_functions = {
    1: question_1_solution, 2: question_2_solution, 3: question_3_solution, 4: question_4_solution, 5: question_5_solution,
    6: question_6_solution, 7: question_7_solution, 8: question_8_solution, 9: question_9_solution, 10: question_10_solution,
    11: question_11_solution, 12: question_12_solution, 13: question_13_solution, 14: question_14_solution, 15: question_15_solution,
    16: question_16_solution, 17: question_17_solution, 18: question_18_solution, 19: question_19_solution, 20: question_20_solution,
    21: question_21_solution, 22: question_22_solution, 23: question_23_solution, 24: question_24_solution, 25: question_25_solution,
    26: question_26_solution, 27: question_27_solution, 28: question_28_solution, 29: question_29_solution, 30: question_30_solution,
}

# Display current question
q_num = st.session_state.current_question
st.write(f"### Question {q_num}")
question_functions[q_num]()

# Buttons
if st.button("Show Solution"):
    solution_functions[q_num]()

if q_num < 30:
    if st.button("Next Question"):
        st.session_state.current_question += 1
        st.rerun()
else:
    st.write("🎉 You’ve completed all 30 questions!")
