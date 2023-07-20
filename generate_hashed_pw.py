import pickle
from streamlit_authenticator import Hasher

# Define the passwords that you want to hash
passwords = ['abc123', 'def456']

# Create a Hasher instance and generate the hashed passwords
hasher = Hasher(passwords)
hashed_passwords = hasher.generate()

# Save the hashed passwords to a pickle file
with open('hashed_pw.pkl', 'wb') as file:
    pickle.dump(hashed_passwords, file)

print("Hashed passwords saved to 'hashed_pw.pkl'")