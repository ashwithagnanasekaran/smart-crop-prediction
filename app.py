import streamlit as st

st.set_page_config(page_title="Smart Crop Prediction", layout="wide")

page = st.sidebar.radio("Navigate", ["Home", "Crop Assessment", "Result"])

if page == "Home":
    st.title("🌱 Smart Crop Prediction System")
    st.subheader("Welcome to the Crop Prediction Application")
    st.write("This system helps predict suitable crops using soil and weather details.")

if st.session_state.get("go_result"):
    page = "Result"
    st.session_state["go_result"] = False

st.set_page_config(page_title="Smart Crop Prediction", layout="wide")

page = st.sidebar.radio("Navigate", ["Home", "Crop Assessment", "Result"])

if page == "Home":
    st.title("🌱 Smart Crop Prediction System")
    st.subheader("Welcome to the Crop Prediction Application")
    st.write("This system helps predict suitable crops using soil and weather details.")

elif page == "Crop Assessment":
    st.title("🧪 Crop Assessment")
    st.subheader("Enter Soil and Weather Details")

    temp = st.slider("Temperature", 0, 50, 25)
    humidity = st.slider("Humidity", 0, 100, 60)
    rainfall = st.slider("Rainfall", 0, 300, 100)

    nitrogen = st.number_input("Nitrogen (N)", min_value=0, value=50)
    phosphorus = st.number_input("Phosphorus (P)", min_value=0, value=50)
    potassium = st.number_input("Potassium (K)", min_value=0, value=50)
    ph = st.slider("Soil pH", 0.0, 14.0, 6.5)

    st.markdown("### Selected Input Summary")
    st.write({
        "Temperature": temp,
        "Humidity": humidity,
        "Rainfall": rainfall,
        "Nitrogen": nitrogen,
        "Phosphorus": phosphorus,
        "Potassium": potassium,
        "pH": ph
    })

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Weather Details")
        st.write("Temperature:", temp)
        st.write("Humidity:", humidity)
        st.write("Rainfall:", rainfall)

    with col2:
        st.markdown("### Soil Details")
        st.write("Nitrogen:", nitrogen)
        st.write("Phosphorus:", phosphorus)
        st.write("Potassium:", potassium)
        st.write("pH:", ph)

    st.session_state["input_data"] = [nitrogen, phosphorus, potassium, ph]

    import streamlit as st

st.set_page_config(page_title="Smart Crop Prediction", layout="wide")

page = st.sidebar.radio("Navigate", ["Home", "Crop Assessment", "Result"])

if page == "Home":
    st.title("🌱 Smart Crop Prediction System")
    st.subheader("Welcome to the Crop Prediction Application")
    st.write("This system helps predict suitable crops using soil and weather details.")

elif page == "Crop Assessment":
    st.title("🧪 Crop Assessment")
    st.subheader("Enter Soil and Weather Details")

    temp = st.slider("Temperature", 0, 50, 25)
    humidity = st.slider("Humidity", 0, 100, 60)
    rainfall = st.slider("Rainfall", 0, 300, 100)

    nitrogen = st.number_input("Nitrogen (N)", min_value=0, value=50)
    phosphorus = st.number_input("Phosphorus (P)", min_value=0, value=50)
    potassium = st.number_input("Potassium (K)", min_value=0, value=50)
    ph = st.slider("Soil pH", 0.0, 14.0, 6.5)

    st.markdown("### Selected Input Summary")
    st.write({
        "Temperature": temp,
        "Humidity": humidity,
        "Rainfall": rainfall,
        "Nitrogen": nitrogen,
        "Phosphorus": phosphorus,
        "Potassium": potassium,
        "pH": ph
    })

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Weather Details")
        st.write("Temperature:", temp)
        st.write("Humidity:", humidity)
        st.write("Rainfall:", rainfall)

    with col2:
        st.markdown("### Soil Details")
        st.write("Nitrogen:", nitrogen)
        st.write("Phosphorus:", phosphorus)
        st.write("Potassium:", potassium)
        st.write("pH:", ph)

    st.session_state["input_data"] = [nitrogen, phosphorus, potassium, ph]

elif page == "Result":
    st.title("📊 Result")

    if "input_data" not in st.session_state:
        st.warning("Please navigate to Crop Assessment page and enter values first.")
    else:
        input_data = st.session_state["input_data"]

        if st.button("Predict Crop"):
            with st.spinner("Predicting crop..."):
                prediction = model.predict([input_data])

            st.success(f"🌾 Predicted Crop: {prediction[0]}")

            st.markdown("### Recommendation")
            st.info(f"The system suggests **{prediction[0]}** based on the current soil values.")
            st.markdown("### Input Checklist")
