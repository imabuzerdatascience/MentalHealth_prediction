import streamlit as st
import requests

from pydantic import ValidationError

# Import your Pydantic model from main.py
from main import StudentData


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Mental Health Predictor",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# FASTAPI URL
# =========================================================

API_URL = "https://mentalhealth-prediction-8wcv.onrender.com/predict"


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(""" 
<style> 

    /* ============================== 
       STREAMLIT INPUT LABELS - BLACK 
       ============================== */ 
 
    /* All input labels */ 
    div[data-testid="stWidgetLabel"] p { 
        color: #000000 !important; 
        font-weight: 600 !important; 
        font-size: 16px !important; 
    } 
 
    /* Number input labels */ 
    div[data-testid="stNumberInput"] label p { 
        color: #000000 !important; 
    } 
 
    /* Selectbox labels */ 
    div[data-testid="stSelectbox"] label p { 
        color: #000000 !important; 
    } 
 
    /* Slider labels if you use them */ 
    div[data-testid="stSlider"] label p { 
        color: #000000 !important; 
    } 
 
    /* Text input labels */ 
    div[data-testid="stTextInput"] label p { 
        color: #000000 !important; 
    } 
 
    /* ============================== 
       INPUT TEXT 
       ============================== */ 
 
    /* Text inside selectbox */ 
    div[data-baseweb="select"] span { 
        color: #ffffff !important; 
    } 
 
    /* Number input text */ 
    div[data-testid="stNumberInput"] input { 
        color: #ffffff !important; 
    } 
 
    /* ============================== 
       SECTION HEADINGS 
       ============================== */ 
 
    .section-title { 
        color: #000000 !important; 
        font-size: 22px; 
        font-weight: 700; 
        margin-top: 15px; 
        margin-bottom: 15px; 
    } 
 
    /* ========================================= 
       PREDICT BUTTON
       ========================================= */ 
 
    button[kind="primaryFormSubmit"] { 
        background-color: black !important;
        color: #ffffff !important; 
        border: none !important; 
        font-weight: 700 !important; 
        font-size: 17px !important; 
        border-radius: 12px !important; 
    }

  
 
    /* ========================================= 
       SUCCESS MESSAGE 
       ========================================= */ 
 
    div[data-testid="stAlert"] { 
        border-radius: 12px !important; 
    } 
 
    div[data-testid="stAlert"] p { 
        color: #166534 !important; 
        font-weight: 600 !important; 
    } 
 
 
    .stApp { 
        background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%); 
    } 
 
    .block-container { 
        max-width: 1200px; 
        padding-top: 2rem; 
        padding-bottom: 3rem; 
    } 
 
    .main-title { 
        text-align: center; 
        font-size: 42px; 
        font-weight: 800; 
        color: #1e293b; 
        margin-bottom: 5px; 
    } 
 
    .subtitle { 
        text-align: center; 
        font-size: 17px; 
        margin-bottom: 35px; 
        color: black; 
    } 
 
    .section-title { 
        font-size: 22px; 
        font-weight: 700; 
        color: black; 
        margin-top: 15px; 
        margin-bottom: 15px; 
    } 
 
    .result-box { 
        background: white; 
        padding: 30px; 
        border-radius: 20px; 
        text-align: center; 
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.08); 
        border: 1px solid #e2e8f0; 
        margin-top: 25px; 
    } 
 
    .result-label { 
        font-size: 18px; 
        color: #64748b; 
    } 
 
    .result-score { 
        font-size: 52px; 
        font-weight: 800; 
        color: #4f46e5; 
    } 
 
</style> 
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🧠 Mental Health Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Enter your personal, academic, social media and lifestyle information.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FORM
# =========================================================

with st.form("mental_health_form"):

    # -----------------------------------------------------
    # PERSONAL INFORMATION
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">👤 Personal Information</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input(
            "Age",
            min_value=0,
            max_value=150,
            value=20,
            step=1
        )

    with col2:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Custom"]
        )

    with col3:
        country = st.selectbox(
            "Country",
            [
                "Other",
                "India",
                "USA",
                "Canada",
                "Australia",
                "UK",
                "Germany",
                "Mexico",
                "Turkey",
                "France"
            ]
        )

    # -----------------------------------------------------
    # ACADEMIC
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">🎓 Academic Information</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        academic_level = st.selectbox(
            "Academic Level",
            [
                "Undergraduate",
                "Graduate",
                "High School"
            ]
        )

    with col2:
        study_hours = st.number_input(
            "Study Hours",
            min_value=0.0,
            max_value=1000.0,
            value=5.0,
            step=0.5
        )

    # -----------------------------------------------------
    # SOCIAL MEDIA
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">📱 Social Media Usage</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        platform = st.selectbox(
            "Most Used Platform",
            [
                "Facebook",
                "LinkedIn",
                "Instagram",
                "Snapchat",
                "Twitter",
                "YouTube",
                "TikTok",
                "LINE",
                "KakaoTalk",
                "VKontakte",
                "WhatsApp",
                "WeChat"
            ]
        )

    with col2:
        purpose = st.selectbox(
            "Purpose of Use",
            [
                "Networking",
                "Education",
                "Entertainment",
                "News"
            ]
        )

    with col3:
        daily_usage = st.number_input(
            "Average Daily Usage Hours",
            min_value=0.0,
            max_value=100.0,
            value=5.0,
            step=0.5
        )

    daily_unlocks = st.number_input(
        "Daily Unlocks",
        min_value=0,
        max_value=10000,
        value=30,
        step=1
    )

    # -----------------------------------------------------
    # LIFESTYLE
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">🏃 Lifestyle & Well-being</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        physical_activity = st.number_input(
            "Physical Activity Hours",
            min_value=0.0,
            max_value=100.0,
            value=1.0,
            step=0.5
        )

    with col2:
        sleep_hours = st.number_input(
            "Sleep Hours per Night",
            min_value=0.0,
            max_value=100.0,
            value=7.0,
            step=0.5
        )

    with col3:
        stress_level = st.selectbox(
            "Stress Level",
            [
                "Low",
                "Medium",
                "High",
                "Very High"
            ]
        )

    st.markdown("<br>", unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "🔮 Predict Mental Health Score",
        use_container_width=True
    )


# =========================================================
# VALIDATION + API REQUEST
# =========================================================

if submitted:

    # -----------------------------------------------------
    # CREATE DATA FOR PYDANTIC
    # -----------------------------------------------------

    input_data = {
        "Age": age,
        "Gender": gender,
        "Country": country,
        "Academic_Level": academic_level,
        "Most_Used_Platform": platform,
        "Purpose_Of_Use": purpose,
        "Avg_Daily_Usage_Hours": daily_usage,
        "Daily_Unlocks": daily_unlocks,
        "Study_Hours": study_hours,
        "Physical_Activity_Hours": physical_activity,
        "Sleep_Hours_Per_Night": sleep_hours,
        "Stress_Level": stress_level
    }


    # =====================================================
    # PYDANTIC VALIDATION
    # =====================================================

    try:

        # This is where your StudentData Pydantic model
        # validates every field.

        validated_data = StudentData(**input_data)

    except ValidationError as e:

        st.error("❌ Please fix the following validation errors:")

        # Show each Pydantic validation error nicely

        for error in e.errors():

            field = error["loc"][0]
            message = error["msg"]

            st.warning(
                f"**{field}:** {message}"
            )

        st.stop()


    # =====================================================
    # CONVERT PYDANTIC DATA TO JSON
    # =====================================================

    payload = validated_data.model_dump()


    # =====================================================
    # SEND TO FASTAPI
    # =====================================================

    with st.spinner("🧠 Analyzing your information..."):

        try:

            response = requests.post(
                API_URL,
                json=payload,
                timeout=10
            )


            # -------------------------------------------------
            # SUCCESS
            # -------------------------------------------------

            if response.status_code == 200:

                result = response.json()

                score = result[
                    "predict_mental_health_score"
                ]

                st.markdown(
        f"""
        <div class="result-box">
            <div class="result-label">
                Your Predicted Mental Health Score
            </div>

                Your Menatal score is  : {score} 
           
                Prediction generated successfully by your ML model.
           
        </div>
        """,
        unsafe_allow_html=True
    )

                st.success(
                    "✅ Prediction generated successfully."
                )


            # -------------------------------------------------
            # FASTAPI VALIDATION ERROR
            # -------------------------------------------------

            elif response.status_code == 422:

                st.error(
                    "❌ FastAPI validation failed."
                )

                st.json(response.json())


            # -------------------------------------------------
            # OTHER API ERROR
            # -------------------------------------------------

            else:

                st.error(
                    f"❌ API Error: {response.status_code}"
                )

                try:
                    st.json(response.json())
                except Exception:
                    st.write(response.text)


        # -----------------------------------------------------
        # CONNECTION ERROR
        # -----------------------------------------------------

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Could not connect to FastAPI."
            )

            st.info(
                "Start your FastAPI server first:\n\n"
                "`uvicorn main:app --reload`"
            )


        # -----------------------------------------------------
        # TIMEOUT
        # -----------------------------------------------------

        except requests.exceptions.Timeout:

            st.error(
                "⏳ FastAPI request timed out. Please try again."
            )


        # -----------------------------------------------------
        # OTHER ERROR
        # -----------------------------------------------------

        except Exception as e:

            st.error(
                f"❌ Something went wrong: {str(e)}"
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#64748b;">
        🧠 Mental Health Prediction System
        • Machine Learning + FastAPI + Pydantic + Streamlit
    </div>
    """,
    unsafe_allow_html=True
)