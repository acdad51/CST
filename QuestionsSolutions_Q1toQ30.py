#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 14:50:43 2025

@author: srothman
"""
import streamlit as st

# === QUESTIONS 1–10 ===

import streamlit as st

def question_1():
    st.write("50 coins consisting of quarters \\((q)\\) and dimes \\((d)\\) total \\($9.20\\).")
    st.write("Which equations can be used to solve for the number of quarters and dimes?")

    choice = st.radio(
        "Select your answer:",
        [
            r"$q + d = 50,\ 10q + 25d = 920$",
            r"$q + d = 50,\ 25q + 10d = 920$",
            r"$q + d = 9.20,\ 25q + 10d = 50$",
            r"$q + d = 50,\ 0.25q + 0.10d = 920$"
        ],
        index=None,
        key="q1_choice"
    )

    if choice == r"$q + d = 50,\ 25q + 10d = 920$":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")






def question_2():
    #st.markdown("### Question 2")
    st.write("A table of 200 students shows the results of a survey.")
    st.write("One row shows 34 third graders from one category.")
    st.write("If there are a total of 110 third graders, what is the probability of picking this category?")

    choice = st.radio(
        "Select your answer:",
        [
            "34 / 200",
            "34 / 110",
            "76 / 200",
            "76 / 110"
        ],
        index=None,
        key="q2_choice"
    )

    if choice == "34 / 110":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_3():
    #st.markdown("### Question 3")
    st.markdown("A 13-ounce box of cereal costs \\$3.90 and another 2.5 lb box of cereal costs \\$6.50.")
    st.markdown("What is the difference in the price per pound for the two boxes of cereal?")

    choice = st.radio(
        "Select your answer:",
        [
            "$0.20",
            "$0.1375",
            "$0.10",
            "$0.25"
        ],
        index=None,
        key="q3_choice"
    )

    if choice == "$0.1375":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_4():
    #st.markdown("### Question 4")
    st.write("Given the number 3333.231, which digit to the left of the decimal point is 1000 times the 3 to the right of the decimal?")

    choice = st.radio(
        "Select your answer:",
        [
            "3 (in thousands place)",
            "3 (in ones place)",
            "3 (in hundreds place)",
            "3 (in tens place)"
        ],
        index=None,
        key="q4_choice"
    )

    if choice == "3 (in thousands place)":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_5():
    st.latex(r"\text{The time for light to travel back and forth from Uranus to Earth is } 1.74 \times 10^4\ \text{seconds.}")
    st.latex(r"\text{If light travels at } 2.6 \times 10^{14}\ \text{cm/sec, how many kilometers is it from Uranus to Earth (one way)?}")

    choices = [
        "2.262 × 10¹³ km",
        "4.524 × 10¹³ km",
        "2.6 × 10¹⁴ km",
        "1.74 × 10⁴ km"
    ]

    # Display choices using st.markdown to format math
    for idx, option in enumerate(choices, start=1):
        st.markdown(f"**({chr(96+idx)})**  {option}")

    # Radio buttons with plain text options for selection
    choice = st.radio(
        "Select your answer:",
        choices,
        index=None,
        key="q5_choice"
    )

    if choice == "2.262 × 10¹³ km":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")



def question_6():
    #st.markdown("### Question 6")
    st.write("Item A originally costs $2000. If it is (a) reduced by 15% or (b) reduced by 5% and then by 10%, what is the difference in the final prices of item A?")

    choice = st.radio(
        "Select your answer:",
        [
            "$30",
            "$10",
            "$25",
            "$15"
        ],
        index=None,
        key="q6_choice"
    )

    if choice == "$20":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_7():
    #st.markdown("### Question 7")
    st.write("If the fraction 3/7 is changed to its equivalent decimal, how many digits repeat?")

    choice = st.radio(
        "Select your answer:",
        [
            "5",
            "6",
            "7",
            "8"
        ],
        index=None,
        key="q7_choice"
    )

    if choice == "6":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_8():
    #st.markdown("### Question 8")
    st.write("A company gets 80 responses from 200 surveys sent out. If they want an increase of 20 responses, how many surveys do they need to send out?")

    choice = st.radio(
        "Select your answer:",
        [
            "220",
            "250",
            "300",
            "240"
        ],
        index=None,
        key="q8_choice"
    )

    if choice == "250":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_9():
    #st.markdown("### Question 9")
    st.write("If the average speed of an object is measured 20 times over one second, how can we best estimate the average speed?")

    choice = st.radio(
        "Select your answer:",
        [
            "Median",
            "Mean",
            "Mode",
            "Range"
        ],
        index=None,
        key="q9_choice"
    )

    if choice == "Mean":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

    


def question_10():
    # Left-justified question
    st.markdown(
        "10. Given the three points $A(-3,7)$, $D(3,-1)$, and $C(0,-5)$, "
        "find the perimeter of the parallelogram with these points as vertices."
    )

    # Choices: plain text for radio buttons
    choice = st.radio(
        "Select your answer:",
        [
            "63.86",         # ✅ Correct answer
            "31.93",         # ❌ Forgot to double the sides
            "127.72",        # ❌ Double-counted the full perimeter
            "50.00"          # ❌ Rough estimate or calculation error
        ],
        index=None,
        key="q10_choice"
    )

    if choice == "63.86":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")



    



def question_1_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Let } q \text{ be the number of quarters and } d \text{ the number of dimes.} \\
    q + d = 50 \\
    0.25q + 0.10d = 9.20 \\
    \text{Multiply by 100: } 25q + 10d = 920
    """)

