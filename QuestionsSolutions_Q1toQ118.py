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
    #st.write("50 coins consisting of quarters, q, and dimes, d, total $9.20.")
    #st.write("Which equations can be used to solve for the number of quarters and dimes?")
    st.markdown("50 coins consisting of quarters ($q$) and dimes ($d$) total \\$9.20.")


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
    # st.markdown("### Question 2")
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

    if choice == "$10":
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
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Let } q \text{ be the number of quarters and } d \text{ the number of dimes.} \\
    q + d = 50 \\
    0.25q + 0.10d = 9.20 \\
    \text{Multiply by 100: } 25q + 10d = 920
    """)
    st.write("**Answer:**")
    st.latex(r"q + d = 50,\quad 25q + 10d = 920")

def question_2_solution():
    st.write("**Worked-Out Solution (Q2)**")
    st.latex(
        r"""
        P(E) = \dfrac{\text{Number of successes}}{\text{Total number of possibilities}}\\
        P(E) = \dfrac{34}{110}
        """
    )
    st.write("**Answer:** 34 / 110")



def question_3_solution():
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Price per ounce for 13 oz box: } \dfrac{\$3.90}{13} \approx \$0.30 \text{ per oz} \\
    \text{Price per ounce for 2.5 lb box: } 2.5 \text{ lb} = 40 \text{ oz} \\
    \dfrac{\$6.50}{40} = \$0.1625 \text{ per oz} \\
    \text{Difference: } \$0.30 - \$0.1625 = \boxed{\$0.1375 \text{ per oz}}
    """)
    st.write("**Answer:**")
    st.latex(r"\$0.1375")

def question_4_solution():
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{The 3 to the right of the decimal is in the } \tfrac{1}{1000} \text{th place.} \\
    \text{The 3 in the thousands place is 1000 times larger.}
    """)
    st.write("**Answer:**: 3(in thousands place)")


def question_5_solution():
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
    st.latex(r"""
    \mathbf{Worked\text{-}Out\ Solution} \\
    15\%\ \mathrm{reduction:}\ 2000 \times 0.85 = 1700 \\
    5\%\ \mathrm{then}\ 10\%\ \mathrm{reduction:}\ 2000 \times 0.95 \times 0.90 = 1710 \\
    \mathrm{Difference:}\ 1710 - 1700 = \boxed{10}
    """)


def question_7_solution():
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \frac{3}{7} = 0.\overline{428571} \text{ (repeats every 6 digits)} \\
    \boxed{6}
    """)


def question_8_solution():
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Current response rate: } \dfrac{80}{200} = 40\% \\
    \text{Desired responses: } 80 + 20 = 100 \\
    \text{Required surveys: } \dfrac{100}{0.4} = \boxed{250}
    """)


def question_9_solution():
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{The mean gives the best estimate for central tendency.} \\
    \boxed{\text{Mean}}
    """)

def question_10_solution():
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
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Since } P \propto T, \text{ we have } P = kT. \\
    \text{Given } k = 2.6, \text{ so } P = 2.6T. \\
    \boxed{P = 2.6T}
    """)

def question_12():
    st.write("The surface area of an object is given by")
    st.latex(r"A = 6\sqrt[3]{V^2}")
    st.markdown("Find $V$ if $A = 18$.")

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
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    A = 6\sqrt[3]{V^2},\ A=18 \\
    \dfrac{18}{6} = \sqrt[3]{V^2} \implies 3 = \sqrt[3]{V^2} \\
    (3)^3 = (\sqrt[3]{V^2})^3 \implies 27 = V^2 \\
    V = \sqrt{27} = \sqrt{9 \cdot 3} = 3\sqrt{3} \\
    \boxed{3\sqrt{3}}
    """)

def question_13():
    st.write("The compound interest formula is given by:")
    st.latex(r"A = A_0 (1 + r)^t")
    st.write("If:")
    st.latex(r"A = \$60,000,\ A_0 = \$50,000,\ t = 3")
    st.write("Find the annual interest rate $r$.")

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
            "80",
            "83",
            "84",
            "85"
        ],
        index=None,
        key="q15_choice"
    )

    if choice:
        if choice == "85":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_15_solution():
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
        if choice == "√2 ⋅ √8":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Try again.")

    


def question_17_solution():
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
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{The fractions in the diagram are NOT equivalent.} \\
    \text{The first represents 4/6 = 1/3 but the second represents}\\ 
    \text{4/12 = 1/3.}\\
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
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{Two }y\text{'s and one dot balance with }x. \\
    \boxed{2y + \text{a dot}}
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
    st.markdown("**Worked-Out Solution**  \n"  # <- note the double space before \n
                "A straight line has a constant slope, so the triangles are similar  \n"
                "because the sides are proportional.  \n")
    st.latex(r"\boxed{\text{Constant Slope}}")
    

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
    st.latex(r"""
    \textbf{Worked-Out Solution} \\
    \text{This is a line passing through the origin with slope }1. \\
    \boxed{y = x}
    """)

def question_31():
    # Question prompt
    st.write("What is the correct order (least to greatest from left to right)?")
    st.write("3 ⁄ 4, 40%, 2⁵, 20, 5 ⁄ 8")  # use Unicode fraction slash (⁄) and superscript ⁵

    # Choices (clean Unicode formatting)
    choices = [
        "40%, 5 ⁄ 8, 3 ⁄ 4, 2⁵, 20",   # ✅ correct
        "5 ⁄ 8, 40%, 3 ⁄ 4, 20, 2⁵",
        "40%, 5 ⁄ 8, 3 ⁄ 4, 20, 2⁵",
        "40%, 3 ⁄ 4, 5 ⁄ 8, 2⁵, 20"
    ]

    # Display each option with labels (a–d)
    for idx, option in enumerate(choices, start=1):
        st.markdown(f"**({chr(96+idx)})**  {option}")

    # Radio for selection
    choice = st.radio(
        "Select your answer:",
        choices,
        index=None,
        key="q31_choice"
    )

    if choice == "40%, 5 ⁄ 8, 3 ⁄ 4, 20, 2⁵":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")





def question_31_solution():
    st.latex(r"""
    \begin{aligned}
    &40\% = 0.40,\quad \frac{5}{8}=0.625,\quad \frac{3}{4}=0.75,\quad 20=20,\quad 2^5=32 \\
    &\text{Order (least to greatest): } 0.40,\ 0.625,\ 0.75,\ 20,\ 32 \\
    &\Rightarrow\ 40\%,\ 5/8,\ 3/4,\ 20,\ 2^5
    \end{aligned}
    """)

def question_32():
    st.write("In a board game, if you roll doubles, you double your points. "
             "What is the probability that on one roll of two standard dice (1–6) you roll a double?")
    choice = st.radio(
        "Select your answer:",
        ["1/3", "1/6", "1/12", "1/36"],
        index=None, key="q32_choice"
    )
    if choice == "1/6":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_32_solution():
    st.latex(r"\text{Doubles: }(1,1),(2,2),\ldots,(6,6)\Rightarrow 6\ \text{out of }36=\boxed{\tfrac{1}{6}}")

def question_33():
    st.write("If there are 2.54 centimeters in 1 inch, how many centimeters, to the nearest hundredth, are in a yard?")
    st.write("(1 yard = 36 inches)")
    choice = st.radio(
        "Select your answer:",
        ["86.36 cm", "90.14 cm", "91.44 cm", "94.20 cm"],
        index=None, key="q33_choice"
    )
    if choice == "91.44 cm":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_33_solution():
    st.latex(r"1\ \text{yard}=36\ \text{inches}")
    st.latex(r"36\times 2.54=\boxed{91.44\ \text{cm}}")

def question_34():
    # Use markdown to format variables cleanly
    st.markdown(
        r"Keisha is ordering merchandise. Shipping is \$5.00 for the first 10 oz, "
        r"then \$0.75 per additional ounce."
    )
    st.markdown(
        r"Which algebraic expression gives the shipping charge for a shipment weighing \(x\) ounces, where \(x>10\)?"
    )
    choice = st.radio(
        "Select your answer:",
        ["5 + 0.75x", "5 + 0.75(x - 10)", "0.75(x + 10) + 5", "0.75x - 5"],
        index=None, key="q34_choice"
    )
    if choice == "5 + 0.75(x - 10)":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_34_solution():
    st.latex(r"\text{Base } \$5\ \text{covers first }10\text{ oz; extras: }(x-10)\text{ oz at } \$0.75")
    st.latex(r"\boxed{5 + 0.75(x-10)}\quad (x>10)")

def question_35():
    st.write("Liz lives 150 miles from her favorite beach. The beach is 200 miles from the nation’s capital.")
    st.write("What are the shortest and longest possible distances from Liz’s residence to the capital?")
    choice = st.radio(
        "Select your answer:",
        ["50 miles, 200 miles", "50 miles, 350 miles", "150 miles, 350 miles", "200 miles, 350 miles"],
        index=None, key="q35_choice"
    )
    if choice == "50 miles, 350 miles":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_35_solution():
    st.latex(r"\text{Shortest: }|200-150|=\boxed{50}\ \text{miles}")
    st.latex(r"\text{Longest: }150+200=\boxed{350}\ \text{miles}")

# ----------------------------
# New questions: Q36 – Q42
# ----------------------------

# ----------------------------
# New questions: Q36 – Q42
# ----------------------------

def question_36():
    st.write("If the radius of a right circular cylinder is doubled, how does its volume change?")
    choice = st.radio(
        "Select your answer:",
        [
            "No change",
            "also is doubled",
            "four times the original",  # ✅
            "pi times the original",
        ],
        index=None, key="q36_choice"
    )
    if choice == "four times the original":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_36_solution():
    st.latex(r"""
    \begin{aligned}
    &V=\pi r^2 h,\quad r\to 2r \\
    &V'=\pi(2r)^2 h = 4\pi r^2 h = 4V \\
    &\text{Answer: four times the original.}
    \end{aligned}
    """)


def question_37():
    st.write("An item that sells for \$375 is put on sale at \$120. What is the percent discount?")
    choice = st.radio(
        "Select your answer:",
        [
            "25%",
            "28%",
            "68%",   # ✅
            "34%",
        ],
        index=None, key="q37_choice"
    )
    if choice == "68%":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_37_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Discount}=375-120=255 \\
    &\text{Percent discount}=\frac{255}{375}=0.68=68\% \\
    &\text{Answer: }68\%.
    \end{aligned}
    """)


def question_38():
    st.write(
        "Kindergarten students paint one half of a folded paper, close and reopen it. "
        "The picture shows matching sides. What math principle does this demonstrate?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "Slide",
            "Rotate",
            "Symmetry",     # ✅
            "Transformation",
        ],
        index=None, key="q38_choice"
    )
    if choice == "Symmetry":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_38_solution():
    st.write(
        "Folding and transferring ink/paint creates a mirror image. "
        "This is **reflectional (line) symmetry**.\n\n**Answer:** Symmetry."
    )


def question_39():
    st.write(
        "Given a drawer with 5 black socks, 3 blue socks, and 2 red socks, what is the probability "
        "that you will draw two black socks in two draws (without replacement) in a dark room?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "2/9",    # ✅
            "1/4",
            "17/18",
            "1/18",
        ],
        index=None, key="q39_choice"
    )
    if choice == "2/9":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_39_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Total socks}=5+3+2=10 \\
    &P(\text{1st black})=\frac{5}{10}=\frac{1}{2},\quad
      P(\text{2nd black}\mid \text{1st black})=\frac{4}{9} \\
    &P(\text{two blacks})=\frac{1}{2}\cdot\frac{4}{9}=\frac{2}{9} \\
    &\text{Answer: } \frac{2}{9}.
    \end{aligned}
    """)


