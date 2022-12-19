import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import numpy as np

# Loading Saved Machine Learning Model

heart_disease_model_data = pickle.load(open("models/heart_disease_model.sav",'rb'))
diabetes_model_data = pickle.load(open("models/diabetes_model.sav",'rb'))
parkinsons_model_data = pickle.load(open("models/parkinsons_model.sav",'rb'))
standardized_parkinsons_model = pickle.load(open("models/parkinsons_trained_sc.sav","rb"))


#sidebar option turn on
with st.sidebar:
    selected = option_menu("Health Care \nPredictive System",
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
    
    col1,col2 = st.columns(2)
    
    with col1:
        MDVP_Fo_Hz = st.text_input("MDVP:Fo(Hz)")
    with col2:
        MDVP_Fhi_Hz = st.text_input("MDVP:Fhi(Hz)")
    with col1:
        MDVP_Flo_Hz = st.text_input("MDVP:Flo(Hz)")
    with col2:
        MDVP_jitter_perc = st.text_input("MDVP:Jitter(%)")
    with col1:
        MDVP_jitter_abs = st.text_input("MDVP:Jitter(Abs)")
    with col2:
        MDVP_RAP = st.text_input("MDVP:RAP")
    with col1:
        MDVP_PPQ = st.text_input("MDVP:PPQ")
    with col2:
        Jitter_DDP = st.text_input("Jitter:DDP")
    with col1:
        MDVP_Shimmer = st.text_input("MDVP:Shimmer")
    with col2:
        MDVP_Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col1:
        Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
    with col2:
        Shimmer_APQ5 = st.text_input("Shimmer:APQ5")
    with col1:
        MDVP_APQ = st.text_input("MDVP:APQ")
    with col2:
        Shimmer_DDA = st.text_input("Shimmer:DDA")
    with col1:
        NHR = st.text_input("NHR")
    with col2:
        HNR = st.text_input("HNR")
    with col1:
        RPDE = st.text_input("RPDE")
    with col2:
        DFA = st.text_input("DFA")
    with col1:
        spread1 = st.text_input("spread1")
    with col2:
        spread2 = st.text_input("spread2")
    with col1:
        D2 = st.text_input("D2")
    with col2:
        PPE = st.text_input("PPE")
    # 116.67600,137.87100,111.36600,0.00997,0.00009,0.00502,0.00698,0.01505,0.05492,0.51700,0.02924,0.04005,0.03772,0.08771,0.01353,20.64400,0.434969,0.819235,-4.117501,0.334147,2.405554,0.368975
    
    diagnose_result = ""
    #creating a button to get the result
    if st.button("Get Result"):
        input_data = (float(MDVP_Fo_Hz),float(MDVP_Fhi_Hz),float(MDVP_Flo_Hz),float(MDVP_jitter_perc),float(MDVP_jitter_abs),
                    float(MDVP_RAP),float(MDVP_PPQ),float(Jitter_DDP),float(MDVP_Shimmer),float(MDVP_Shimmer_dB),
                    float(Shimmer_APQ3),float(Shimmer_APQ5),float(MDVP_APQ),float(Shimmer_DDA),float(NHR),
                    float(HNR),float(RPDE),float(DFA),float(spread1),float(spread2),float(D2),float(PPE))

        # converting dataset into numpy array
        data_converted = np.asarray(input_data)

        # reshaping the data into 1,-1 to avoid the error

        reshaped_data = data_converted.reshape(1,-1)
        # standardizing the data
        standardized_data = standardized_parkinsons_model.transform(reshaped_data)
        #svc model used to predict the result
        predicted_result = parkinsons_model_data.predict(standardized_data)

        if predicted_result[0] == 0:
            diagnose_result = "This Person is Healthy"
        else:
            diagnose_result = "This Person is Having Parkinsons "
    
    if diagnose_result != "":
        st.success(diagnose_result)