def question_2_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    P(E) = \dfrac{\text{Number of successes}}{\text{Total number of possibilities}} \\
    Here: P(E) = \dfrac{34}{110}
    """)

def question_3_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Price per ounce for 13 oz box: } \dfrac{\$3.90}{13} \approx \$0.30 \text{ per oz} \\
    \text{Price per ounce for 2.5 lb box: } 2.5 \text{ lb} = 40 \text{ oz} \\
    \dfrac{\$6.50}{40} = \$0.1625 \text{ per oz} \\
    \text{Difference: } \$0.30 - \$0.1625 = \boxed{\$0.1375 \text{ per oz}}
    """)

def question_4_solution():
    st.write("✅ Correct answer: (a)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{The 3 to the right of the decimal is in the } \tfrac{1}{1000} \text{th place.} \\
    \text{The 3 in the thousands place is 1000 times larger.}
    """)


def question_5_solution():
    st.write("✅ Correct answer: \(2.262 \times 10^{13}\ \mathrm{km}\)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Time for round trip: } 1.74 \times 10^4\ \mathrm{s} \\
    \text{One-way time: } \dfrac{1.74 \times 10^4}{2} = 8.7 \times 10^3\ \mathrm{s} \\
    \text{Speed of light: } 2.6 \times 10^{14}\ \mathrm{cm/s} \\
    \text{Distance (cm): } (2.6 \times 10^{14}) \times (8.7 \times 10^3) \\
    = (2.6 \times 8.7) \times 10^{14+3}\ \mathrm{cm} \\
    = 22.62 \times 10^{17}\ \mathrm{cm} \\
    = 2.262 \times 10^{18}\ \mathrm{cm} \\
    \text{Convert to km: } 1\ \mathrm{km}=10^5\ \mathrm{cm} \\
    \dfrac{2.262 \times 10^{18}\ \mathrm{cm}}{10^5} = 2.262 \times 10^{13}\ \mathrm{km} \\
    \boxed{2.262 \times 10^{13}\ \mathrm{km}}
    """)
# ... Continue similarly for question_6 through question_10 ...

# NOTE: I’ll send Q6–Q10 next.


def question_6_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \mathbf{Worked\text{-}Out\ Solution} \\
    15\%\ \mathrm{reduction:}\ 2000 \times 0.85 = 1700 \\
    5\%\ \mathrm{then}\ 10\%\ \mathrm{reduction:}\ 2000 \times 0.95 \times 0.90 = 1710 \\
    \mathrm{Difference:}\ 1710 - 1700 = \boxed{10}
    """)


def question_7_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \frac{3}{7} = 0.\overline{428571} \text{ (repeats every 6 digits)} \\
    \boxed{6}
    """)