def question_40():
    st.write("A sofa sells for $520. If the retailer makes a 30% profit, what was the wholesale price?")
    choice = st.radio(
        "Select your answer:",
        [
            "$400",   # ✅
            "$676",
            "$490",
            "$364",
        ],
        index=None, key="q40_choice"
    )
    if choice == "$400":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_40_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let wholesale price be } C. \\
    &\text{Retail} = 1.30\,C = 520 \;\Rightarrow\; C=\frac{520}{1.30}=400 \\
    &\text{Answer: } \$400.
    \end{aligned}
    """)


def question_41():
    st.write("Each (x, y) relationship between a pair of values is called the ______ and can be plotted on a graph.")
    choice = st.radio(
        "Select your answer:",
        [
            "Coordinate pair",   # ✅ (a.k.a. ordered pair)
            "parallel value",
            "symbolic rule",
            "proportional function",
        ],
        index=None, key="q41_choice"
    )
    if choice == "Coordinate pair":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_41_solution():
    st.write(
        "A single (x, y) value is an **ordered (coordinate) pair**, which marks a point on the coordinate plane.\n\n"
        "**Answer:** Coordinate pair."
    )


def question_42():
    st.write("In similar polygons, if the perimeters are in a ratio of x:y, the sides are in a ratio of:")

    # Choices (no duplicate display)
    choices = [
        "x:y",       # ✅ correct
        "x²:y²",
        "2x:y",
        "½x:y"
    ]

    # Single radio handles display + selection
    choice = st.radio(
        "Select your answer:",
        choices,
        index=None,
        key="q42_choice"
    )

    if choice == "x:y":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")



def question_42_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{In similar figures, all corresponding \emph{lengths} scale by the same factor.} \\
    &\text{Perimeter is a sum of lengths, so perimeter ratio = side ratio.} \\
    &\text{(Areas would scale as } x^2:y^2\text{.)} \\
    &\text{Answer: } x:y.
    \end{aligned}
    """)

# ----------------------------
# New questions: Q43 – Q48
# ----------------------------

def question_43():
    st.write("The maximum area of a rectangular yard bounded by 42 meters of fencing is:")

    choices = [
        "84 m²",
        "100 m²",
        "110.25 m²",   # ✅ correct
        "126 m²"
    ]

    choice = st.radio(
        "Select your answer:",
        choices,
        index=None,
        key="q43_choice"
    )

    if choice == "110.25 m²":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")



def question_43_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let sides } x,y \ \text{with } 2(x+y)=42 \Rightarrow y=21-x.\\
    &A(x)=xy=x(21-x)=21x-x^2 \ \Rightarrow \ A'(x)=21-2x=0 \Rightarrow x=10.5.\\
    &y=10.5,\quad A_{\max}=10.5\cdot 10.5=110.25\ \text{m}^2.\\
    &\text{(Max at a square for fixed perimeter.)}
    \end{aligned}
    """)


def question_44():
    st.write("Which of the following are possible angle measures of an isosceles triangle?")
    choice = st.radio(
        "Select your answer:",
        [
            "70, 70, 70",
            "65, 65, 50",   # ✅
            "80, 70, 30",
            "55, 55, 60",
        ],
        index=None, key="q44_choice"
    )
    if choice == "65, 65, 50":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_44_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Triangle angle sum }=180^\circ\ \text{and isosceles }\Rightarrow \text{two equal angles.}\\
    &70+70+70=210^\circ\ (\text{invalid});\quad 65+65+50=180^\circ\ (\text{valid, two equal});\\
    &80+70+30=180^\circ\ (\text{no equal angles});\quad 55+55+60=170^\circ\ (\text{invalid}).\\
    &\text{Answer: } 65, 65, 50.
    \end{aligned}
    """)


def question_45():
    st.write("Jane has canaries and ferrets. They are all canaries except 3, and all ferrets except 3. "
             "The total number of pets Jane has is")
    choice = st.radio(
        "Select your answer:",
        [
            "3",
            "5",
            "6",  # ✅
            "8",
        ],
        index=None, key="q45_choice"
    )
    if choice == "6":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_45_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let } C=\#\text{canaries},\ F=\#\text{ferrets}.\\
    &\text{"All are canaries except 3"} \Rightarrow F=3.\\
    &\text{"All are ferrets except 3"} \Rightarrow C=3.\\
    &\text{Total}=C+F=3+3=6.
    \end{aligned}
    """)


def question_46():
    st.write("The cost of a round pizza is directly related to its size. Which pizza would cost more: "
             "one with radius 5 inches or one with circumference 50 inches?")
    choice = st.radio(
        "Select your answer:",
        [
            "Pizza with radius 5 inches",
            "Pizza with circumference 50 inches",  # ✅
            "They cost the same",
            "Not enough information",
        ],
        index=None, key="q46_choice"
    )
    if choice == "Pizza with circumference 50 inches":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_46_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Cost } \propto \text{area} = \pi r^2.\\
    &r_1=5 \Rightarrow A_1=\pi(5)^2=25\pi\approx 78.54.\\
    &C=50 \Rightarrow r_2=\tfrac{C}{2\pi}=\tfrac{50}{2\pi}=\tfrac{25}{\pi}\approx 7.96,\ 
      A_2=\pi r_2^2=\frac{625}{\pi}\approx 198.94.\\
    &A_2>A_1 \Rightarrow \text{circumference-50'' pizza costs more.}
    \end{aligned}
    """)


def question_47():
    st.write("The definition of a parallelogram is")
    choice = st.radio(
        "Select your answer:",
        [
            "A quadrilateral with all 4 sides of equal length",
            "4-sided polygon with exactly 1 pair of parallel sides",
            "4-sided polygon with exactly 2 pairs of parallel sides",  # ✅
            "4-sided polygon having all right angles",
        ],
        index=None, key="q47_choice"
    )
    if choice == "4-sided polygon with exactly 2 pairs of parallel sides":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_47_solution():
    st.write(
        "A parallelogram is a quadrilateral with **both pairs of opposite sides parallel** "
        "(i.e., two pairs of parallel sides). Rectangles, rhombuses, and squares are all parallelograms.\n\n"
        "**Answer:** 4-sided polygon with exactly 2 pairs of parallel sides."
    )


def question_48():
    st.write("Julia has an average of 70 on 3 math tests. The final exam counts as 2 tests. "
             "What score must she get on the final to have an average of 80?")
    choice = st.radio(
        "Select your answer:",
        [
            "85",
            "90",
            "95",  # ✅
            "100",
        ],
        index=None, key="q48_choice"
    )
    if choice == "95":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_48_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Total weight }=3+2=5 \text{ tests}. \\
    &\text{Need total }=80\cdot 5=400. \\
    &\text{Have } 70\cdot 3=210. \\
    &210 + 2x = 400 \Rightarrow 2x=190 \Rightarrow x=95. \\
    &\text{Answer: } 95.
    \end{aligned}
    """)
 # ----------------------------
# New questions: Q49 – Q55
# ----------------------------

def question_49():
    st.write("As the number of sides of a regular polygon increases, the measure of each interior angle …")
    choice = st.radio(
        "Select your answer:",
        [
            "decreases",
            "increases",  # ✅
            "remains the same",
            "alternates between increasing and decreasing",
        ],
        index=None, key="q49_choice"
    )
    if choice == "increases":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_49_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Interior angle of regular } n\text{-gon}:\ \ \theta_n=\frac{(n-2)180^\circ}{n}
      =180^\circ-\frac{360^\circ}{n}.\\
    &\text{As }n\text{ increases, } \frac{360^\circ}{n}\text{ decreases }\Rightarrow \theta_n \text{ increases.}
    \end{aligned}
    """)


