import streamlit as st

st.set_page_config(page_title="Smart Crop Prediction", layout="wide")

page = st.sidebar.radio("Navigate", ["Home", "Crop Assessment", "Result"])

if page == "Home":
    st.title("🌱 Smart Crop Prediction System")
    st.subheader("Welcome to the Crop Prediction Application")
    st.write("This system helps predict suitable crops using soil and weather details.")

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

    