def question_8_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Current response rate: } \dfrac{80}{200} = 40\% \\
    \text{Desired responses: } 80 + 20 = 100 \\
    \text{Required surveys: } \dfrac{100}{0.4} = \boxed{250}
    """)


def question_9_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{The mean gives the best estimate for central tendency.} \\
    \boxed{\text{Mean}}
    """)

def question_10_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{We are given three points: } A(-3, 7),\ D(3, -1),\ C(0, -5). \\
    \textbf{Step 1: Find the fourth vertex.} \\
    \overrightarrow{AC} = (0 - (-3),\ -5 - 7) = (3, -12). \\
    B = D + \overrightarrow{AC} = (3, -1) + (3, -12) = (6, -13). \\
    \\
    \textbf{Step 2: Compute side lengths.} \\
    AB = \sqrt{(6 - (-3))^2 + (-13 - 7)^2} \\
    = \sqrt{9^2 + (-20)^2} = \sqrt{81 + 400} = \sqrt{481}. \\
    AD = \sqrt{(3 - (-3))^2 + (-1 - 7)^2} \\
    = \sqrt{6^2 + (-8)^2} = \sqrt{36 + 64} = \sqrt{100} = 10. \\
    \\
    \textbf{Step 3: Find the perimeter.} \\
    P = 2 \times (AB + AD) \\
    = 2 \times \left(\sqrt{481} + 10\right) \\
    \approx 2 \times (21.93 + 10) = 2 \times 31.93 = 63.86. \\
    \\
    \boxed{P = 63.86}
    """)


def question_11():
    # Left-justified and math-like question
    st.markdown(
        "Pressure $P$ is directly proportional to temperature $T$. "
        "The constant of proportionality is 2.6. Write the equation relating pressure and temperature."
    )

    # Render choices as LaTeX
    choice = st.radio(
        "Select your answer:",
        [
            r"$P = \dfrac{2.6}{T}$",
            r"$P = 2.6T$",              # ✅ Correct answer
            r"$P = T + 2.6$",
            r"$P = T - 2.6$"
        ],
        index=None,
        key="q11_choice"
    )

    # Evaluate answer
    if choice:
        if choice == r"$P = 2.6T$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")




def question_11_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Since } P \propto T, \text{ we have } P = kT. \\
    \text{Given } k = 2.6, \text{ so } P = 2.6T. \\
    \boxed{P = 2.6T}
    """)
def question_12():
    st.write("The surface area of an object is given by")
    st.latex(r"A = 6\sqrt[3]{V^2}")
    st.write("Find")
    st.latex(r"V \text{ if } A = 18.")

    choice = st.radio(
        "Select your answer:",
        [
            r"$3$",
            r"$3\sqrt{3}$",
            r"$6$",
            r"$2\sqrt{3}$"
        ],
        index=None,
        key="q12_choice"
    )

    if choice:
        if choice == r"$3\sqrt{3}$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")




def question_12_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    A = 6\sqrt[3]{V^2},\ A=18 \\
    \dfrac{18}{6} = \sqrt[3]{V^2} \implies 3 = \sqrt[3]{V^2} \\
    (3)^3 = (\sqrt[3]{V^2})^3 \implies 27 = V^2 \\
    V = \sqrt{27} = \sqrt{9 \cdot 3} = 3\sqrt{3} \\
    \boxed{3\sqrt{3}}
    """)

def question_13():
    st.write("The compound interest formula is given by")
    st.latex(r"A = A_0(1 + r)^t")
   # st.write("If")
    st.latex(r"\text{If } A = \$60,000, \ A_0 = \$50,000, \ t = 3.")
    st.latex(r"\text{Find the annual interest rate }\, r.")

    choice = st.radio(
        "Select your answer:",
        [
            r"$5.5\%$",
            r"$6.27\%$",
            r"$7\%$",
            r"$8\%$"
        ],
        index=None,
        key="q13_choice"
    )

    if choice:
        if choice == r"$6.27\%$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")




def question_13_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    A = A_0(1 + r)^t,\ 60000 = 50000(1 + r)^3 \\
    \dfrac{60000}{50000} = (1 + r)^3 \implies 1.2 = (1 + r)^3 \\
    (1 + r) = \sqrt[3]{1.2} \approx 1.0627 \\
    r = 1.0627 - 1 = 0.0627 = 6.27\% \\
    \boxed{6.27\%}
    """)