def question_50():
    st.write(
        "A train leaves point P for point G at an average speed of 40 mph. A half-hour later, an express train "
        "leaves P at 50 mph. Both arrive at G at the same time. Calculate the distance (miles) between P and G."
    )
    choice = st.radio(
        "Select your answer:",
        [
            "100",  # ✅
            "85",
            "58",
            "92",
        ],
        index=None, key="q50_choice"
    )
    if choice == "100":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_50_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let distance } D. \\
    &\text{Times: slow }=D/40,\ \text{express }=D/50. \\
    &\text{Express leaves }0.5\text{ hr later: } \frac{D}{40}=\frac{D}{50}+0.5. \\
    &\frac{D}{40}-\frac{D}{50}=\frac{D}{200}=0.5 \Rightarrow D=100\ \text{miles}.
    \end{aligned}
    """)


def question_51():
    st.write(
        "Sales tax is 6.25% on the item and its shipping/handling cost. A store has a 10% discount plus $7 shipping/handling. "
        "Which expression gives the total cost T (in dollars) in terms of price P?"
    )

    choices = [
        "P - 0.1P + 0.0625 × 0.9P + 7",
        "0.0625 × 0.9P + 7",
        "(0.9P + 7) × 1.0625",   # ✅ Correct: tax applied after discount + shipping
        "0.0625 × 0.9P - 0.1P"
    ]

    choice = st.radio(
        "Select your answer:",
        choices,
        index=None,
        key="q51_choice"
    )

    if choice == "(0.9P + 7) × 1.0625":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")


def question_51_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Discounted price} = 0.9P. \\
    &\text{Add shipping: } 0.9P + 7. \\
    &\text{Apply sales tax }6.25\% = 0.0625:\ \ T=(0.9P+7)(1+0.0625)=(0.9P+7)\cdot 1.0625.
    \end{aligned}
    """)


