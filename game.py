import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize the secret number in session state
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)

if "message" not in st.session_state:
    st.session_state.message = ""

st.write("I'm thinking of a number between **1 and 100**. Try to guess it!")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    if guess < st.session_state.secret:
        st.session_state.message = "⬇️ Too low! Try a higher number."
    elif guess > st.session_state.secret:
        st.session_state.message = "⬆️ Too high! Try a lower number."
    else:
        st.session_state.message = "🎉 Correct! You guessed the number!"
        
    st.experimental_rerun()

st.write(st.session_state.message)

# Reset button
if st.button("Restart Game"):
    st.session_state.secret = random.randint(1, 100)
    st.session_state.message = ""
    st.experimental_rerun()
