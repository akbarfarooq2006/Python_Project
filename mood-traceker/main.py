import streamlit as st
import pandas as pd
import datetime
import csv
import os

# st.title("Mood Tracker 😎😎")

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        with open(MOOD_FILE, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Mood"])
    if os.stat(MOOD_FILE).st_size == 0:
        with open(MOOD_FILE, "w", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Mood"])
    if os.stat(MOOD_FILE).st_size > 0:
        return pd.read_csv(MOOD_FILE, encoding='utf-8')

def save_mood_data(date,mood):
    with open(MOOD_FILE, "a" , encoding = "utf-8" ) as file:
        if os.stat(MOOD_FILE).st_size == 0:
            writer = csv.writer(file)
            writer.writerow(["Date", "Mood"])
        writer = csv.writer(file)
        writer.writerow([date, mood])
        

st.title("Mood Tracker 😎😎")
st.subheader ("How are you felling today?")

today = datetime.date.today()
mood = st.selectbox("Select your mood:", ["Happy", "Sad", "Angry", "Neutral"])

if st.button("Log Mood"):
    if mood == "Happy":
        save_mood_data(datetime.date.today(), mood+"😀")
    elif mood == "Sad":
        save_mood_data(datetime.date.today(), mood+"😔")
    elif mood == "Angry":
        save_mood_data(datetime.date.today(), mood+"😠")
    else:
        save_mood_data(datetime.date.today(), mood+"😐")
    st.success("Mood saved successfully!")


data = load_mood_data()
if not data.empty:
    st.subheader("Mood Trends over time")
    data["Date"] = pd.to_datetime(data["Date"])
    
    mood_counts = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_counts)
else:
    st.info ("no data available")

    