st.checkbox("Temperature entered", value=True)
st.checkbox("Humidity entered", value=True)
st.checkbox("Rainfall entered", value=True)
st.checkbox("Soil nutrients entered", value=True)

st.caption("Recommended: enter realistic values for better prediction quality.")

st.caption("Recommended: enter realistic values for better prediction quality.")
from datetime import datetime

import streamlit as st
import shap
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Crop Prediction", layout="wide")

page = st.sidebar.radio("Navigate", ["Home", "Crop Assessment", "Result"])

if page == "Home":
    st.title("🌱 Smart Crop Prediction System")
    st.subheader("Welcome to the Crop Prediction Application")
    st.write("This system helps predict suitable crops using soil and weather details.")

elif page == "Crop Assessment":
    st.title("🧪 Crop Assessment")
    st.subheader("Enter Soil and Weather Details")

    temp = st.slider("Temperature", 0, 50, 25)
    humidity = st.slider("Humidity", 0, 100, 60)
    rainfall = st.slider("Rainfall", 0, 300, 100)

    nitrogen = st.number_input("Nitrogen (N)", min_value=0, value=50)
    phosphorus = st.number_input("Phosphorus (P)", min_value=0, value=50)
    potassium = st.number_input("Potassium (K)", min_value=0, value=50)
    ph = st.slider("Soil pH", 0.0, 14.0, 6.5)

    st.markdown("### Selected Input Summary")
    st.write({
        "Temperature": temp,
        "Humidity": humidity,
        "Rainfall": rainfall,
        "Nitrogen": nitrogen,
        "Phosphorus": phosphorus,
        "Potassium": potassium,
        "pH": ph
    })

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Weather Details")
        st.write("Temperature:", temp)
        st.write("Humidity:", humidity)
        st.write("Rainfall:", rainfall)

    with col2:
        st.markdown("### Soil Details")
        st.write("Nitrogen:", nitrogen)
        st.write("Phosphorus:", phosphorus)
        st.write("Potassium:", potassium)
        st.write("pH:", ph)

    st.session_state["input_data"] = [nitrogen, phosphorus, potassium, ph]

elif page == "Result":
    st.title("📊 Result")

    if "input_data" not in st.session_state:
        st.warning("Please navigate to Crop Assessment page and enter values first.")
    else:
        input_data = st.session_state["input_data"]

        if st.button("Predict Crop"):
            with st.spinner("Predicting crop..."):
                prediction = model.predict([input_data])

            st.success(f"🌾 Predicted Crop: {prediction[0]}")

            st.markdown("### Recommendation")
            st.info(f"The system suggests **{prediction[0]}** based on the current soil values.")

            explainer = shap.Explainer(model)
            shap_values = explainer([input_data])

            st.markdown("---")
            st.markdown("### Explainable AI Analysis")

            st.subheader("📊 SHAP Explanation")
            fig, ax = plt.subplots()
            shap.plots.bar(shap_values[0], show=False)
            st.pyplot(fig)

            st.caption("This chart shows which soil features contributed more to the prediction.")

            st.session_state["history"].append(prediction[0])

            if st.button("Go to Result Page"):
            st.session_state["go_result"] = True
            st.experimental_rerun()

            if any(v is None for v in input_data):
            st.error("Please enter all input values before prediction.")

            st.markdown("### Feature Impact")

            feature_names = ["Nitrogen", "Phosphorus", "Potassium", "pH"]

            for i, val in enumerate(input_data):
                st.write(f"{feature_names[i]}: {val}")

            if st.button("Reset Inputs"):
            st.session_state.clear()
            st.experimental_rerun()

            if "history" not in st.session_state:
            st.session_state["history"] = []

            st.markdown("### Prediction History")

            for i, item in enumerate(st.session_state["history"]):
            st.write(f"{i+1}. {item}")

            st.markdown("### Result Summary")
            st.write({
                "Predicted Crop": prediction[0],
                "Input Count": len(input_data),
                "Status": "Prediction Completed"
            })
            st.success("Use the sidebar to navigate through Home, Crop Assessment, and Result pages.")

            st.info("Fill all soil and weather values carefully before moving to the Result page.")

            st.markdown("---")
            st.caption("Smart Crop Prediction System | Streamlit UI | SHAP Explainable AI")
            col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌦 Weather Input")
    st.write("Temperature, humidity, and rainfall are collected for assessment.")

with col2:
    st.markdown("### 🌱 Soil Input")
    st.write("Nitrogen, phosphorus, potassium, and pH are used for analysis.")

with col3:
    st.markdown("### 🤖 AI Result")
    st.write("Prediction, recommendation, and SHAP explanation are shown.")

    st.write("Prediction Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    st.markdown("### Prediction Status")
    st.success("Assessment completed successfully")

    st.write("Total Predictions:", len(st.session_state["history"]))