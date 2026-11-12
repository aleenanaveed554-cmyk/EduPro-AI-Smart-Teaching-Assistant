import streamlit as st
from groq import Groq

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="EduPro AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

* {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top right, rgba(37, 99, 235, 0.14), transparent 35%),
        radial-gradient(circle at bottom left, rgba(14, 165, 233, 0.10), transparent 30%),
        #07111f;
    color: #f8fafc;
}

/* Main container */
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Header */
.hero {
    padding: 30px 34px;
    border-radius: 24px;
    background: linear-gradient(
        135deg,
        rgba(15, 23, 42, 0.96),
        rgba(15, 45, 75, 0.92)
    );
    border: 1px solid rgba(96, 165, 250, 0.22);
    box-shadow: 0 20px 60px rgba(0,0,0,0.25);
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin: 0;
    color: #ffffff;
    font-weight: 700;
}

.hero p {
    font-size: 17px;
    color: #cbd5e1;
    margin-top: 10px;
}

/* Cards */
.card {
    background: rgba(15, 23, 42, 0.88);
    border: 1px solid rgba(148, 163, 184, 0.16);
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.18);
}

.card-title {
    font-size: 22px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 8px;
}

.card-subtitle {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 18px;
}

/* Labels */
label, .stSelectbox label, .stTextInput label,
.stTextArea label {
    color: #f8fafc !important;
    font-weight: 600 !important;
}

/* Inputs */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    background-color: #0f1d31 !important;
    color: #ffffff !important;
    border: 1px solid #263a55 !important;
    border-radius: 12px !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #94a3b8 !important;
}

/* Button */
.stButton > button {
    width: 100%;
    min-height: 50px;
    border: none;
    border-radius: 12px;
    background: linear-gradient(135deg, #2563eb, #0ea5e9);
    color: white;
    font-size: 16px;
    font-weight: 700;
    transition: 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(37,99,235,0.35);
}

/* Output */
.output {
    background: #0b1728;
    border: 1px solid rgba(96, 165, 250, 0.25);
    border-radius: 18px;
    padding: 28px;
    color: #f8fafc;
    line-height: 1.8;
    font-size: 16px;
}

.output h1,
.output h2,
.output h3 {
    color: #60a5fa;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #08111f;
    border-right: 1px solid #1e293b;
}

.sidebar-title {
    font-size: 24px;
    font-weight: 700;
    color: white;
}

.sidebar-text {
    color: #94a3b8;
    font-size: 14px;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    margin-top: 40px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# API
# -----------------------------
api_key = st.secrets.get("GROQ_API_KEY", "")

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.markdown(
        '<div class="sidebar-title">🎓 EduPro AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-text">Smart Teaching Assistant</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🧰 Teaching Tools")

    st.markdown("""
    <div style="color:#cbd5e1; line-height:2;">
    📝 Lesson Plan<br>
    ❓ Quiz & MCQs<br>
    📚 Topic Explanation<br>
    📋 Assignment<br>
    🎯 Learning Objectives<br>
    🧑‍🏫 Classroom Activities<br>
    📊 Assessment & Rubric<br>
    💡 Teaching Ideas
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.caption("Powered by Groq AI")

# -----------------------------
# HERO
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🎓 EduPro AI — Smart Teaching Assistant</h1>
    <p>
        Create lesson plans, quizzes, assignments, explanations,
        activities and teaching resources with AI.
    </p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# INPUT CARD
# -----------------------------
st.markdown("""
<div class="card">
<div class="card-title">✨ Create Teaching Material</div>
<div class="card-subtitle">
Choose a tool and provide a few details. EduPro AI will generate
professional educational content for you.
</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    tool = st.selectbox(
        "Teaching Tool",
        [
            "Lesson Plan",
            "Quiz & MCQs",
            "Topic Explanation",
            "Assignment",
            "Learning Objectives",
            "Classroom Activity",
            "Assessment & Rubric",
            "Teaching Ideas"
        ]
    )

with col2:
    subject = st.text_input(
        "Subject",
        placeholder="e.g. Computer Science"
    )

col3, col4 = st.columns(2)

with col3:
    grade = st.selectbox(
        "Class / Grade",
        [
            "Primary",
            "Class 5",
            "Class 6",
            "Class 7",
            "Class 8",
            "Class 9",
            "Class 10",
            "College",
            "University"
        ]
    )

with col4:
    difficulty = st.selectbox(
        "Difficulty Level",
        ["Easy", "Medium", "Hard"]
    )

topic = st.text_input(
    "Topic",
    placeholder="e.g. Artificial Intelligence"
)

extra = st.text_area(
    "Additional Instructions (Optional)",
    placeholder="Tell EduPro AI anything else you want...",
    height=120
)

st.markdown("<br>", unsafe_allow_html=True)

generate = st.button("✨ Generate with EduPro AI")

# -----------------------------
# GENERATION
# -----------------------------
if generate:

    if not api_key:
        st.error(
            "GROQ_API_KEY is missing. Please add your Groq API key "
            "in Streamlit Secrets."
        )
        st.stop()

    if not subject.strip():
        st.warning("Please enter a subject.")
        st.stop()

    if not topic.strip():
        st.warning("Please enter a topic.")
        st.stop()

    prompt = f"""
You are EduPro AI, a professional teaching assistant.

Create high-quality educational content.

Teaching Tool:
{tool}

Subject:
{subject}

Class / Grade:
{grade}

Difficulty:
{difficulty}

Topic:
{topic}

Additional Instructions:
{extra}

Requirements:
- Make the content suitable for the selected class.
- Use clear headings.
- Use bullet points and numbered lists where useful.
- Keep the language professional and easy to understand.
- Make the result practical for a teacher.
- Avoid unnecessary filler.
"""

    try:
        client = Groq(api_key=api_key)

        with st.spinner("EduPro AI is preparing your teaching material..."):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are EduPro AI, an expert educational "
                            "assistant for teachers."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2000
            )

        result = response.choices[0].message.content

        st.markdown("---")

        st.markdown("""
        <div class="card">
            <div class="card-title">📘 AI Generated Result</div>
            <div class="card-subtitle">
                Your teaching material is ready.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            f'<div class="output">{result.replace(chr(10), "<br>")}</div>',
            unsafe_allow_html=True
        )

        st.download_button(
            label="📥 Download Result",
            data=result,
            file_name="edupro_ai_result.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Something went wrong: {str(e)}")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<div class="footer">
    EduPro AI • Smart Teaching Assistant • Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)