def question_52():
    st.write(
        "The statement 'The sum of two different integers is 24, where the larger is twice the smaller minus 3' "
        "is expressed as:"
    )

    choice = st.radio(
        "Select your answer:",
        [
            "x - 2 = 24",
            "(2x - 3) + x = 24",  # ✅
            "3x - 3 = 21",
            "x + 3x = 24",
        ],
        index=None, key="q52_choice"
    )
    if choice == "(2x - 3) + x = 24":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_52_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let the smaller integer be }x,\ \text{so larger }=2x-3. \\
    &\text{Sum }= x + (2x-3) = 24 \ \Longleftrightarrow\ (2x-3)+x=24.
    \end{aligned}
    """)


def question_53():
    st.write("James is 4 times as old as Melissa. The sum of their ages is 40. The age of Melissa is …")
    choice = st.radio(
        "Select your answer:",
        [
            "6",
            "8",   # ✅
            "10",
            "12",
        ],
        index=None, key="q53_choice"
    )
    if choice == "8":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_53_solution():
    st.latex(r"""
    \begin{aligned}
    &\text{Let Melissa }=m,\ \text{James }=4m,\ \ m+4m=40 \Rightarrow 5m=40 \Rightarrow m=8.
    \end{aligned}
    """)


def question_54():
    st.write("The prime factorization of the number 260 is …")
    choice = st.radio(
        "Select your answer:",
        [
            "2² · 5 · 13",  # ✅ (using Unicode superscript for radio display)
            "2 · 5 · 13",
            "2² · 5² · 13",
            "2 · 5² · 13",
        ],
        index=None, key="q54_choice"
    )
    if choice == "2² · 5 · 13":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_54_solution():
    st.latex(r"""
    \begin{aligned}
    &260=26\cdot 10=(2\cdot 13)(2\cdot 5)=2^2\cdot 5 \cdot 13.
    \end{aligned}
    """)


def question_55():
    st.write("The number √5 is")
    choice = st.radio(
        "Select your answer:",
        [
            "irrational",
            "real",
            "a number that cannot be expressed as a ratio of 2 integers",
            "all of the above",  # ✅
        ],
        index=None, key="q55_choice"
    )
    if choice == "all of the above":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_55_solution():
    st.write(
        "√5 is a real number and irrational, i.e., it cannot be written as a ratio of two integers. "
        "**Answer:** all of the above."
    )
   

# =========================
# Q56
# =========================
def question_56():
    st.write(
        "Identify the addition and multiplication properties, in the proper order, "
        "that transform the expression on the left into the one on the right:\n\n"
        r"$2\times(3+4)=(4\times2)+(3\times2)$"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "Distributive followed by commutative of multiplication and then commutative for addition",  # ✅
            "Associative followed by commutative of multiplication and then commutative for addition",
            "Associative followed by distributive property",
            "Commutative of addition followed by commutative of multiplication",
        ],
        index=None, key="q56_choice"
    )
    if choice == "Distributive followed by commutative of multiplication and then commutative for addition":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_56_solution():
    st.write("**Worked-Out Solution (Q56)**")
    st.write(
        r"Start with $2(3+4)$. "
        r"**Distribute**: $2\cdot3 + 2\cdot4$. "
        r"Apply **commutative of multiplication**: $(3\times2) + (4\times)$. "
        r"Apply **commutative of addition** to reorder the sum: $(4\times2) + (3\times2)$."
    )
    st.write("**Answer:** Distributive → commutative (multiplication) → commutative (addition).")


# =========================
# Q57
# =========================
def question_57():
    st.write("What percent of 80 is 12?")
    choice = st.radio(
        "Select your answer:",
        [
            "10%",
            "12%",
            "15%",  # ✅
            "20%",
        ],
        index=None, key="q57_choice"
    )
    if choice == "15%":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_57_solution():
    st.write("**Worked-Out Solution (Q57)**")
    st.write(
        r"We want $p\% \times 80 = 12 \Rightarrow p = \frac{12}{80} = 0.15 = 15\%.$"
    )
    st.write("**Answer:** 15%.")


# =========================
# Q58
# =========================
def question_58():
    st.write(
        "From left to right each number in the sequence is "
        r"$\frac{125}{126},\ \frac{126}{127},\ \frac{128}{129},\ \frac{130}{131},\ \dots$ is"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "Larger than the previous number",  # ✅
            "Same as the previous number",
            "Smaller than the previous number",
            "Smaller than the first number in that sequence",
        ],
        index=None, key="q58_choice"
    )
    if choice == "Larger than the previous number":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")


def question_58_solution():
    st.write("**Worked-Out Solution (Q58)**")
    st.write(
        r"For $n \ge 1$, we can write"
    )
    st.latex(r"\dfrac{n}{n+1} = 1 - \dfrac{1}{n+1}.")
    st.write(
        r"As $n$ increases, $\dfrac{1}{n+1}$ gets smaller, so "
        r"$1 - \dfrac{1}{n+1}$ gets larger. Therefore each successive term "
        r"is larger than the previous one."
    )
    st.write("**Answer:** Larger than the previous number.")




# =========================
# Q59
# =========================


def question_59():
    st.write(
        r"59. The population of a certain country is about $3$ billion $145$ million. "
        r"Which of the following is an appropriate scientific notation for this population?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"$3.145\times 10^8$",
            r"$3.145\times 10^9$",  # ✅
            r"$3.145\times 10^{10}$",
            r"$3.145\times 10^{11}$",
        ],
        index=None,
        key="q59_choice"
    )
    if choice == r"$3.145\times 10^9$":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Think about how many zeros are in 1 billion.")



def question_59_solution():
    st.write("**Worked-Out Solution (Q59)**")
    st.write(
        r"$3$ billion is $3{,}000{,}000{,}000$ and $145$ million is $145{,}000{,}000$. "
        r"Adding gives $3{,}145{,}000{,}000$."
    )
    st.latex(r"3{,}145{,}000{,}000 = 3.145 \times 10^9")
    st.write(r"**Answer**: $3.145 \times 10^9$")



# =========================
# Q60
# =========================
def question_60():
    st.write(
        "Simplify "
        r"$\big[(5\times10^8)\times(12\times10^{-5})\big] \div (3\times10^{-2})$."
    )
    choice = st.radio(
        "Select your answer:",
        [
            "200 million",
            "2 million",   # ✅
            r"$2\times 10^5$",
            "2 billion",
        ],
        index=None, key="q60_choice"
    )
    if choice == "2 million":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_60_solution():
    st.write("**Worked-Out Solution (Q60)**")
    st.write(
        r"Compute coefficients: $\dfrac{5\cdot12}{3}=20$. "
        r"Add exponents: $10^{8+(-5)-(-2)}=10^{5}$. "
        r"So the result is $20\times10^{5}=2.0\times10^{6}=2{,}000{,}000$ (2 million)."
    )
    st.write("**Answer:** 2 million.")


# =========================
# Q61
# =========================
def question_61():
    st.write(
        r"The solution to the equation $\frac{1}{7}x+\frac{1}{21}=\frac{3}{42}x-\frac{2}{42}$ is"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"$\frac{3}{4}$",
            r"$-\frac{3}{4}$",
            r"$\frac{4}{3}$",
            r"$-\frac{4}{3}$",  # ✅
        ],
        index=None, key="q61_choice"
    )
    if choice == r"$-\frac{4}{3}$":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_61_solution():
    st.write("**Worked-Out Solution (Q61)**")
    st.write(
        r"$\frac{x}{7}+\frac{1}{21}=\frac{x}{14}-\frac{1}{21}$."
        r" Multiply both sides by $42$: $6x+2=3x-2 \Rightarrow 3x=-4 \Rightarrow x=-\frac{4}{3}$."
    )
    st.write("**Answer:** $-4/3$")



# =========================
# Q62
# =========================
def question_62():
    st.write("The number 23 is a")
    choice = st.radio(
        "Select your answer:",
        [
            "prime number",
            "real number",
            "odd number",
            "all of the above",  # ✅
        ],
        index=None, key="q62_choice"
    )
    if choice == "all of the above":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_62_solution():
    st.write("**Worked-Out Solution (Q62)**")
    st.write(
        "23 has no positive divisors other than 1 and 23 (*prime*), it lies on the real number line (*real*), "
        "and it is not divisible by 2 (*odd*)."
    )
    st.write("**Answer:** all of the above.")


# =========================
# Q63
# =========================
def question_63():
    # Your prompt already used LaTeX; keep it and leave radio as plain numerals.
    st.markdown(r"The sum of $1 + 2 + 3 + \cdots + 50 $ is")


    choice = st.radio(
        "Select your answer:",
        [
            "1225",
            "1250",
            "1275",  # ✅
            "1300",
        ],
        index=None, key="q63_choice"
    )
    if choice == "1275":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_63_solution():
    st.write("**Worked-Out Solution (Q63)**")
    st.write(
        r"Use the formula for the sum of the first $n$ integers: "
        r"$1+2+\cdots+n=\dfrac{n(n+1)}{2}$. With $n=50$: $\dfrac{50\cdot51}{2}=1275$."
    )
    st.write("**Answer:** 1275.")


# =========================
# Q64
# =========================
def question_64():
    # Use $...$ for math in Streamlit markdown
    st.markdown(r"Solve the inequality $4 - \tfrac{7}{3}x \le 25$. The solution set is:")

    # Radios do not render LaTeX → use Unicode symbols
    choices = [
        "x ≤ -9",
        "x ≥ -9",  # ✅
        "x ≤ 9",
        "x ≥ 9",
    ]

    choice = st.radio(
        "Select your answer:",
        choices,
        index=None,
        key="q64_choice"
    )

    if choice == "x ≥ -9":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")


def question_64_solution():
    st.write("**Worked-Out Solution (Q64)**")
    st.write(
        r"$4-\frac{7}{3}x\le 25 \Rightarrow -\frac{7}{3}x\le 21 \Rightarrow x \ge -9$ "
        r"(inequality reverses when multiplying by a negative)."
    )
    st.write("**Answer:** $x\ge -9$.")



# =========================
# Q65
# =========================
def question_65():
    st.write(
        r"If you replace the graph of $y=2x^2$ by the graph of $y=2x^2+5$, the resulting parabola"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "shifts up 5 units",    # ✅
            "shifts down 5 units",
            "compressed by 3 units",
            "shifts down by 3 units",
        ],
        index=None, key="q65_choice"
    )
    if choice == "shifts up 5 units":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_65_solution():
    st.write("**Worked-Out Solution (Q65)**")
    st.write(
        r"Adding a constant $+5$ to $y=2x^2$ translates the graph **up** by 5 units; "
        r"the shape (opening and width) does not change."
    )
    st.write("**Answer:** shifts up 5 units.")
  
def question_66():
    st.write(
        r"If the $3^\text{rd}$ term of an arithmetic progression is $13$ and the $8^\text{th}$ term is $33$, the $13^\text{th}$ term is"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "45",
            "33",
            "125",
            "53",   # ✅
        ],
        index=None, key="q66_choice"
    )
    if choice == "53":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_66_solution():
    st.write("**Worked-Out Solution (Q66)**")
    st.write(
        r"In an arithmetic sequence $a_n=a_1+(n-1)d$. "
        r"$a_3=a_1+2d=13,\ a_8=a_1+7d=33 \Rightarrow 5d=20 \Rightarrow d=4.$ "
        r"Then $a_1=13-2\cdot4=5$ and $a_{13}=5+12\cdot4=53$."
    )
    st.write("**Answer:** 53.")


def question_67():
    st.write(
        r"A wireless company charges a flat fee of \$32 per month plus 15 cents per call. "
        r"The cost $C$ (dollars) as a function of $N$ calls is"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "C = 32 + N",
            "C = 32 + 0.15N",  # ✅
            "C = 32 + 15N",
            "C = 32N + 15N",
        ],
        index=None, key="q67_choice"
    )
    if choice == "C = 32 + 0.15N":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_67_solution():
    st.write("**Worked-Out Solution (Q67)**")
    st.write(
        r"The fixed part is \$32. Each call adds \$0.15, so the variable part is $0.15N$. "
        r"Thus $C=32+0.15N$."
    )
    st.write("**Answer:** $C=32+0.15N$.") 


def question_68():
    st.write(
        r"The symmetry group of a regular pentagon is"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "5 reflections only",
            "5 rotations only",
            "5 rotations together with 5 reflections",  # ✅
            "10 rotations together with 10 reflections",
        ],
        index=None, key="q68_choice"
    )
    if choice == "5 rotations together with 5 reflections":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_68_solution():
    st.write("**Worked-Out Solution (Q68)**")
    st.write(
        r"A regular $n$-gon has the dihedral symmetry group $D_n$ with $n$ rotations (including the identity) "
        r"and $n$ reflections. For a pentagon ($n=5$), there are $5$ rotations and $5$ reflections."
    )
    st.write("**Answer:** 5 rotations together with 5 reflections.")


def question_69():
    st.write(
        r"The function $f(x)=|x-3|$ is symmetric about the"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "Y-axis",
            "X-axis",
            "origin",
            "line $x=3$",   # ✅
        ],
        index=None, key="q69_choice"
    )
    if choice == "line $x=3$":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_69_solution():
    st.write("**Worked-Out Solution (Q69)**")
    st.write(
        r"$|x-3|$ is the graph of $|x|$ shifted right by $3$, so the axis of symmetry moves from $x=0$ to $x=3$."
    )
    st.write("**Answer:** line $x=3$.") 


def question_70():
    st.write(
        r"Determine a possible fourth vertex of a trapezoid with vertices $(-3,0)$, $(3,0)$, and $(-2,1)$."
    )
    choice = st.radio(
        "Select your answer:",
        [
            "(2, 1)",   # ✅
            "(-2, -1)",
            "(3, 1)",
            "(0, 3)",
        ],
        index=None, key="q70_choice"
    )
    if choice == "(2, 1)":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_70_solution():
    st.write("**Worked-Out Solution (Q70)**")
    st.write(
        r"A trapezoid has exactly one pair of parallel sides. The base through $(-3,0)$ and $(3,0)$ is horizontal ($y=0$). "
        r"To keep one pair of horizontal, choose the top base with the same $y$–value as $(-2,1)$, i.e., $y=1$. "
        r"Taking the fourth vertex as $(2,1)$ gives top base endpoints $(-2,1)$ and $(2,1)$ (length $4$) and bottom base endpoints "
        r"$(-3,0)$ and $(3,0)$ (length $6$), which are parallel and of different lengths—so the figure is a trapezoid."
    )
    st.write("**Answer:** $(2,1)$.")

def question_71():
    st.write(
        r"A flagpole casts a shadow of $6$ meters. A nearby $1$-meter stick casts a shadow of $50$ cm. "
        r"The height of the flagpole is"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "6 m",
            "12 m",   # ✅
            "24 m",
            "18 m",
        ],
        index=None, key="q71_choice"
    )
    if choice == "12 m":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_71_solution():
    st.write("**Worked-Out Solution (Q71)**")
    st.write(
        r"By similar triangles: $\dfrac{\text{height}}{\text{shadow}}=\dfrac{1}{0.5}=2$. "
        r"Flagpole height $=2\times 6=12$ meters."
    )
    st.write("**Answer:** 12 m.")


def question_72():
    st.write(
        r"$46712$ milligrams is equivalent to"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "4.6712 gms",
            "467.12 gms",
            "4671.2 gms",
            "46.712 gms",  # ✅
        ],
        index=None, key="q72_choice"
    )
    if choice == "46.712 gms":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_72_solution():
    st.write("**Worked-Out Solution (Q72)**")
    st.write(
        r"$1\,\text{g} = 1000\,\text{mg}$. Thus $46712\,\text{mg} = 46.712\,\text{g}$."
    )
    st.write("**Answer:** 46.712 gms.")


def question_73():
    st.write(
        r"Compute the sum $235\text{ m} + 20150\text{ mm} + 7.3\text{ km}$ in kilometers."
    )
    choice = st.radio(
        "Select your answer:",
        [
            "298 km",
            "7.55515 km",  # ✅
            "7.7365 km",
            "21.115 km",
        ],
        index=None, key="q73_choice"
    )
    if choice == "7.55515 km":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_73_solution():
    st.write("**Worked-Out Solution (Q73)**")
    st.write(
        r"$235\text{ m}=0.235\text{ km},\quad 20150\text{ mm}=20.15\text{ m}=0.02015\text{ km}.$ "
        r"Total $=7.3+0.235+0.02015=7.55515\text{ km}$."
    )
    st.write("**Answer:** 7.55515 km.")


def question_74():
    st.write(
        r"74. The volume of a cylinder with radius $4$ cm and height $\tfrac{1}{2}$ meter is approximately:"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"$2513\ \text{m}$",
            r"$2513\ \text{m}^3$",
            r"$0.002513\ \text{m}^3$",   # ✅
            r"$2.513\ \text{m}^3$",
        ],
        index=None,
        key="q74_choice"
    )
    if choice == r"$0.002513\ \text{m}^3$":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Remember to convert centimeters to meters before finding volume.")

def question_74_solution():
    st.write("**Worked-Out Solution (Q74)**")
    st.write(
        r"Convert radius to meters: $r = 4\text{ cm} = 0.04\text{ m}$ and $h = 0.5\text{ m}.$" "\n\n"
        r"Then $V = \pi r^2 h = \pi (0.04)^2 (0.5) = \pi (0.0016)(0.5) = 0.0008\pi$." "\n\n"
        r"$0.0008\pi \approx 0.002513\ \text{m}^3.$"
    )
    st.write("**Answer:**", r"$0.002513\ \text{m}^3$")



def question_75():
    st.write(
        r"The probability of rolling a sum of $8$ or $10$ on two fair six-sided dice is"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "2/9",   # ✅
            "5/36",
            "1/4",
            "1/3",
        ],
        index=None, key="q75_choice"
    )
    if choice == "2/9":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_75_solution():
    st.write("**Worked-Out Solution (Q75)**")
    st.write(
        r"Favorable outcomes: sum $8$ has $5$ ways $(2,6),(3,5),(4,4),(5,3),(6,2)$; "
        r"sum $10$ has $3$ ways $(4,6),(5,5),(6,4)$. Total $=8$ out of $36$ equally likely outcomes: "
        r"$\tfrac{8}{36}=\tfrac{2}{9}$."
    )
    st.write("**Answer:** $2/9$.")


def question_76():
    st.write(
        r"How many different license plates can be made if each plate has one letter followed by $5$ numbers?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "260,000",
            "2,600,000",   # ✅
            "26,000,000",
            "260,000,000",
        ],
        index=None, key="q76_choice"
    )
    if choice == "2,600,000":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_76_solution():
    st.write("**Worked-Out Solution (Q76)**")
    st.write(
        r"Assuming $26$ letters (A–Z) and digits $0$–$9$ with repetition allowed: "
        r"$26\times 10^5=26\times 100{,}000=2{,}600{,}000$."
    )
    st.write("**Answer:** 2,600,000.")


def question_77():
    st.write(
        r"Solve for $x$: $4x - (3 - x)= 7(x - 30)+ 10$."
    )
    choice = st.radio(
        "Select your answer:",
        [
            "98.5",   # ✅
            "197",
            "-98.5",
            "100",
        ],
        index=None, key="q77_choice"
    )
    if choice == "98.5":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_77_solution():
    st.write("**Worked-Out Solution (Q77)**")
    st.write(
        r"LHS: $4x-(3-x)=4x-3+x=5x-3$. RHS: $7(x-30)+10=7x-210+10=7x-200$. "
        r"$5x-3=7x-200\Rightarrow 197=2x\Rightarrow x=98.5$."
    )
    st.write("**Answer:** $x=98.5$.")


def question_78():
    st.write(
        r"An item that sells for \$375 is put on sale at \$120. What is the percent decrease?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "32%",
            "68%",   # ✅
            "49%",
            "72%",
        ],
        index=None, key="q78_choice"
    )
    if choice == "68%":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_78_solution():
    st.write("**Worked-Out Solution (Q78)**")
    st.write(
        r"Decrease $=375-120=255$. Percent decrease $=\dfrac{255}{375}\times 100\%=68\%$."
    )
    st.write("**Answer:** 68%.")

def question_79():
    st.write(
        r"If the radius of a right circular cylinder is doubled (height fixed), how does its volume change?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "It doubles (×2)",
            "It triples (×3)",
            "It quadruples (×4)",  # ✅
            "It stays the same",
        ],
        index=None, key="q79_choice"
    )
    if choice == "It quadruples (×4)":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_79_solution():
    st.write("**Worked-Out Solution (Q79)**")
    st.write(
        r"$V=\pi r^2 h$. If $r\mapsto 2r$ (with $h$ fixed), then $V\mapsto \pi(2r)^2h=4\pi r^2h$, i.e., volume multiplies by $4$."
    )
    st.write("**Answer:** It quadruples (×4).")


def question_80():
    st.write(
        r"In similar polygons, if the perimeters are in a ratio $x:y$, the sides are in a ratio of:"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"$x:y$",          # ✅ Correct Answer
            r"$x^2:y^2$",
            r"$2x:y$",
            r"$\tfrac{1}{2}x:y$",
        ],
        index=None, key="q80_choice"
    )
    if choice == r"$x:y$":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_80_solution():
    st.write("**Worked-Out Solution (Q80)**")
    st.write(
        r"For similar polygons, all corresponding **linear measures** (such as side lengths and perimeters) "
        r"scale by the same ratio. So if the perimeters are in the ratio $x:y$, then the corresponding side lengths "
        r"also must be in the ratio $x:y$."
    )
    st.write("**Answer:** $x:y$.")


def question_80_solution():
    st.write("**Worked-Out Solution (Q80)**")
    st.write(
        r"For similar polygons, all corresponding **linear** measures scale by the same factor. "
        r"This means that if the perimeters are in the ratio $x:y$, then each corresponding side is also in the ratio $x:y$ — "
        r"not $x^2:y^2$, which would apply to **areas**, not linear dimensions."
    )
    st.write("**Answer:** $x:y$.")



def question_81():
    st.write(
        r"What measure could be used to report the **distance** traveled walking around a track?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "degrees",
            "square miles",
            "kilometers",   # ✅
            "cubic feet",
        ],
        index=None, key="q81_choice"
    )
    if choice == "kilometers":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_81_solution():
    st.write("**Worked-Out Solution (Q81)**")
    st.write(
        r"Distance is a linear measure, so use units like meters or kilometers (not degrees/area/volume units)."
    )
    st.write("**Answer:** kilometers.")


def question_82():
    st.write(
        r"The mass of a cookie is closest to"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "0.5 kg",
            "0.5 g",
            "15 g",   # ✅
            "1.5 g",
        ],
        index=None, key="q82_choice"
    )
    if choice == "15 g":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_82_solution():
    st.write("**Worked-Out Solution (Q82)**")
    st.write(
        r"Typical cookie mass is on the order of $10$–$30$ grams. $15$ g is reasonable; $0.5$ kg is too large; $0.5$ g or $1.5$ g are too small."
    )
    st.write("**Answer:** 15 g.")


def question_83():
    st.write(
        r"$3\ \text{km}$ is equivalent to"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "300 cm",
            "300 m",
            "3000 cm",
            "3000 m",   # ✅
        ],
        index=None, key="q83_choice"
    )
    if choice == "3000 m":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_83_solution():
    st.write("**Worked-Out Solution (Q83)**")
    st.write(
        r"$1\ \text{km}=1000\ \text{m}$, so $3\ \text{km}=3000\ \text{m}$."
    )
    st.write("**Answer:** 3000 m.")


def question_84():
    st.write(
        r"What is the area of a square whose perimeter is $13$ feet?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"$\dfrac{169}{16}\ \text{ft}^2$",  # ✅
            r"$13\ \text{ft}^2$",
            r"$16\ \text{ft}^2$",
            r"$52\ \text{ft}^2$",
        ],
        index=None, key="q84_choice"
    )
    if choice == r"$\dfrac{169}{16}\ \text{ft}^2$":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_84_solution():
    st.write("**Worked-Out Solution (Q84)**")
    st.write(
        r"Perimeter $P=4s=13\Rightarrow s=\dfrac{13}{4}$. Area $=s^2=\left(\dfrac{13}{4}\right)^2=\dfrac{169}{16}\approx 10.5625\ \text{ft}^2$."
    )
    st.write(r"**Answer:** $\dfrac{169}{16}\ \text{ft}^2$.")


def question_85():
    st.write(
        r"Corporate salaries are: \$24,000, \$24,000, \$26,000, \$28,000, \$30,000, \$20,000. "
        r"Which measure of central tendency is best?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "mean",
            "median",   # ✅
            "mode",
            "no difference",
        ],
        index=None, key="q85_choice"
    )
    if choice == "median":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_85_solution():
    st.write("**Worked-Out Solution (Q85)**")
    st.write(
        r"Salaries are often skewed by high outliers, so the median is typically preferred. "
        r"For this data (sorted: $20,24,24,26,28,30$), median $=\frac{24+26}{2}=25$ (thousand). "
        r"The mean is $\frac{152}{6}\approx 25.33$, close here, but **median** is generally the better choice for salary data."
    )
    st.write("**Answer:** median.")


def question_86():
    st.write(
        r"A drawer has $5$ black socks, $3$ blue socks, and $2$ red socks. "
        r"What is the probability of drawing **two black** socks in two draws **without replacement**?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "1/5",
            "2/9",     # ✅
            "5/18",
            "1/3",
        ],
        index=None, key="q86_choice"
    )
    if choice == "2/9":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_86_solution():
    st.write("**Worked-Out Solution (Q86)**")
    st.write(
        r"Total socks $=10$. $P(\text{BB})=\frac{5}{10}\cdot\frac{4}{9}=\frac{20}{90}=\frac{2}{9}$."
    )
    st.write("**Answer:** 2/9.")

import streamlit as st

# ---------- Q87 ----------
def question_87():
    st.write(r"What is the value of the $7$ in $1.37\times10^{-2}$?")
    choice = st.radio(
        "Select your answer:",
        [
            "7 / 10",
            "7 / 100",
            "7 / 1000",
            "7 / 10,000"  # ✅
        ],
        index=None, key="q87_choice"
    )
    if choice == "7 / 10,000":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_87_solution():
    st.write("**Worked-Out Solution (Q87)**")
    st.write(
        r"$1.37\times10^{-2}=1.37\div100=0.0137.$ "
        r"In the decimal $0.0137$, the $7$ is in the ten-thousandths place "
        r"$\left(\tfrac{1}{10000}\right)$, so its value is $\tfrac{7}{10000}$."
    )
    st.write("**Answer:** " + r"$\dfrac{7}{10000}$.")


# ---------- Q88 ----------
def question_88():
    st.write(r"Which statement best describes $1\frac14\times1\frac13$?")
    choice = st.radio(
        "Select your answer:",
        [
            "There are 1¼ lbs of clay and we want an equal share for 3 people.",
            "Each of 3 people has 1¼ lbs of clay; find the total.",
            "There are 1¼ lbs of clay and we want ⅓ more than that amount.",  # ✅
            "There are 1¼ lbs of clay and we want to remove clay to make ⅓ lb.",
        ],
        index=None, key="q88_choice"
    )
    if choice == "There are 1¼ lbs of clay and we want ⅓ more than that amount.":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_88_solution():
    st.write("**Worked-Out Solution (Q88)**")
    st.write(
        r"$1\frac14\times1\frac13=(1+\tfrac14)\times(1+\tfrac13)$. "
        r"This multiplies the amount $1\frac14$ by $1+\tfrac13$, "
        r"which means finding **one-third more** than that amount."
    )
    st.write("**Answer:** There are 1¼ lbs of clay and we want ⅓ more than that amount.")


# ---------- Q89 ----------
def question_89():
    st.write(
        "Two elevators start at the 1st floor. One stops every x floors; "
        "the other every 7 floors. What’s the best way to find floors both stop at?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "Find the common multiples of x and 7.",  # ✅
            "Find the common factors of x and 7.",
            "Find the prime factors of x and 7.",
            "Find the divisors of x and 7.",
        ],
        index=None, key="q89_choice"
    )
    if choice == "Find the common multiples of x and 7.":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_89_solution():
    st.write("**Worked-Out Solution (Q89)**")
    st.write(
        r"The first elevator stops on $\{x,2x,3x,\dots\}$ and the second on $\{7,14,21,\dots\}$. "
        r"Common stops occur at **common multiples** of $x$ and $7$; "
        r"the first shared stop is $\operatorname{LCM}(x,7)$."
    )
    st.write("**Answer:** Find the common multiples of $x$ and $7$.")



# ---------- Q90 ----------
def question_90():
    st.write(
        r"A landscaper mixes $3\tfrac{1}{2}$ lbs of rye per $\tfrac{3}{4}$ lb of bluegrass. "
        r"If $5\tfrac{1}{4}$ lbs of rye are needed, how many lbs of bluegrass are needed?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"$\tfrac{3}{4}$ lb",
            r"$1$ lb",
            r"$1\tfrac{1}{8}$ lb",  # ✅
            r"$1\tfrac{1}{2}$ lb",
        ],
        index=None, key="q90_choice"
    )
    if choice == r"$1\tfrac{1}{8}$ lb":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")


def question_90_solution():
    st.write("**Worked-Out Solution (Q90)**")
    st.write(
        r"Ratio $\frac{\text{rye}}{\text{blue}}=\frac{3.5}{0.75}=\frac{14}{3}$. "
        r"For $5\frac14=5.25$ lbs of rye:"
    )
    st.latex(r"\text{blue}=\frac{5.25\times3}{14}=\frac{15.75}{14}=1.125=1\dfrac18\text{ lb.}")
    st.write("**Answer:** " + r"$1\dfrac18$ lb.")


# ---------- Q91 ----------
def question_91():
    st.write("Point (2, −3) is on a line with slope −1. Which other point lies on that line?")
    choice = st.radio(
        "Select your answer:",
        ["(4, 5)", "(4, −5)", "(-4, 5)", "(-4, −5)"], index=None, key="q91_choice"
    )
    if choice == "(4, −5)":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_91_solution():
    st.write("**Worked-Out Solution (Q91)**")
    st.write(
        r"Using point–slope form: $y+3=-1(x-2)\Rightarrow y=-x-1.$ "
        r"Substitute $x=4$: $y=-4-1=-5.$ Hence point (4, −5) is on the line."
    )
    st.write("**Answer:** (4, −5).")


# ---------- Q92 ----------
def question_92():
    st.write(
        "A phone plan costs $0.29$ per call plus $0.04$ per minute m. "
        "Which expression gives the total cost?")
    choice = st.radio(
        "Select your answer:",
        ["0.29 + 0.04", "0.04 m + 0.29", "0.29 m + 0.04", "m (0.29 + 0.04)"],
        index=None, key="q92_choice"
    )
    if choice == "0.04 m + 0.29":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")


def question_92_solution():
    st.write("**Worked-Out Solution (Q92)**")
    st.write(
        r"Total cost = fixed charge $0.29$ + variable charge $0.04m$. "
        r"Therefore $C=0.04m+0.29$."
    )
    st.write("**Answer:** 0.04 m + 0.29.")


# ---------- Q93 ----------
def question_93():
    st.write("An even number is the product of two prime factors. Which could it be?")
    choice = st.radio(
        "Select your answer:",
        ["6", "12", "36", "48"], index=None, key="q93_choice"
    )
    if choice == "6":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_93_solution():
    st.write("**Worked-Out Solution (Q93)**")
    st.write(
        r"A number with exactly two prime factors = $2\times p$ where $p$ is prime. "
        r"$6=2\times3$ fits; others have repeated primes."
    )
    st.write("**Answer:** 6.")


# ---------- Q94 ----------
def question_94():
    st.write(
        "A car travels 45 mph. Map scale 1 in = 10 mi. How long is the map line for 90 min of travel?"
    )
    choice = st.radio(
        "Select your answer:",
        ["4.5 in", "6.75 in", "9 in", "13.5 in"], index=None, key="q94_choice"
    )
    if choice == "6.75 in":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_94_solution():
    st.write("**Worked-Out Solution (Q94)**")
    st.write(
        r"$90$ min = $1.5$ h. Distance $=45\times1.5=67.5$ mi. "
        r"Map length $=\frac{67.5}{10}=6.75$ in."
    )
    st.write("**Answer:** 6.75 in.")


# ---------- Q95 ----------
def question_95():
    st.write(
        r"95. A fair penny is flipped three times and lands heads each time. "
        r"What is the probability it lands heads on the next flip?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "0",
            "1 / 2",   # ✅ Correct
            "3 / 4",
            "1",
        ],
        index=None,
        key="q95_choice"
    )

    if choice == "1 / 2":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_95_solution():
    st.write("**Worked-Out Solution (Q95)**")
    st.write(
        r"Each coin flip is an independent event. "
        r"Previous outcomes do not affect the next result. "
        r"The probability of heads on any single flip is therefore $1/2$, "
        r"no matter what happened before."
    )
    st.write("**Answer:** 1 / 2")



# ---------- Q96 ----------
def question_96():
    st.write(
        "An item costs $83.00. What is the sale price after a 35% discount?"
    )
    choice = st.radio(
        "Select your answer:",
        ["$53.95", "$54.45", "$55.95", "$57.75"], index=None, key="q96_choice"
    )
    if choice == "$53.95":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_96_solution():
    st.write("**Worked-Out Solution (Q96)**")
    st.write(
        r"The sale price is given by multiplying the original price by $(1 - \text{discount rate})$." "\n\n"
        r"$\text{Sale Price} = 83(1 - 0.35) = 83(0.65) = 53.95.$" "\n\n"
        r"Therefore, after a 35\% discount, the price per item is **\$53.95**."
    )
    st.write("**Answer:** \$53.95.")



# ---------- Q97 ----------
def question_97():
    st.write(
        "A truck pumps 100 gal/hr and fills a tank in 3 h. "
        "How long would another truck pumping 60 gal/hr take?"
    )
    choice = st.radio(
        "Select your answer:",
        ["3 h", "4 h", "5 h", "6 h"], index=None, key="q97_choice"
    )
    if choice == "5 h":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_97_solution():
    st.write("**Worked-Out Solution (Q97)**")
    st.write(
        r"Tank volume $=100\times3=300$ gal. At 60 gal/hr: time $=\frac{300}{60}=5$ h."
    )
    st.write("**Answer:** 5 h.")


# ---------- Q98 ----------
def question_98():
    st.write(
        r"98. A baker made brownies and cookies in a ratio of $2 : 9$. "
        r"If $1250$ cookies were made, how many brownies were made?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"275",
            r"278",
            r"280",
            "Not possible with whole numbers",  # ✅
        ],
        index=None,
        key="q98_choice"
    )
    if choice == "Not possible with whole numbers":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. The ratio $2:9$ gives a non-integer result when cookies = 1250.")

def question_98_solution():
    st.write("**Worked-Out Solution (Q98)**")
    st.write(
        r"Let the common factor be $k$. Then brownies $= 2k$ and cookies $= 9k$." "\n"
        r"Given $9k = 1250$, we find $k = \tfrac{1250}{9} \approx 138.89$." "\n"
        r"Then brownies $= 2k = \tfrac{2500}{9} \approx 277.78.$" "\n"
        r"Because brownies must be counted in whole numbers and 1250 is not a multiple of 9, "
        r"the result cannot be a whole number."
    )
    st.write(r"**Answer:** Not possible with whole numbers.")




# ---------------------------
# Question 99
# ---------------------------
def question_99():
    st.write(
        r"**99.** The disaster relief specialist found that 289, or 85 percent, "
        r"of the houses on the beach had been damaged by Hurricane Sandy. "
        r"How many houses were on the beach?"
    )
    choice = st.radio(
        "Select your answer:",
        ["320", "340", "360", "380"],  # ✅ 340
        index=None, key="q99_choice"
    )
    if choice == "340":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_99_solution():
    st.write("**Worked-Out Solution (Q99)**")
    st.write(
        r"Let the total number of houses be $x$.  Then $0.85x = 289$, so "
        r"$x = \frac{289}{0.85} = 340$."
    )

# ---------------------------
# Question 100
# ---------------------------
def question_100():
    st.write(
        r"**100.** After a discount of 25 percent, the savings for a pair of inline skates is \$12.00. "
        r"What is the sale price?"
    )
    choice = st.radio(
        "Select your answer:",
        ["$24", "$36", "$48", "$60"],  # ✅ $36
        index=None, key="q100_choice"
    )
    if choice == "$36":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_100_solution():
    st.write("**Worked-Out Solution (Q100)**")
    st.write(
        r"If a 25% discount equals \$12, then the original price is "
        r"$\dfrac{12}{0.25} = 48$." "\n\n"
        r"The sale price is $48 - 12 = 36$, so the discounted price is **\$36**."
    )
    st.write("**Answer:** \$36.")


# ---------------------------
# Question 101
# ---------------------------
def question_101():
    st.write(
        r"**101.** The class kept track of rainy and sunny days.  "
        r"During the 54 days classified rainy or sunny, the ratio of rainy days to sunny days is 7 to 14.  "
        r"How many sunny days were there?"
    )
    choice = st.radio(
        "Select your answer:",
        ["18", "27", "36", "42"],  # ✅ 36
        index=None, key="q101_choice"
    )
    if choice == "36":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_101_solution():
    st.write("**Worked-Out Solution (Q101)**")
    st.write(
        r"The ratio $7:14$ means $7 + 14 = 21$ parts total.  "
        r"Each part is $\frac{54}{21} = 2.57$ days.  "
        r"Sunny days = $14 \times 2.57 = 36$ days."
    )

# ---------------------------
# Question 102
# ---------------------------
def question_102():
    st.write(
        r"**102.** Serena is an account executive. She receives a base pay of \$18 an hour plus "
        r"a 15 percent bonus for the sales she generates.  Last week she generated \$1200 worth of sales.  "
        r"What is the minimum number of hours she could have worked to make \$500?"
    )
    choice = st.radio(
        "Select your answer:",
        ["22", "18", "26", "28"],  # ✅ 18
        index=None, key="q102_choice"
    )
    if choice == "18":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_102_solution():
    st.write("**Worked-Out Solution (Q102)**")
    st.write(
        r"Bonus = $0.15 \times 1200 = 180$." "\n\n"
        r"Let hours $= h$. Then total pay is given by "
        r"$18h + 180 = 500$." "\n\n"
        r"Solving for $h$: $18h = 320 \Rightarrow h = 17.78.$" "\n\n"
        r"Since hours must be whole, she must have worked **at least 18 hours** "
        r"(since $18$ hours gives \$504)."
    )
    st.write("**Answer:** 18 hours.")


# ---------------------------
# Question 103
# ---------------------------
def question_103():
    st.write(
        r"**103.** At sea level, sound travels about 34,000 centimeters per second, "
        r"while light travels almost instantaneously.  You see a lightning bolt, and five seconds later you hear the thunder.  "
        r"What is the best estimate of how far away the lightning bolt was using scientific notation?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"$1.7\times10^4$ cm",
            r"$1.7\times10^5$ cm",  # ✅
            r"$1.7\times10^6$ cm",
            r"$0.017\times10^7$ cm",
        ],
        index=None, key="q103_choice"
    )
    if choice == r"$1.7\times10^5$ cm":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_103_solution():
    st.write("**Worked-Out Solution (Q103)**")
    st.write(
        r"Distance = speed × time = $34{,}000 \times 5 = 170{,}000$ cm = $1.7\times10^5$ cm."
    )

# ---------------------------
# Question 104
# ---------------------------
def question_104():
    st.write(
        r"**104.** As part of a manufacturing process, two spheres, each with a radius of 3 cm, are dipped into water.  "
        r"Engineers use the product of the water displaced as part of their calculations.  "
        r"What is the formula for the product of the water displaced by two identical spheres? "
        r"(Volume of a sphere = $\frac{4}{3}\pi r^3$)"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"$9\pi^2r^6$",
            r"$\frac{16}{9}\pi^2r^5$",
            r"$\frac{16}{9}\pi^2r^6$",  # ✅
            r"$48\pi^2r^5$",
        ],
        index=None, key="q104_choice"
    )
    if choice == r"$\frac{16}{9}\pi^2r^6$":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_104_solution():
    st.write("**Worked-Out Solution (Q104)**")
    st.write(
        r"Each sphere displaces $\frac{4}{3}\pi r^3$.  "
        r"The product is $\left(\frac{4}{3}\pi r^3\right)\left(\frac{4}{3}\pi r^3\right) "
        r"= \frac{16}{9}\pi^2r^6$."
    )

# ---------------------------
# Question 105
# ---------------------------
def question_105():
    st.write(
        r"**105.** A mathematical relationship is represented by this expression: $3\sqrt{7a}$.  "
        r"How is this expression best represented using fractional exponents?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"$3^{1/3}\cdot7a^{1/2}$",
            r"$3(7^{1/2}\cdot a^{1/2})$",  # ✅
            r"$(21a)^{1/2}$",
            r"$(3\cdot7a^{1/2})^{1/2}$",
        ],
        index=None, key="q105_choice"
    )
    if choice == r"$3(7^{1/2}\cdot a^{1/2})$":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_105_solution():
    st.write("**Worked-Out Solution (Q105)**")
    st.write(
        r"$\sqrt{7a} = 7^{1/2}a^{1/2}$, so the expression equals $3(7^{1/2}a^{1/2})$."
    )

# ---------------------------
# Question 106
# ---------------------------
def question_106():
    st.write(
        r"**106.** Cubes one centimeter on a side are used to form a square pyramid shape.  "
        r"The bottom square on the pyramid measures six cubes on a side.  "
        r"The top of the pyramid shape has a single centimeter cube.  "
        r"How many centimeter cubes are used to make the pyramid?"
    )
    choice = st.radio(
        "Select your answer:",
        ["81", "91", "100", "216"],  # ✅ 91
        index=None, key="q106_choice"
    )
    if choice == "91":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_106_solution():
    st.write("**Worked-Out Solution (Q106)**")
    st.write(
        r"The pyramid has layers with $6^2, 5^2, 4^2, 3^2, 2^2, 1^2$ cubes.  "
        r"Sum = $36 + 25 + 16 + 9 + 4 + 1 = 91$ cubes."
    )

# ---------------------------
# Question 107
# ---------------------------
def question_107():
    st.write(
        r"**107.** Triangle ABC is an equilateral triangle.  The length of side AB is 40 cm.  "
        r"What is the measure of angle B?"
    )
    choice = st.radio(
        "Select your answer:",
        ["30°", "45°", "60°", "90°"],  # ✅ 60°
        index=None, key="q107_choice"
    )
    if choice == "60°":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_107_solution():
    st.write("**Worked-Out Solution (Q107)**")
    st.write(
        r"All interior angles of an equilateral triangle measure $60^\circ$."
    )

# ---------------------------
# Question 108
# ---------------------------
def question_108():
    st.write(
        r"**108.** Translate $\triangle ABC$ with vertices $A(-6,-2)$, $B(-4,2)$, $C(-2,-2)$ "
        r"to $\triangle DEF$ with vertex $D(2,1)$.  What are the coordinates of point $E$?"
    )
    choice = st.radio(
        "Select your answer:",
        ["(3,4)", "(3,5)", "(4,5)", "(5,5)"],  # ✅ (4,4)
        index=None, key="q108_choice"
    )
    if choice == "(4,5)":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_108_solution():
    st.write("**Worked-Out Solution (Q108)**")
    st.write(
        r"Translation vector = $D - A = (2 - (-6), 1 - (-2)) = (8, 3)$.  "
        r"Then $E = B + (8,3) = (-4 + 8, 2 + 3) = (4, 5)$."
        r"the correct translation by $(8,3)$ gives $(4,5)$."
    )

# ---------------------------
# Question 109
# ---------------------------
def question_109():
    st.write(
        r"**109.** The area of a garden is 12 square yards.  How many square feet is that?"
    )
    choice = st.radio(
        "Select your answer:",
        ["27", "36", "81", "108"],  # ✅ 108
        index=None, key="q109_choice"
    )
    if choice == "108":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_109_solution():
    st.write("**Worked-Out Solution (Q109)**")
    st.write(
        r"$1$ yard = $3$ feet, so $1$ square yard = $3^2 = 9$ square feet.  "
        r"$12$ square yards = $12\times9 = 108$ square feet."
    )

# ---------------------------
# Question 110
# ---------------------------
def question_110():
    st.write(
        r"**110.** There are 9 toll booths at a toll plaza. In 1 hour, the mode of the number of cars passing "
        r"through a toll booth is 86, the median is 97, and the range is 108.  "
        r"From this information we can tell that:"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "at least 6 toll booths have fewer than 97 cars passing through.",
            "the toll booth with the most cars had at least 108 cars pass through.",  # ✅
            "most toll booths had more than 86 cars pass through.",
            "most toll booths had 86 cars pass through."
        ],
        index=None, key="q110_choice"
    )
    if choice == "the toll booth with the most cars had at least 108 cars pass through.":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_110_solution():
    st.write("**Worked-Out Solution (Q110)**")
    st.write(
        r"Range = maximum − minimum = 108, so the booth with the most cars had at least "
        r"$\text{min} + 108$ cars.  Thus it had **at least 108** cars pass through."
    )

# ---------------------------
# Question 111
# ---------------------------
def question_111():
    st.write(
        r"**111.** The points $(-4,3)$ and $(4,-3)$ are plotted on a coordinate grid.  "
        r"At what point would a line connecting these two points cross the y-axis?"
    )
    choice = st.radio(
        "Select your answer:",
        ["(0,0)", "(0,1)", "(0,-1)", "(0,3)"],  # ✅ (0,0)
        index=None, key="q111_choice"
    )
    if choice == "(0,0)":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_111_solution():
    st.write("**Worked-Out Solution (Q111)**")
    st.write(
        r"Slope $m = \frac{-3 - 3}{4 - (-4)} = -\frac{6}{8} = -\frac{3}{4}$.  "
        r"Equation: $y - 3 = -\frac{3}{4}(x + 4)$ → $y = -\frac{3}{4}x$.  "
        r"At $x = 0$, $y = 0$.  So the line crosses at $(0,0)$."
    )

# ---------------------------
# Question 112
# ---------------------------
def question_112():
    st.write(
        r"**112.** Light travels about 186,000 miles in one second.  "
        r"Which of the following choices shows how to find how far light travels in an hour?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "Multiply 186,000 by 24",
            "Multiply 186,000 by 60",
            "Multiply 186,000 by 360",
            "Multiply 186,000 by 3600",  # ✅
        ],
        index=None, key="q112_choice"
    )
    if choice == "Multiply 186,000 by 3600":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Try again.")

def question_112_solution():
    st.write("**Worked-Out Solution (Q112)**")
    st.write(
        r"There are 60 seconds per minute and 60 minutes per hour, or $60\times60=3600$ seconds per hour.  "
        r"So multiply $186{,}000\times3600$ to get the distance light travels in an hour."
    )

import streamlit as st

def question_113():
    st.write(
        r"113. A hummingbird can beat its wings about 75 times per second. "
        r"Which expression shows how to find how many times it beats its wings in 5 minutes?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"75 × 5",
            r"75 × 60",
            r"75 × 300",   # ✅
            r"75 × 3600",
        ],
        index=None,
        key="q113_choice"
    )
    if choice == r"75 × 300":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error(
            "❌ Incorrect. Convert 5 minutes to seconds first: "
            "5 × 60 = 300 seconds."
        )


def question_113_solution():
    st.write("**Worked-Out Solution (Q113)**")
    st.write(
        r"A hummingbird beats its wings 75 times every second. "
        r"To find how many beats occur in 5 minutes, convert 5 minutes into seconds: "
        r"$5 \times 60 = 300$ seconds. "
        r"Then multiply $75 \times 300$ to get the total number of wingbeats."
    )



def question_114():
    st.write(
        r"114. The third person (T) in line is taller than the first person. "
        r"The first person (F) is the same height or smaller than the second person (S). "
        r"Using the letters F, S, and T, which of the following choices best represents the height order "
        r"of these three people?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"$F > S > T$",
            r"$F \ge S > T$",
            r"$S > T \ge F$",
            r"$T > F \le S$",  # ✅
        ],
        index=None,
        key="q114_choice"
    )
    if choice == r"$T > F \le S$":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Translate each statement carefully into inequalities.")

def question_114_solution():
    st.write("**Worked-Out Solution (Q114)**")
    st.write(
        r"The statements are:" "\n"
        r"- $T$ is taller than $F$: so $T > F$." "\n"
        r"- $F$ is the same height or smaller than $S$: so $F \le S$." "\n"
        r"Choice (d) writes exactly $T > F \le S$, which encodes both conditions directly. "
        r"Other options contradict at least one of the given relationships."
    )



def question_115():
    st.write(
        "115. Which of the following is the LEAST appropriate mathematics objective "
        "to teach using manipulative materials?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            "Adding single-digit numbers",
            'Solving problems using the strategy "make an organized list"',  # ✅
            "Adding double-digit decimals",
            "Dividing decimals",
        ],
        index=None,
        key="q115_choice"
    )
    if choice == 'Solving problems using the strategy "make an organized list"':
        st.success("✅ Correct!")
    elif choice is not None:
        st.error(
            "❌ Incorrect. Think about which goal is more about problem-solving "
            "strategy than concrete quantity representation."
        )

def question_115_solution():
    st.write("**Worked-Out Solution (Q115)**")
    st.write(
        "Manipulatives are especially effective for representing numerical quantities and place value, "
        "such as adding single digits, operating with decimals, or modeling division. "
        "The objective “make an organized list” is a problem-solving and reasoning strategy, "
        "not primarily about concrete quantity representation. Thus, "
        'Solving problems using the strategy "make an organized list" is the least appropriate for manipulatives.'
    )



def question_116():
    st.write(
        r"116. A teacher is helping young students learn about counting. The teacher uses shapes as counters "
        r"and makes sure students point to a shape each time they say the next numeral. "
        r"Why is the teacher using this approach?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"The teacher wants to be sure the students are paying attention to what they are doing.",
            r"The teacher wants to be sure students are developing eye-hand coordination.",
            r"The teacher is going to ask the students questions about the shapes once they are finished counting.",
            r"The teacher wants to be sure the students are not just saying counting words.",  # ✅
        ],
        index=None,
        key="q116_choice"
    )
    if choice == r"The teacher wants to be sure the students are not just saying counting words.":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Think about 1-to-1 correspondence in early counting.")

def question_116_solution():
    st.write("**Worked-Out Solution (Q116)**")
    st.write(
        r"In early counting, students must develop one-to-one correspondence: each counting word "
        r"matches exactly one object. By having students point to each shape as they say the next number, "
        r"the teacher ensures they are truly counting objects, not simply reciting the number sequence. "
        r"Therefore, the best explanation is that the teacher wants to be sure students are not just saying counting words."
    )


def question_117():
    st.write(
        r"117. How many inches are in 32 kilometers given the following conversions:"
        r" 1 kilometer = 0.62137 miles; 1 mile = 5280 feet; 1 foot = 12 inches?"
    )
    choice = st.radio(
        "Select your answer:",
        [
            r"About 125,984 inches",
            r"About 1,259,840 inches",  # ✅
            r"About 12,598,400 inches",
            r"About 125,984,000 inches",
        ],
        index=None,
        key="q117_choice"
    )
    if choice == r"About 1,259,840 inches":
        st.success("✅ Correct!")
    elif choice is not None:
        st.error("❌ Incorrect. Carefully apply each conversion factor step by step.")
        
def question_117_solution():
    st.write("**Worked-Out Solution (Q117)**")
    st.write(
        r"Use unit conversions step by step:" "\n"
        r"$32\ \text{km} \times 0.62137\ \dfrac{\text{miles}}{\text{km}}"
        r"= 19.88384\ \text{miles}$ (approximately)." "\n"
        r"$19.88384\ \text{miles} \times 5280\ \dfrac{\text{ft}}{\text{mile}}"
        r" \approx 104{,}986.6752\ \text{ft}.$" "\n"
        r"$104{,}986.6752\ \text{ft} \times 12\ \dfrac{\text{in}}{\text{ft}}"
        r" \approx 1{,}259{,}840.1\ \text{inches}.$" "\n"
        r"So $32$ kilometers is approximately $1{,}259{,}840$ inches."
    )

def question_118():
    st.write(
        r"118. **Written Response Question**" "\n\n"
        r"A 4th grade student was asked to solve $450 - 398$ in two different ways."
    )

    st.write(
        r"**(a) Correct reasoning:** The student drew a number line and explained that "
        r"$450 - 400 = 50$ should be two less than $450 - 398$ because 398 is two numbers "
        r"further away from 450 than 400 is on the number line. Therefore, $450 - 398 = 50 + 2 = 52.$"
    )

    st.write(
        r"**(b) Incorrect reasoning:** The student said that the following two subtraction "
        r"problems should have the same answer but didn’t understand why they didn’t get 52 "
        r"from the second equation: $450 - 398 = 448 - 400 = 48.$"
    )

    st.write(
        r"You are asked to explain the mathematical ideas the student *understood* in part (a), "
        r"the ones they *did not yet understand* in part (b), and how you would help them understand "
        r"their mistake in (b)."
    )

def question_118_solution():
    st.write("**Worked-Out Solution (Q118)**")
    st.write(
        r"In (a), the student demonstrates a strong understanding of **number sense** and **relative "
        r"distance on a number line**. They recognize that subtraction can be interpreted as finding "
        r"the difference between two numbers (a *measurement* or *distance* model of subtraction*). "
        r"They also understand that decreasing the subtrahend (the number being subtracted) increases "
        r"the difference, so if $450 - 400 = 50$, then $450 - 398$ must be two more, or 52."
    )
    st.write(
        r"In (b), the student’s reasoning breaks down because they no longer keep both numbers in the "
        r"same relative relationship. They subtracted 2 from **both** the minuend and the subtrahend, "
        r"forming $448 - 400$, but didn’t recognize that subtracting the same amount from both numbers "
        r"does *not* keep the difference the same. Adding or subtracting the same amount from only one "
        r"of the numbers changes the difference, but doing so to both cancels out. The difference remains "
        r"unchanged only if you add or subtract the same number from *both* the minuend and subtrahend "
        r"in the same direction: $(a - b) = ((a - k) - (b - k))$."
    )
    st.write(
        r"To help the student, I would use a **number line** or **base-ten blocks** to show that when "
        r"both numbers move together by the same amount, their distance apart stays constant. "
        r"For instance, shifting both 450 and 398 down by 2 gives 448 and 396, whose difference is "
        r"still 52. But changing only one number changes that distance. This helps the student see "
        r"the **invariance of differences** when both numbers are adjusted equally—a key idea in "
        r"understanding subtraction as distance rather than ‘take away.’"
    )
    st.write(
        r"Mathematically, the student in (a) grasps the *compensation strategy* and relative magnitude, "
        r"while in (b) they confuse the effect of changing both terms. The teacher should emphasize "
        r"equivalence transformations and invariance of differences using concrete models and number-line "
        r"visuals to solidify this concept."
    )




def run_quiz():
    # Call all 70 questions in order
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
    question_31()
    question_32()
    question_33()
    question_34()
    question_35()
    question_36()
    question_37()
    question_38()
    question_39()
    question_40()
    question_41()
    question_42()
    question_43()
    question_44()
    question_45()
    question_46()
    question_47()
    question_48()
    question_49()
    question_50()
    question_51()
    question_52()
    question_53()
    question_54()
    question_55()
    question_56()
    question_57()
    question_58()
    question_59()
    question_60()
    question_61()
    question_62()
    question_63()
    question_64()
    question_65()
    question_66()
    question_67()
    question_68()
    question_69()
    question_70()
    question_71()
    question_72()
    question_73()
    question_74()
    question_75()
    question_76()
    question_77()
    question_78()
    question_79()
    question_80()
    question_81()
    question_82()
    question_83()
    question_84()
    question_85()
    question_86()
    question_87()
    question_88()
    question_89()
    question_90()
    question_91()
    question_92()
    question_93()
    question_94()
    question_95()
    question_96()
    question_97()
    question_98()
    question_99()
    question_100()
    question_101()
    question_102()
    question_103()
    question_104()
    question_105()
    question_106()
    question_107()
    question_108()
    question_109()
    question_110()
    question_111()
    question_112()
    question_113()
    question_114()
    question_115()
    question_116()
    question_117()
    question_118()
   