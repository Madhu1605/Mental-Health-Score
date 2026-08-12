import streamlit as st
import requests


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Mental Health Score",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #071918;
    color: white;
}

.block-container {
    max-width: 1200px;
    padding-top: 35px;
    padding-bottom: 40px;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
}

.subtitle {
    color: #9db8b3;
    font-size: 16px;
    margin-bottom: 35px;
}

.section {
    background: #0d2422;
    border: 1px solid #183b37;
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 20px;
}

.section-title {
    font-size: 19px;
    font-weight: 700;
    margin-bottom: 20px;
}

.section-number {
    color: #65d8b7;
    margin-right: 8px;
}

label {
    color: #b7ccc8 !important;
}

.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    border: none;
    background: #54d6b2;
    color: #06201b;
    font-size: 16px;
    font-weight: 700;
}

.stButton > button:hover {
    background: #6ee4c3;
}

.disclaimer {
    margin-top: 25px;
    padding: 14px;
    background: rgba(255, 255, 255, 0.04);
    border-radius: 10px;
    color: #8da7a2;
    font-size: 12px;
    text-align: center;
}

.result-card {
    background: #0d2422;
    border: 1px solid #183b37;
    border-radius: 24px;
    padding: 45px 35px;
    margin-top: 35px;
    text-align: center;
}

.result-title {
    font-size: 23px;
    font-weight: 700;
    color: white;
    margin-bottom: 35px;
}

.result-score {
    font-size: 70px;
    font-weight: 800;
    color: white;
    line-height: 1;
}

.result-out {
    font-size: 20px;
    color: #8fa9a4;
    margin-top: 8px;
}

.result-info {
    margin-top: 30px;
    padding: 15px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    color: #9db8b3;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🧠 Mental Health Score</div>',
    unsafe_allow_html=True
)




# =========================================================
# 01 - PERSONAL PROFILE
# =========================================================

st.markdown(
    """
    <div class="section">
        <div class="section-title">
            <span class="section-number">01</span>
            Personal Profile
        </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=10,
        max_value=100,
        value=21
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col3:
    country = st.text_input(
        "Country",
        value="India"
    )

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# 02 - ACADEMIC & DIGITAL HABITS
# =========================================================

st.markdown(
    """
    <div class="section">
        <div class="section-title">
            <span class="section-number">02</span>
            Academic & Digital Habits
        </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

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
    purpose = st.selectbox(
        "Primary Purpose",
        [
            "Networking",
            "Education",
            "Entertainment",
            "News"
        ]
    )

with col3:
    platform = st.selectbox(
        "Most-used Platform",
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

col1, col2 = st.columns(2)

with col1:
    screen_time = st.number_input(
        "Avg. Daily Screen Time (hours)",
        min_value=0.0,
        max_value=24.0,
        value=4.0,
        step=0.1
    )

with col2:
    daily_unlocks = st.number_input(
        "Daily Phone Unlocks",
        min_value=0,
        value=50,
        step=1
    )

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# 03 - LIFESTYLE
# =========================================================

st.markdown(
    """
    <div class="section">
        <div class="section-title">
            <span class="section-number">03</span>
            Lifestyle
        </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    study_hours = st.number_input(
        "Study Hours / Day",
        min_value=0.0,
        max_value=24.0,
        value=4.0,
        step=0.1
    )

with col2:
    physical_activity = st.number_input(
        "Physical Activity / Day",
        min_value=0.0,
        max_value=24.0,
        value=1.0,
        step=0.1
    )

with col3:
    sleep_hours = st.number_input(
        "Sleep / Night",
        min_value=0.0,
        max_value=24.0,
        value=7.0,
        step=0.1
    )

st.markdown("</div>", unsafe_allow_html=True)

stress_level = st.selectbox(
    "Stress Level",
    ["Low", "Medium", "High", "Very High"]
)
# =========================================================
# PREDICT BUTTON
# =========================================================

predict = st.button("🧠 Predict Score")


# =========================================================
# PREDICTION
# =========================================================

if predict:

    payload = {
        "age": age,
        "gender": gender,
        "country": country,
        "academic_level": academic_level,
        "most_used_platform": platform,
        "purpose_of_use": purpose,
        "avg_daily_usage_hours": screen_time,
        "daily_unlocks": daily_unlocks,
        "study_hours": study_hours,
        "physical_activity_hours": physical_activity,
        "sleep_hours_per_night": sleep_hours,

        
        "stress_level": stress_level
    }

    try:

        with st.spinner("Generating your score..."):

            response = requests.post(
                "https://mental-health-score-1-63iu.onrender.com/predict",
                json=payload,
                timeout=20
            )

        # -------------------------------------------------
        # SUCCESS
        # -------------------------------------------------

        if response.status_code == 200:

            result = response.json()

            score = float(
                result["predicted_mental_health_score"]
            )
            
            # -------------------------------------------------
            # RESULT CARD
            # -------------------------------------------------

            st.html(f"""
            <div style="
                background:#0d2422;
                border:1px solid #183b37;
                border-radius:24px;
                padding:45px 35px;
                margin-top:35px;
                text-align:center;
            ">
                <div style="
                    font-size:23px;
                    font-weight:700;
                    color:white;
                    margin-bottom:35px;
                ">
                    Your Mental Health Score
                </div>

                <div style="
                    font-size:70px;
                    font-weight:800;
                    color:white;
                    line-height:1;
                ">
                    {score:.2f}
                </div>

                <div style="
                    font-size:20px;
                    color:#8fa9a4;
                    margin-top:8px;
                ">
                    /10
                </div>

                
            </div>
            """)

        # -------------------------------------------------
        # API ERROR
        # -------------------------------------------------

        else:

            st.error(
                f"FastAPI returned status {response.status_code}"
            )

            st.code(response.text)

    # -----------------------------------------------------
    # CONNECTION ERROR
    # -----------------------------------------------------

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Cannot connect to FastAPI."
        )

        st.info(
            "Make sure FastAPI is running with:"
        )

        

    # -----------------------------------------------------
    # TIMEOUT
    # -----------------------------------------------------

    except requests.exceptions.Timeout:

        st.error(
            "❌ FastAPI took too long to respond."
        )

    # -----------------------------------------------------
    # OTHER ERROR
    # -----------------------------------------------------

    except Exception as e:

        st.error(
            f"❌ Unexpected error: {e}"
        )


# =========================================================
# DISCLAIMER
# =========================================================

# st.markdown(
#     """
#     <div class="disclaimer">
#         This model provides an estimated score based on the
#         information you provide. It is not a medical diagnosis.
#     </div>
#     """,
#     unsafe_allow_html=True
# )