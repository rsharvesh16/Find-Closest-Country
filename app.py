import streamlit as st
import Levenshtein as lev

def find_closest_match(input_text, items):
    min_distance = float('inf')
    closest_match = None
    
    for item in items:
        distance = lev.distance(input_text.lower(), item.lower())
        if distance < min_distance:
            min_distance = distance
            closest_match = item
            
    return closest_match, min_distance

st.header("Find Closest Match of a Country")
items = countries = [
    "USA", "UK", "Germany", "France", "Italy", "Japan", "China", "India", "Brazil", "Canada",
    "Australia", "Russia", "South Africa", "Argentina", "Egypt", "Mexico", "Spain", "South Korea",
    "Saudi Arabia", "Nigeria", "Indonesia", "Sweden", "Turkey", "Vietnam", "Netherlands",
    "Pakistan", "Iran", "Poland", "Thailand", "Bangladesh"
]

input_text = st.text_input("Enter a country:", "")
closest_match, min_distance = find_closest_match(input_text, items)

if closest_match:
    st.write(f"Closest match to '{input_text}' is: '{closest_match}' (Levenshtein distance: {min_distance})")
else:
    st.write("No match found.")