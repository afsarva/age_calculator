import streamlit as st

# Session state variable to track button click
if 'submitted' not in st.session_state:
  st.session_state['submitted'] = False

st.title("Find your Age")

# User input fields
age1 = st.number_input("**Enter your father age**", step=1)
age2 = st.number_input("**Enter your mother age**", step=1)
user_age = st.number_input("**Enter your age**", step=0.5)

# Submit button and progress bar
submitted = st.button("**Find**", key="submit_button")
if submitted:
  st.session_state['submitted'] = True
  with st.empty():
    for i in range(101):
      st.progress(i)  # Update progress bar
      if i == 100:  # Simulate calculation completion after reaching 100%
        st.success(f"**Your age is: {user_age}**")  # Display user_age as result
        st.session_state['submitted'] = False  # Reset button state

# Hide progress bar if button not clicked
if not st.session_state['submitted']:
  st.empty()
