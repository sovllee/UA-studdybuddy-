import pickle
import streamlit_authenticator as stauth
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title='Study Buddy',
    page_icon=':couple:'
)

names = ['Peter Parker', 'Rebecca Miller']
usernames = ['p', 'r']
passwords = ['abc123', 'def456']

# Create a Hasher instance and generate the hashed passwords
hasher = stauth.Hasher(passwords)
hashed_passwords = hasher.generate()

# Save the hashed passwords to a pickle file
file_path = Path(__file__).parent / 'hashed_pw.pkl'
with file_path.open('wb') as file:
    pickle.dump(hashed_passwords, file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords)

name, authentication_status, usernames = authenticator.login('login', 'main')

if authentication_status == False:
    st.error('Username/password is incorrect')
if authentication_status == None:
    st.warning('Please enter your username and password')

if authentication_status:
    st.title("Study Buddy")
    st.sidebar.success("Select a page above")

    if "my_input" not in st.session_state:
        st.session_state['my_input'] = ""

    my_input = st.text_input('Input a text here', st.session_state['my_input'])
    submit = st.button('Submit')

    if submit:
        st.session_state['my_input'] = my_input
        st.write('You have entered:', my_input)

        st.write('you have entered: ',my_input)

