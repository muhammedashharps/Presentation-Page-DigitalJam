import streamlit as st

st.set_page_config(
    page_title="Perspective Matters 🔮",
    page_icon="📱",
    layout="wide"
)


page_bg_img = '''

<style> 
[data-testid="stHeader"] {
background-color: white;
}

</style

'''
st.markdown(page_bg_img,unsafe_allow_html =True)
# Set page config




# Custom CSS with improved color scheme
st.markdown("""
<style>
    body {
        color: #1E1E1E;
        background-color: #F5F5F5;
    }
    .main {
        padding: 2rem;
        border-radius: 10px;
        background-color: #FFFFFF;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        border: none;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stDownloadButton>button {
        background-color: #007BFF;  /* Changed to blue color */
        color: white;                /* Set text color to white */
        font-weight: bold;           /* Make text bold */
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 20px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;
        border: none;
        transition-duration: 0.4s;
    }
    .stDownloadButton>button:hover {
        background-color: #0056b3;  /* Darker blue on hover */
    }
    .feature-box {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    h1, h2, h3 {
        color: #2C3E50;
    }
    .footer-text {
        color: black;                 /* Set footer text color to black */
    }
    .warning-text {
        color: red;                  /* Change to the desired color for the warning */
        font-weight: bold;           /* Make warning text bold */
    }
    p {
        color: white;
    }
    .border {
        border-bottom: 2px solid #007BFF;  /* Add a blue bottom border */
        margin: 20px 0;                     /* Add margin for spacing */
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🔮 Perspective Matters")
st.subheader("Next Gen AI Debate App To Challenge Your Beliefs")


st.markdown('<div class="border"></div>', unsafe_allow_html=True)
st.download_button(label="Click Here To Download The Android App",
                       data=open("perspective_matters.apk", "rb").read(),
                       file_name="perspective_matters.apk",
                       mime="application/vnd.android.package-archive", )

# App description

st.divider()
st.title("🎥 Demos")

# Main content
col1, col2, col3 = st.columns([3, 3, 3])

with col1:
    video_file = open("org1.mp4", 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.subheader("AI's debating about whether AI is a threat :)")




with col2:
    # Placeholder for app screenshot
    video_file = open("vid2.mp4", 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.subheader("Let's here both sides of the topic: 'Internet Censorship")


with col3:
    video_file = open("vid3.mp4", 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.subheader("An Engaging Debate About Free Will")



# Additional information
st.divider()

# Add a border above the warning


# Warning message

st.markdown("---")
st.markdown('<p class="footer-text">©Digital Jam Hackathon</p>', unsafe_allow_html=True)
