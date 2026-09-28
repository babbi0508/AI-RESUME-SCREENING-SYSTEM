import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #eef2ff, #f8fafc);
    }

    /* Main title */
    .title {
        text-align: center;
        color: #1e3a8a;
        font-size: 38px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 17px;
        margin-bottom: 30px;
    }

    /* Form container */
    .form-box {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px;
        border: none;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background-color: #1d4ed8;
        transform: scale(1.02);
    }

    /* Input fields */
    .stTextInput input,
    .stTextArea textarea {
        border-radius: 8px;
        border: 1px solid #cbd5e1;
    }

</style>
""", unsafe_allow_html=True)


# Title
st.markdown(
    '<div class="title">🤖 AI Resume Screening System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Upload your resume and compare it with a job description</div>',
    unsafe_allow_html=True
)


# Form container
st.markdown('<div class="form-box">', unsafe_allow_html=True)

# Name
name = st.text_input("👤 Enter your name")

# Resume upload
resume = st.file_uploader(
    "📄 Upload your resume",
    type=["pdf", "docx", "txt"]
)

# Job description
job = st.text_area(
    "💼 Enter Job Description",
    height=180
)

# Button
if st.button("🔍 Check Resume"):

    if name and resume and job:

        st.success("✅ Resume submitted successfully!")

        st.info(
            "Your resume is ready for AI-based screening."
        )

    else:

        st.error("❌ Please fill all fields")

st.markdown('</div>', unsafe_allow_html=True)