def question_14():
   #st.markdown("### Question 14")
    st.write("Bicycle A travels 35 feet on 5 revolutions while bicycle B travels 49 feet on 10 revolutions. What is the ratio of one revolution of B to one revolution of A?")

    choice = st.radio(
        "Select your answer:",
        [
            "0.6",
            "0.7",
            "0.8",
            "0.75"
        ],
        index=None,
        key="q14_choice"
    )

    if choice:
        if choice == "0.7":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_14_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{A: } \dfrac{35}{5} = 7\ \text{ft/rev} \\
    \text{B: } \dfrac{49}{10} = 4.9\ \text{ft/rev} \\
    \dfrac{\text{B}}{\text{A}} = \dfrac{4.9}{7} = \boxed{0.7}
    """)

def question_15():
    #st.markdown("### Question 15")
    st.write("Given an arithmetic sequence where the third term is 17 and the sixth term is 29, find the 20th term.")

    choice = st.radio(
        "Select your answer:",
        [
            "70",
            "71",
            "72",
            "73"
        ],
        index=None,
        key="q15_choice"
    )

    if choice:
        if choice == "71":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_15_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Let } a_1 = a,\ d = \text{common difference.} \\
    a_3 = a + 2d = 17,\ a_6 = a + 5d = 29 \\
    (a + 5d) - (a + 2d) = 29 - 17 \implies 3d = 12 \implies d = 4 \\
    a + 2d = 17 \implies a + 8 = 17 \implies a = 9 \\
    a_{20} = a + 19d = 9 + 19(4) = 9 + 76 = \boxed{85}
    """)

def question_16():
    #st.markdown("### Question 16")
    st.write("A fair coin is tossed three times. What is the probability of getting exactly two heads?")

    choice = st.radio(
        "Select your answer:",
        [
            "1/2",
            "3/8",
            "1/8",
            "1/4"
        ],
        index=None,
        key="q16_choice"
    )

    if choice:
        if choice == "3/8":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_16_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Sample space: } 2^3 = 8\ \text{outcomes.} \\
    \text{Favorable outcomes: HHT, HTH, THH (3 outcomes)} \\
    P(\text{exactly 2 heads}) = \dfrac{3}{8} \\
    \boxed{\dfrac{3}{8}}
    """)

def question_17():
    #st.markdown("### Question 17")
    st.write("Which one is a counterexample to the statement: 'The product of two irrational numbers is an irrational number'?")

    choice = st.radio(
        "Select your answer:",
        [
            "√2 ⋅ √8",
            "√4 ⋅ √8",
            "π ⋅ √2",
            "√3 ⋅ √5"
        ],
        index=None,
        key="q17_choice"
    )

    if choice:
        if choice == "√2 ⋅ √4":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_17_solution():
    st.write("✅ Correct answer: (a)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \sqrt{2}\ \text{is irrational,}\ \sqrt{8}\ \text{is irrational.} \\
    \sqrt{2} \cdot \sqrt{8} = \sqrt{16} = 4\ \text{is rational.} \\
    \boxed{\sqrt{2} \cdot \sqrt{8}\ \textbf{is a counterexample.}} \\
    """)

def question_18():
    #st.markdown("### Question 18")
    st.write("A box contains 8 white balls and 16 red balls. What is the red-to-white constant of proportionality?")

    choice = st.radio(
        "Select your answer:",
        [
            "1/2",
            "2",
            "3",
            "3/2"
        ],
        index=None,
        key="q18_choice"
    )

    if choice:
        if choice == "2":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    



