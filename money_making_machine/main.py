import streamlit as st
import random
import time
import requests



def money_generate():
    return random.randint(1,1000)



st.title("Money Making Machine💸💸")
st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    with st.spinner("Your money is counting......"):
        time.sleep(1)
    st.success("Your made: " + str(money_generate()) + " PKR")

def fetch_hastle():
    try:
        response = requests.get("http://127.0.0.1:8000/slide_hustle")
        if response.status_code == 200:
            hustle = response.json()
            return hustle["hustle"]
        else:
            return "Freelancing"
    except:
        return "Something went wrong"

st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):
    with st.spinner("Getting Hustle Ideas"):
        time.sleep(1)
    st.success(fetch_hastle())












