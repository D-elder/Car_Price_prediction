





from flask import Flask, request
import flasgger
from flasgger import Swagger

import numpy as np
import pickle
import pandas as pd
import pandas as pd
import numpy as np

pickle_in = open("model_pipeline.pkl","rb")
model=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"



def predict(model, input_df):
  predictions_df = model.predict(estimator= model, data=input_df)
  predictions = predictions_df['Label'][0]
  return predictions

def main():

   from PIL import Image
   img = Image.open("octave.PNG")
   img2 = Image.open("cars.jfif")
   st.image(img,use_column_width=False)
   
add_selectbox = st.sidebar.selectbox(
  "How would you like to predict?",
  ("Online", "Batch"))
  
st.sidebar.info('This app is created to predict cars Selling price') 
st.sidebar.success('https://www.pycaret.org')

st.title("Cars prices Prediction App")


if add_selectbox == 'Online': 

  year = st.number_input('Year', min_value=1983, max_value=2020, value=2014)
  km_driven = st.number_input('km_driven', min_value=1, max_value=None, value=100000)
  fuel_type = st.selectbox('fuel', ['Petrol','Diesel','LPG','CNG'])
  seller_type = st.selectbox('seller_type',['Individual','Dealer','Trustmarl Dealer'])
  transmission = st.selectbox('transmission', ['Manual', 'Automatic'])
  owner = st.selectbox('owner',['First Owner','Second Owner','Third Owner','Fouth & Above Owner', 'Test Drive Car'])
  mileage = st.number_input('mileage', min_value=0, max_value=None, value = 13)
  engine = st.number_input('engine', min_value=None, max_value=None, value=1248)
  max_power = st.number_input('max_power', min_value=None, max_value=None)
  seats = st.selectbox('Seats',[2,3,4,5,6,7,8,9,10,11,12,13])
  torque = st.number_input('torque', min_value= None, max_value=None)
  max_frequency = st.number_input('Frequency', min_value=None, max_value=None)

  output=""
  input_dict ={'year':year,'km_driven':km_driven,'fuel_type':fuel_type,'seller_type':seller_type,'transmission':transmission,'owner':owner,'mileage':mileage,
               'engine':engine,'max_power':max_power,'seats':seats,'torque':torque,'max_frequency':max_frequency}
  input_df = pd.DataFrame([input_dict]) 

  if st.button("Predict"):
    output =predict(model=model, input_df =input_df)
    output = 'INR' + str(output)

if add_selectbox == 'Batch': #Batch Prediction

  file_upload = st.file_uploader("Upload csv file predictions", type=["csv"])

  if file_upload is not None:
    data = pd.read_csv(file_upload)
    predictions = model.predict(estimator=model, data=data)
    st.write(predictions)



    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