def question_18_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Red:White ratio } = \dfrac{16}{8} = 2 \\
    \boxed{2}
    """)

def question_19():
    #st.markdown("### Question 19")
    st.write("Given the two similar triangles below, find \(x\).")
    st.image("SimilarTriangles19.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            "4",
            "12.5",
            "8",
            "10"
        ],
        index=None,
        key="q19_choice"
    )

    if choice:
        if choice == "12.5":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    
def question_19_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Using similarity, set up a proportion:} \\
    \dfrac{5}{2} = \dfrac{x}{5} \implies x = \dfrac{5 \cdot 5}{2} = 12.5 \\
    \boxed{12.5}
    """)

def question_20():
    #st.markdown("### Question 20")
    st.write("What does the diagram below show?")
    st.image("Fractions20.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            "These represent equivalent fractions.",
            "These represent inequivalent fractions.",
            "These represent fractions with a common denominator.",
            "These represent proper fractions."
        ],
        index=None,
        key="q20_choice"
    )

    if choice:
        if choice == "These represent inequivalent fractions.":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    



def question_20_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{The fractions in the diagram are NOT equivalent.} \\
    \text{The first represents 4/6 = 1/3 but the second represents 
    \text4/12 = 1/3.}\\
    \boxed{\text{Inequivalent Fractions}}
    """)

def question_21():
    st.write("Which equation can be used to find:")
    st.latex(r"x")
    st.image("Pythag21.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            r"$x + y = 10$",
            r"$10^2 + (5x)^2 = 20^2$",
            r"$x^2 + y^2 = 25$",
            r"$x^2 - y^2 = 20$"
        ],
        index=None,
        key="q21_choice"
    )

    if choice:
        if choice == r"$10^2 + (5x)^2 = 20^2$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")


    


def question_21_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Using Pythagoras: } \\
    (5x)^2 + 10^2 = 20^2 \\
    \boxed{10^2 + (5x)^2 = 20^2}
    """)

def question_22():
    st.write("Which balances with:")
    st.latex(r"x")
    st.image("Scale22.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            r"$y$ and a dot",
            r"$2y$ and a dot",
            r"$3y$",
            r"a single dot"
        ],
        index=None,
        key="q22_choice"
    )

    if choice:
        if choice == r"$2y$ and a dot":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

def question_22_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Two }y\text{'s and one dot balance with }x. \\
    \boxed{2y + \text{dot}}
    """)

def question_23():
    #st.markdown("### Question 23")
    st.write("Which point is closest to \(\sqrt{1000}\)?")
    st.image("NumberLine23.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            "Point C",
            "Point A",
            "Point B",
            "Point D"
        ],
        index=None,
        key="q23_choice"
    )

    if choice:
        if choice == "Point A":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_23_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \sqrt{1000} \approx 31.62 \\
    \text{Point A is closest to this value.} \\
    \boxed{A}
    """)


def question_24():
    st.write("Container B holds twice as much liquid as container A. "
             "If container A presently has 24 ounces and this is 30% of its capacity, "
             "and container B presently holds 48 ounces, "
             "what percentage of container B will be filled after pouring the contents" 
             "of container A into it?")

    choice = st.radio(
        "Select your answer:",
        [
            "30%",
            "45%",   # ✅ Correct
            "60%",
            "50%"
        ],
        index=None,
        key="q24_choice"
    )

    if choice:
        if choice == "45%":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")


    

def question_24_solution():
    st.write("✅ Correct answer: 45%")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Container A: } 24\ \mathrm{oz} = 30\%\ \text{of its capacity} \\
    \implies \text{Capacity of A} = \dfrac{24}{0.3} = 80\ \mathrm{oz} \\
    \text{Container B: Capacity} = 2 \times 80 = 160\ \mathrm{oz} \\
    \\
    \text{Liquid in B before pouring: } 48\ \mathrm{oz} \\
    \text{Liquid added from A: } 24\ \mathrm{oz} \\
    \text{Total in B: } 48 + 24 = 72\ \mathrm{oz} \\
    \text{Percentage filled: } \dfrac{72}{160} \times 100\% = \boxed{45\%}
    """)



def question_25():
    #st.markdown("### Question 25")
    st.write("Why are these triangles similar?")
    st.image("Slope25.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            "Because they are right triangles",
            "Because a straight line has constant slope",
            "Because they have proportional sides",
            "Because their angles add up to 180°"
        ],
        index=None,
        key="q25_choice"
    )

    if choice:
        if choice == "Because a straight line has constant slope":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_25_solution():
    #st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{A straight line has a constant slope, so the triangles are similar because the sides are proportional.} \\
    \boxed{\text{Constant Slope}}
    """)
    

