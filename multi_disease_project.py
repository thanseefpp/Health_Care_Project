import streamlit as st
import pickle
from streamlit_option_menu import option_menu


# Loading Saved Machine Learning Model

heart_disease_model_data = pickle.load(open("models/heart_disease_model.sav",'rb'))
diabetes_model_data = pickle.load(open("models/diabetes_model.sav",'rb'))
parkinsons_model_data = pickle.load(open("models/parkinsons_model.sav",'rb'))


#sidebar option turn on
with st.sidebar:
    selected = option_menu("Predictive System",
                    ["Heart Disease",
                    "Diabetes",
                    "Parkinsons"],
                    icons=["heart","activity","person"],
                    default_index=0)
    
    
#based on user selection this filter will change
if (selected == 'Heart Disease'):
    #tile will change to this
    st.title("Heart Disease ML Predictive System")
    
    col1,col2 = st.columns(2)
    
    with col1:
        age     = st.text_input("Age (age in years)")
    with col2:
        sex     = st.text_input("Sex (1 = male; 0 = female")
    with col1:
        cp      = st.text_input("CP(chest Pain (1 = true; 0 = false))")
    with col2:
        trestbps= st.text_input("Trestbps (resting blood pressure)")
    with col1:
        chol    = st.text_input("Chol (serum cholestoral in mg/dl)")
    with col2:
        fbs     = st.text_input("fbs (fasting blood sugar (1 = true; 0 = false)")
    with col1:
        restecg = st.text_input("restecg (resting electrocardiographic results)")
    with col2:
        thalach = st.text_input("thalach (maximum heart rate achieved)")
    with col1:
        exang   = st.text_input("exang (exercise induced angina (1 = yes; 0 = no))")
    with col2:
        thal    = st.text_input("thal (1 = normal; 2 = fixed defect; 3 = reversable defect)")
    with col1:
        slope   = st.text_input("slope (the slope of the peak exercise ST segment)")
    with col2:
        ca      = st.text_input("ca (number of major vessels (0-3) colored by flourosopy)")
    
    oldpeak     = st.text_input("oldpeak (ST depression induced by exercise relative to rest)")
        
    diagnose_result = ""
    
    #creating a button to get the result
    if st.button("Get Result"):
        # age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
        predicted_result = heart_disease_model_data.predict([[int(age),int(sex),int(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]])
        
        if predicted_result[0] == 0:
            diagnose_result = "This Person is Healthy"
        else:
            diagnose_result = "This Person is have Heart Disease"
    
    if diagnose_result != "":
        st.success(diagnose_result)
    
    
if (selected == 'Diabetes'):
    #tile will change to this
    st.title("Diabetes Disease ML Predictive System")
    
    col1,col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input("Pregnancies (Number of times pregnant)")
    with col2:
        Glucose = st.text_input("Glucose")
    with col1:
        BloodPressure = st.text_input("BloodPressure")
    with col2:
        SkinThickness = st.text_input("SkinThickness")
    with col1:
        Insulin = st.text_input("Insulin")
    with col2:
        BMI = st.text_input("BMI (Body mass index(weight in kg/(height in m)^2))")
    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
    with col2:
        Age = st.text_input("Age (age in years)")
        
    diagnose_result = ""
    #creating a button to get the result
    if st.button("Get Result"):
        # Pregnancies : int,Glucose : int,BloodPressure : int,SkinThickness : int,Insulin : int,BMI : float,DiabetesPedigreeFunction :  float,Age : int
        predicted_result = diabetes_model_data.predict([[int(Pregnancies),int(Glucose),int(BloodPressure),int(SkinThickness),int(Insulin),float(BMI),float(DiabetesPedigreeFunction),int(Age)]])
        
        if predicted_result[0] == 0:
            diagnose_result = "This Person is Healthy"
        else:
            diagnose_result = "This Person is Having Diabetes"
    
    if diagnose_result != "":
        st.success(diagnose_result)
    
if (selected == 'Parkinsons'):
    #tile will change to this
    st.title("Parkinsons Disease ML Predictive System")
    
    

