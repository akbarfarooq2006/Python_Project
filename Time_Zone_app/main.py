import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo



TIME_ZONE = [
    "UTC",
    "Asia/Karachi",
    "Africa/Abidjan",
    # "Lahore",
    "Africa/Accra",
    "Africa/Addis_Ababa",
    "Africa/Algiers",
    "Africa/Asmara",
    "Africa/Bamako",
    "Africa/Bangui",
    "Africa/Banjul",
    "Africa/Bissau",
    "Africa/Cairo",
    "Africa/Casablanca",
    "Africa/Dakar",
    "Africa/Djibouti",
    "Africa/Douala",
    "Africa/Freetown",
    "Africa/Harare",
    "Africa/Johannesburg",
    "Africa/Kampala",
    "Africa/Khartoum",
    "Africa/Lagos",
    "Africa/Nairobi",
    "America/Anchorage",
    "America/Argentina/Buenos_Aires",
    "America/Asuncion",
    "America/Bogota",
    "America/Caracas",
    "America/Chicago",
    "America/Denver",
    "America/Detroit",
    "America/Edmonton",
    "America/Halifax",
    "America/Havana",
    "America/Indianapolis",
    "America/Lima",
    "America/Los_Angeles",
    "America/Mexico_City",
    "America/Montreal",
    "America/New_York",
    "America/Panama",
    "America/Phoenix",
    "America/Santiago",
    "America/Sao_Paulo",
    "America/St_Johns",
    "America/Toronto",
    "America/Vancouver",
    "America/Winnipeg",
    "Asia/Almaty",
    "Asia/Amman",
    "Asia/Baghdad",
    "Asia/Bahrain",
    "Asia/Bangkok",
    "Asia/Beirut",
    "Asia/Colombo",
    "Asia/Damascus",
    "Asia/Dhaka",
    "Asia/Dubai",
    "Asia/Hong_Kong",
    "Asia/Irkutsk",
    "Asia/Jakarta",
    "Asia/Jerusalem",
    "Asia/Kabul",
    "Asia/Karachi",
    "Asia/Kathmandu",
    "Asia/Kolkata",
    "Asia/Kuwait",
    "Asia/Manila",
    "Asia/Muscat",
    "Asia/Riyadh",
    "Asia/Seoul",
    "Asia/Shanghai",
    "Asia/Singapore",
    "Asia/Taipei",
    "Asia/Tehran",
    "Asia/Tokyo",
    "Asia/Vladivostok",
    "Asia/Yakutsk",
    "Australia/Adelaide",
    "Australia/Brisbane",
    "Australia/Darwin",
    "Australia/Hobart",
    "Australia/Melbourne",
    "Australia/Perth",
    "Australia/Sydney",
    "Europe/Amsterdam",
    "Europe/Athens",
    "Europe/Belgrade",
    "Europe/Berlin",
    "Europe/Brussels",
    "Europe/Bucharest",
    "Europe/Budapest",
    "Europe/Copenhagen",
    "Europe/Dublin",
    "Europe/Helsinki",
    "Europe/Istanbul",
    "Europe/Kiev",
    "Europe/Lisbon",
    "Europe/London",
    "Europe/Madrid",
    "Europe/Moscow",
    "Europe/Oslo",
    "Europe/Paris",
    "Europe/Prague",
    "Europe/Rome",
    "Europe/Stockholm",
    "Europe/Vienna",
    "Europe/Warsaw",
    "Europe/Zurich",
    "Pacific/Auckland",
    "Pacific/Fiji",
    "Pacific/Honolulu",
    "Pacific/Noumea"
]

st.title("Time Zone App ⌛⌛")

# Get user input for time zone
selected_time_zone = st.multiselect("Select your time zone", TIME_ZONE, default = ["UTC","Asia/Karachi"])

st.subheader("Selected Timezone")

for tz in selected_time_zone:
    # st.write(datetime.now()) it gives current my location time
    # st.write(f"Time zone: {ZoneInfo(tz)}")  #it gives  zone loaction neccessary for datetime.now() 
    # current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d   %I:%M:%S %p")
    current_time = datetime.now(ZoneInfo(tz)).strftime("%I:%M:%S %p")
    current_date = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d  ")
    current_day = datetime.now(ZoneInfo(tz)).strftime("%A")
    st.write(f"**{tz}** :   {current_time} {current_day} {current_date}")


st.subheader("Convert Time Between Timezone")
current_time = st.time_input("Current Time", datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONE ,index =0)
to_tz = st.selectbox("To Timezone", TIME_ZONE , index= 1)

if st.button("Convert"):
    # Convert the time to the selected timezone
    
    dt = datetime.combine(datetime.now().today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d  %I:%M:%S %p")
    st.success(f"Converted Time: {converted_time}")    
    



















