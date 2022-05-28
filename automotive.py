import streamlit as st
import string as str
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score 
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
import warnings
warnings.filterwarnings('ignore');
import seaborn as sns
from PIL import Image

st.sidebar.title('🏎 🚗')
m=st.sidebar.radio('Navigation:',('Home','corelation','model type','body type','fuel tank','engine','mileage'), key='Navigation')


st.title('🚗 Analysis on the type of car combimation is prefered by most automotive industries🚗')
#importing the file
df=pd.read_excel(r'https://github.com/simranjeet11/Automotive-Analysis/blob/main/cars_engage_2022.xlsx')
#cleaning data
df.drop_duplicates(inplace=True) #drop the duplicates
col=['Ex-Showroom_Price','Displacement','Fuel_Tank','Height','Length','Width','Highway_Mileage','City_Mileage','Kerb_Weight']


df['Height'] = df['Height'].str.replace(' mm','',regex=False).astype(float)
df['Length'] = df['Length'].str.replace(' mm','',regex=False).astype(float)
df['Width'] = df['Width'].str.replace(' mm','',regex=False).astype(float)
df['Fuel_Tank_Capacity'] = df['Fuel_Tank_Capacity'].str.replace(' litres','',regex=False).astype(float)
df['Displacement'] = df['Displacement'].str.replace(' cc','',regex=False)
df['Ex-Showroom_Price'] = df['Ex-Showroom_Price'].str.replace('Rs. ','',regex=False)
df['Ex-Showroom_Price'] = df['Ex-Showroom_Price'].str.replace(',','',regex=False)
df['Ex-Showroom_Price'] = df['Ex-Showroom_Price'].astype(int)
df[['City_Mileage','Highway_Mileage']] = df[['City_Mileage','Highway_Mileage']].replace(to_replace=r'([a-z/]+|[A-Z/]+|[,]+|[-])', value='', regex=True).astype(float)
df[['Kerb_Weight']] = df[['Kerb_Weight']].replace(to_replace=r'([a-z/]+|[A-Z/]+|[,]+|[-])', value='', regex=True).astype(float)

df = df[~df.Company.isnull()]
df = df[~df.Width.isnull()]
df = df[~df.Cylinders.isnull()]
df = df[~df['Fuel_Tank_Capacity'].isnull()]
df = df[~df['Seat'].isnull()]
df = df[~df['Ex-Showroom_Price'].isnull()]
df = df[~df['City_Mileage'].isnull()]
df = df[~df['Highway_Mileage'].isnull()]
df = df[~df['Kerb_Weight'].isnull()]
df = df[~df['Height'].isnull()]
df = df[~df['Length'].isnull()]

df.Doors = df.Doors.astype(int)
df.Seat = df.Seat.astype(int)
df.Displacement = df.Displacement.astype(int)
df.Cylinders = df.Cylinders.astype(int)

x=df[df.Company ==st.sidebar.selectbox('Company',df.Company.unique())]

  
def corr():
    st.subheader('The Corelation between the different parameters in the vehical:')#plotting the corelation between the attributes
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), ax=ax)
    st.write(fig)


def model():
    st.subheader('Model Type :')
    fig, ax = plt.subplots()
    sns.boxplot(data=x ,x='Ex-Showroom_Price' ,y='Model')
    st.write(fig)
    st.text('We can here observe how the model of the company relates with the price')

    st.subheader('Varient')
    fig, ax = plt.subplots()
    sns.boxplot(data=x ,x='Ex-Showroom_Price' ,y='Variant')
    st.write(fig)
    
def body_type():
    st.subheader('width of the car')
    fig, ax = plt.subplots()
    sns.scatterplot(data=x ,x='Ex-Showroom_Price' ,y='Width')
    st.write(fig)
     
    st.subheader('length of the car')
    fig, ax = plt.subplots()
    sns.scatterplot(data=x ,x='Ex-Showroom_Price' ,y='Length')
    st.write(fig)

    st.subheader('Height of the car')
    fig, ax = plt.subplots()
    sns.scatterplot(data=x ,x='Ex-Showroom_Price' ,y='Height')
    st.write(fig)

    st.subheader('Kerb weight')
    fig, ax = plt.subplots()
    sns.scatterplot(data=x ,x='Ex-Showroom_Price' ,y='Kerb_Weight')
    st.write(fig)
    
    st.subheader('no.of seats')
    fig, ax = plt.subplots()
    sns.scatterplot(data=x ,x='Ex-Showroom_Price' ,y='Seat')
    st.write(fig)
    
    st.subheader('doors')
    fig, ax = plt.subplots()
    sns.scatterplot(data=x ,x='Ex-Showroom_Price' ,y='Doors')
    st.write(fig)
    
def fuel_tank():
    st.subheader('Fuel tank capacity')
    fig, ax = plt.subplots()
    sns.histplot(data=x ,x='Ex-Showroom_Price' ,y='Fuel_Tank_Capacity')
    st.write(fig)
    
    st.subheader('Fuel type')
    fig, ax = plt.subplots()
    sns.boxplot(data=x ,x='Ex-Showroom_Price' ,y='Fuel_Type')
    st.write(fig)
    
def mileage():
    st.subheader('Highway mileage')
    fig, ax = plt.subplots()
    sns.scatterplot(data=x ,x='Ex-Showroom_Price' ,y='Highway_Mileage')
    st.write(fig)
    
    st.subheader('City mileage')
    fig, ax = plt.subplots()
    sns.scatterplot(data=x ,x='Ex-Showroom_Price' ,y='City_Mileage')
    st.write(fig)

def eng():
    st.subheader('engine displacement')
    fig, ax = plt.subplots()
    sns.histplot(data=x ,x='Ex-Showroom_Price' ,y='Displacement')
    st.write(fig)
    
    st.subheader('Engine location')
    fig, ax = plt.subplots()
    sns.boxplot(data=x ,x='Ex-Showroom_Price' ,y='Engine_Location')
    st.write(fig)
def home():
    
    #st.image(,caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image('https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.gettyimages.com%2Fphotos%2Fview-of-cars-on-production-line-in-factory-picture-id723504579%3Fs%3D612x612&imgrefurl=https%3A%2F%2Fwww.gettyimages.com%2Fphotos%2Fautomobile-industry&tbnid=UZdWTwvLLt8jzM&vet=12ahUKEwj18-zR4__3AhVbz6ACHYxwDmgQMygAegUIARC2AQ..i&docid=wYitvSp6IrZl-M&w=612&h=408&q=automotive%20industry%20image%20url&client=firefox-b-d&ved=2ahUKEwj18-zR4__3AhVbz6ACHYxwDmgQMygAegUIARC2AQ', width=400)       

if(m=='home'):
    home()
elif(m=='corelation'):   
    corr()
elif(m=='model type'):    
    model()
elif(m=='body type'):
    body_type()
elif(m=='fuel tank'):
    fuel_tank()
elif(m=='mileage'):
    mileage()
elif(m=='engine'):
    eng()
