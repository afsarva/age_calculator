import streamlit as st

# Define age options within the desired range (35 to 200)
age_options = range(35, 201)  # List of ages from 35 to 200
age_options2 = range(0, 201)  # List of ages from 0 to 200

# Session state variable to track button click
if 'submitted' not in st.session_state:
  st.session_state['submitted'] = False

st.title("Age Calculator")

# User input fields
age1 = st.selectbox("**Enter your father age**", age_options)
age2 = st.selectbox("**Enter your mother age**", age_options)
user_age = st.selectbox("**Enter your age**", age_options2)

# Submit button and progress bar
submitted = st.button("**Calculate**", key="submit_button")
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
