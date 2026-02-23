import streamlit as st

# ---- CSS Styling ----
st.markdown("""
    <style>
        .main {
            background-color: #eef5ff;
        }
        .title {
            text-align: center;
            color: #003366;
            font-size: 45px;      /* Increased Title Size */
            font-weight: bold;
            margin-top: -10px;
        }
        .stButton > button {
            background-color: #003366 !important;
            color: white !important;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            font-size: 18px;
        }
        .stTextInput>div>div>input,
        .stTextArea textarea,
        .stSelectbox>div>div select {
            border: 2px solid #003366 !important;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Title ----
st.markdown("<p class='title'>TechFest Registration Form</p>", unsafe_allow_html=True)

# ---- Form ----
with st.form("techfest_form"):
    st.subheader("Personal Details")

    col1, col2, col3 = st.columns(3)
    with col1:
        first_name = st.text_input("First Name")
    with col2:
        middle_name = st.text_input("Middle Name")
    with col3:
        last_name = st.text_input("Last Name")

    email = st.text_input("Email")
    phone = st.text_input("Phone Number")

    age = st.number_input("Age", min_value=10, max_value=100, step=1)
    gender = st.radio("Gender", ["Male", "Female", "Other"])

    st.subheader("Academic Details")
    roll_no = st.text_input("Roll Number")
    department = st.selectbox(
        "Department",
        ["Computer Engineering", "IT", "ENTC", "Mechanical", "Civil",
         "Electrical", "AI & DS", "AIML", "Other"]
    )
    
    year = st.selectbox(
        "Year / Class",
        ["FE", "SE", "TE", "BE", "Diploma", "Other"]
    )

    college = st.text_input("College Name")

    st.subheader("Additional Information")
    address = st.text_area("Address")
    emergency = st.text_input("Emergency Contact Number")

    skills = st.multiselect(
        "Your Skills",
        ["Python", "Java", "C++", "Web Development", "Machine Learning",
         "Public Speaking", "Designing", "Networking", "Robotics"]
    )

    event_category = st.selectbox(
        "Event Category",
        ["Hackathon", "Coding Contest", "Project Competition",
         "Poster Presentation", "Robotics", "Gaming", "Technical Quiz"]
    )

    uploaded_photo = st.file_uploader("Upload Your Photo", type=["jpg", "png"])

    domains = [
        "Web Development", "AI / ML", "Data Science", "Cloud Computing",
        "Cyber Security", "IoT", "App Development", "Blockchain",
        "AR / VR", "Game Development", "UI / UX", "Robotics",
        "Software Testing", "DevOps", "Big Data", "Embedded Systems",
        "Digital Marketing", "Database Management", "Python Programming",
        "Java Development", "C++ Development", "Automation",
        "Quantum Computing"
    ]
    domain = st.selectbox("Interested Domain", domains)

    submit_btn = st.form_submit_button("Submit")

# ---- Output ----
if submit_btn:
    st.success("🎉 Registration Successful!")
    st.write("### Submitted Details:")
    st.write(f"**Name:** {first_name} {middle_name} {last_name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Roll Number:** {roll_no}")
    st.write(f"**Department:** {department}")
    st.write(f"**Year:** {year}")
    st.write(f"**College:** {college}")
    st.write(f"**Address:** {address}")
    st.write(f"**Emergency Contact:** {emergency}")
    st.write(f"**Skills:** {", ".join(skills)}")
    st.write(f"**Event Category:** {event_category}")
    st.write(f"**Interested Domain:** {domain}")

    if uploaded_photo:
        st.image(uploaded_photo, width=150)