def question_26():
    st.markdown("Which equation is true for the function $y = f(x)$ drawn below?")
    st.image("Parabola26.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            r"$f(x) = -f(x)$",
            r"$f(x) = f(-x)$",      # ✅ Correct
            r"$f(-x) = -f(x)$",
            r"$f(x) = x^2$"
        ],
        index=None,
        key="q26_choice"
    )

    if choice:
        if choice == r"$f(x) = f(-x)$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

def question_26():
    st.markdown("Which equation is true for the function $y = f(x)$ drawn below?")
    st.image("Parabola26.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            r"$f(x) = -f(x)$",
            r"$f(x) = f(-x)$",      # ✅ Correct
            r"$f(-x) = -f(x)$",
            r"$f(x) = x^2$"
        ],
        index=None,
        key="q26_choice"
    )

    if choice:
        if choice == r"$f(x) = f(-x)$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")


def question_26_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{The graph is symmetric about the y-axis, so: } \\
    f(x) = f(-x)
    """)

def question_27():
    #st.markdown("### Question 27")
    st.write("Which conversion is correct?")
    # st.image("Conversion27.png", width=400)  # Uncomment if you have an image

    choice = st.radio(
        "Select your answer:",
        [
            "10 centimeters = 1 meter",
            "100,000 centimeters = 1 kilometer",
            "1,000 centimeters = 1 meter",
            "100 centimeters = 1 meter"
        ],
        index=None,
        key="q27_choice"
    )

    if choice:
        if choice == "100 centimeters = 1 meter":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_27_solution():
    st.write("✅ Correct answer: (d)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \boxed{100\ \text{centimeters} = 1\ \text{meter}}
    """)

def question_28():
    # Left-justified question with inline math
    st.markdown("Which equation is correct?")

    choice = st.radio(
        "Select your answer:",
        [
            r"$8 - (x-y)z = 8 - xz - yz$",
            r"$8 - (x-y)z = 8 - xz + yz$",  # ✅ Correct
            r"$8 - (x-y)z = 8 + xz - yz$",
            r"$8 - (x-y)z = 8 + xz + yz$"
        ],
        index=None,
        key="q28_choice"
    )

    if choice:
        if choice == r"$8 - (x-y)z = 8 - xz + yz$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")


    


def question_28_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Distribute the negative sign:} \\
    8 - (x-y)z = 8 - xz + yz
    """)

def question_29():
    #st.markdown("### Question 29")
    st.write("Would you use a histogram, pie chart, or scatter plot to look at students and their GPAs?")

    choice = st.radio(
        "Select your answer:",
        [
            "Pie Chart",
            "Histogram",
            "Scatter Plot",
            "Bar Graph"
        ],
        index=None,
        key="q29_choice"
    )

    if choice:
        if choice == "Histogram":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_29_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{A histogram is best for showing the distribution of GPAs.}
    """)

def question_30():
    st.markdown("Which equation represents the graph of the line drawn?")
    st.image("LineThroughOrigin30.png", width=400)

    choice = st.radio(
        "Select your answer:",
        [
            r"$y = -x$",
            r"$y = x$",        # ✅ Correct
            r"$y = x + 1$",
            r"$y = -x + 1$"
        ],
        index=None,
        key="q30_choice"
    )

    if choice:
        if choice == r"$y = x$":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")


    


def question_30_solution():
    st.write("✅ Correct answer: (b)")
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{This is a line passing through the origin with slope }1. \\
    \boxed{y = x}
    """)
def run_quiz():
    # Call all 30 questions in order
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()
    question_7()
    question_8()
    question_9()
    question_10()
    question_11()
    question_12()
    question_13()
    question_14()
    question_15()
    question_16()
    question_17()
    question_18()
    question_19()
    question_20()
    question_21()
    question_22()
    question_23()
    question_24()
    question_25()
    question_26()
    question_27()
    question_28()
    question_29()
    question_30()


