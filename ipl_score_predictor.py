import pandas as pd
import numpy as np
import streamlit as st
import math
st.set_page_config(page_title="IPL Score Predictor",layout="centered")

from joblib import load
model=load("C:\\Users\\Dell\\OneDrive\\Desktop\\Ipl score predictor project\\ipl_model.joblib")


st.markdown("<h1 style='text-align: center; color: white;'> IPL Score Predictor </h1>", unsafe_allow_html=True)

st.markdown(
    f"""
        <style>
        .stApp {{
            background-image: url("https://wallpapercave.com/wp/wp9536040.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


batting_team= st.selectbox('Select the Batting Team ',('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad'))
prediction_array = []

if batting_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
elif batting_team == 'Delhi Daredevils':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
elif batting_team == 'Kings XI Punjab':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
elif batting_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
elif batting_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
elif batting_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
elif batting_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
elif batting_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]


bowling_team = st.selectbox('Select the Bowling Team ',('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad'))

if bowling_team==batting_team:
    st.error('Bowling and Batting teams should be different')
# Bowling Team
if bowling_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
elif bowling_team == 'Delhi Daredevils':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
elif bowling_team == 'Kings XI Punjab':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
elif bowling_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
elif bowling_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
elif bowling_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
elif bowling_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
elif bowling_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]

col1, col2 = st.columns(2)


with col1:
    overs = st.number_input('Enter the Current Over',min_value=5.1,max_value=19.5,value=5.1,step=0.1)
    if overs-math.floor(overs)>0.5:
        st.error('Please enter valid over input as one over only contains 6 balls')
with col2:

    runs = st.number_input('Enter Current runs',min_value=0,max_value=354,step=1,format='%i')

wickets =st.slider('Enter Wickets fallen till now',0,9)
wickets=int(wickets)


col3, col4 = st.columns(2)

with col3:

    runs_in_prev_5 = st.number_input('Runs scored in the last 5 overs',min_value=0,max_value=runs,step=1,format='%i')

with col4:

    wickets_in_prev_5 = st.number_input('Wickets taken in the last 5 overs',min_value=0,max_value=wickets,step=1,format='%i')

prediction_array = prediction_array + [runs, wickets, overs, runs_in_prev_5,wickets_in_prev_5]
prediction_array = np.array([prediction_array])
predict = model.predict(prediction_array)


if st.button('Predict Score'):
    
    my_prediction = int(round(predict[0]))
    
   
    x=f'PREDICTED MATCH SCORE : {my_prediction-5} to {my_prediction+5}' 
    st.success(x)

if st.sidebar.button("About us"):
    st.write("""Hi,This is Tanmay Rastogi.
    I am a pre final year student at Delhi Technological University. I have made this project to predict score in an ipl match.
    For this project I have used Random forest regressor as it had best efficiency and lowest root mean square error. I hope you would to love this.
    """)




st.markdown(
    "<p style='text-align: center; color: white; font-size: 20px;'>Made with ❤️</p>",
    unsafe_allow_html=True
)
