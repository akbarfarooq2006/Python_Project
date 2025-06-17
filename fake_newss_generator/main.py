import random
import streamlit as st
import time

subjects = [
    "Bilawal bhutto",
    "Fahad Mustafa",
    "Aamir khan",
    "Salman khan",
    "Maryam Nawaz",
    "Shahrukh khan",
    "Imran Khan",
    "Jawaharlal Nehru",
    "Lal Bahadur Shastri",
    "Nawaz Sharif",
    "Allama Iqbal",
    "Muhammad Ali",
    "Kashif",
    "Shahid Afridi",
    "Musharaf Ali",
]
actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plote of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match"
]


subject = random.choice(subjects)
action = random.choice(actions)
place = random.choice(places_or_things)
headline = f"BREAKING NEWS: {subject} {action} {place}."

    
# print("Thanks for use this app")



st.title("Welcome Fake news generator🤡")
st.subheader("This app generates fake news headlines")
st.write("This app presented by  ***Godi Media*** 🤡🤡")

if st.button("Generate Fake News"):
    with st.spinner("Wait..."):
        time.sleep(1)
        st.info(headline)
        
