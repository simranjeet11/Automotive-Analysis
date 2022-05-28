import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

st.sidebar.title('🏎 🚗')
m=st.sidebar.radio('Navigation:',('home','corelation','model type','body type','fuel tank','engine','mileage','conclusion'), key='Navigation')

st.title('🚗 Analysis on the type of car combimation is prefered by most automotive industries🚗')
#importing the file
df=pd.read_excel('https://github.com/simranjeet11/Automotive-Analysis/blob/main/cars_engage_2022.xlsx?raw=true')
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
    st.subheader('🏎 INTRODUCTION:')
    st.subheader('This web app is on the production of different automotive industries choices of vehicles.')
    st.subheader('In this web app, we compare each attribute to the ex-showroom price to observe the entities and how to affect the price.')
    st.subheader('On the left sidebar on the screen, you can navigate the different criteria and select the industry.')

def conc():
    st.subheader('conclusion:')
    st.subheader('We can comapare different entities with each other and extract the insigths, like what kind of model can a company release or what kind of model is in trend')

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
elif(m=='conclusion'):
    conc()
