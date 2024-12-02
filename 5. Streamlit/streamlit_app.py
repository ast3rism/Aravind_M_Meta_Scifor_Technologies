import streamlit as st
import random

def game():
    st.title("Rock, Paper, Scissors")

    user_choice = st.selectbox("Choose your move:", ["Rock", "Paper", "Scissors"])

    if st.button("Play"):
        comp_choice = random.choice(["Rock", "Paper", "Scissors"])

        st.write(f"You chose: {user_choice}")
        st.write(f"Computer chose: {comp_choice}")

        if user_choice == comp_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = "You win!"
            st.balloons()
        else:
            result = "Computer wins!"

        st.write(result)

if __name__ == '__main__':
    game()
