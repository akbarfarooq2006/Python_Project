import streamlit as st

st.set_page_config(layout="centered")

st.title("Streamlit Calculator")

# Initialize session state for display and calculation
if 'display' not in st.session_state:
    st.session_state.display = "0"
if 'current_number' not in st.session_state:
    st.session_state.current_number = ""
if 'operator' not in st.session_state:
    st.session_state.operator = None
if 'first_number' not in st.session_state:
    st.session_state.first_number = None

# Display field
st.text_input("", st.session_state.display, key="display_input", disabled=True)

def handle_button_click(char):
    if char.isdigit() or char == ".":
        if st.session_state.display == "0" and char != ".":
            st.session_state.display = char
        else:
            st.session_state.display += char
        st.session_state.current_number += char
    elif char in ["+", "-", "*", "/"]:
        if st.session_state.current_number:
            st.session_state.first_number = float(st.session_state.current_number)
            st.session_state.operator = char
            st.session_state.display += f" {char} "
            st.session_state.current_number = ""
    elif char == "C":
        st.session_state.display = "0"
        st.session_state.current_number = ""
        st.session_state.operator = None
        st.session_state.first_number = None
    elif char == "=":
        if st.session_state.first_number is not None and st.session_state.current_number:
            second_number = float(st.session_state.current_number)
            try:
                if st.session_state.operator == "+":
                    result = st.session_state.first_number + second_number
                elif st.session_state.operator == "-":
                    result = st.session_state.first_number - second_number
                elif st.session_state.operator == "*":
                    result = st.session_state.first_number * second_number
                elif st.session_state.operator == "/":
                    if second_number != 0:
                        result = st.session_state.first_number / second_number
                    else:
                        st.session_state.display = "Error: Div by zero"
                        st.session_state.current_number = ""
                        st.session_state.operator = None
                        st.session_state.first_number = None
                        return
                st.session_state.display = str(result)
                st.session_state.current_number = str(result)
                st.session_state.operator = None
                st.session_state.first_number = None
            except Exception as e:
                st.session_state.display = "Error"
                st.session_state.current_number = ""
                st.session_state.operator = None
                st.session_state.first_number = None
# Calculator buttons layout
buttons = [
    ["7", "8", "9", "//"],
    ["4", "5", "6", "**"],
    ["1", "2", "3","--"],
    ["C", "0", ".", "++ "],
    ["="]
]

for row in buttons:
    cols = st.columns(len(row))
    for i, button_char in enumerate(row):
        with cols[i]:
            st.button(button_char, on_click=handle_button_click, args=(button_char,), use_container_width=True)
