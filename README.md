# Find-Closest-Country

    
  ### Country Matching with Levenshtein Distance
This project uses the Levenshtein distance algorithm to find the closest match to a user-provided country name among a list of 20 countries. The Levenshtein distance algorithm is a string metric for measuring the difference between two sequences. It calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into another.

<div align="center">
<img width="446" alt="image" src="image3.png">
</div>

  ## Features
    - Input Box: Users can enter a country name in the input box.
    - Closest Match: The app finds the closest match to the user input from a list of 20 countries.
    - Levenshtein Distance: The app uses the Levenshtein distance algorithm to calculate the similarity between the user input and each country in the list.
    
  ## Requirements
    - Python 3.6+
    - Streamlit
    - python-Levenshtein

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rsharvesh16/Find-Closest-Country.git
   cd Find-Closest-Country
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate, On Windows, use venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your web browser (by default, the app runs on `localhost:8501`).
3. Enter a country name in the input box and press Enter. The app will display the closest match from the list of 20 countries.

