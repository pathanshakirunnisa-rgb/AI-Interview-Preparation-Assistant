import streamlit as st

st.title("AI Interview Preparation Assistant")
st.write("Prepare for your interviews using AI assistance")

role = st.text_input("Enter Job Role")

# Store questions and answers in session_state
if "questions" not in st.session_state:
    st.session_state.questions = []
if "answers" not in st.session_state:
    st.session_state.answers = []

if st.button("Generate Questions"):

    if "data" in role.lower():
        st.session_state.questions = [
            "What is machine learning?",
            "Explain supervised vs unsupervised learning.",
            "What is overfitting?"
        ]

    elif "web" in role.lower():
        st.session_state.questions = [
            "What is HTML, CSS, and JavaScript?",
            "Explain REST APIs.",
            "What is responsive design?"
        ]

    elif "python" in role.lower():
        st.session_state.questions = [
            "Explain Python data types.",
            "What are Python decorators?",
            "Explain list vs tuple."
        ]

    else:
        st.session_state.questions = [
            f"What is your experience in {role}?",
            f"What are the important skills required for {role}?",
            f"Explain one project related to {role}"
        ]

    # Reset previous answers
    st.session_state.answers = [""] * len(st.session_state.questions)

# Display questions and collect answers
if st.session_state.questions:
    st.subheader("Interview Questions")
    for i, q in enumerate(st.session_state.questions):
        st.write(q)
        st.session_state.answers[i] = st.text_area(f"Your Answer {i+1}", st.session_state.answers[i])

# Submit answers and calculate scores
if st.button("Submit Answers") and st.session_state.answers:
    st.subheader("Answer Scores")
    keywords = ["python", "project", "experience", "skills"]

    for i, ans in enumerate(st.session_state.answers):
        word_score = len(ans.split())
        keyword_score = sum([1 for k in keywords if k in ans.lower()])
        final_score = word_score + (keyword_score * 5)
        st.write(f"Answer {i+1} Score: {final_score}")
