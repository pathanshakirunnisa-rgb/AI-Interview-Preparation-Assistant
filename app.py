import streamlit as st

st.title("AI Interview Preparation Assistant")
st.write("Prepare for your interviews using AI assistance")

role = st.text_input("Enter Job Role")

if st.button("Generate Questions"):

    if "data" in role.lower():
        questions = [
            "What is machine learning?",
            "Explain supervised vs unsupervised learning.",
            "What is overfitting?"
        ]

    elif "web" in role.lower():
        questions = [
            "What is HTML, CSS, and JavaScript?",
            "Explain REST APIs.",
            "What is responsive design?"
        ]

    elif "python" in role.lower():
        questions = [
            "Explain Python data types.",
            "What are Python decorators?",
            "Explain list vs tuple."
        ]

    else:
        questions = [
            f"What is your experience in {role}?",
            f"What are the important skills required for {role}?",
            f"Explain one project related to {role}"
        ]

    st.subheader("Interview Questions")

    answers = []

    for i, q in enumerate(questions):
        st.write(q)
        ans = st.text_area(f"Your Answer {i+1}")
        answers.append(ans)

    if st.button("Submit Answers"):
    st.subheader("Answer Scores")

    keywords = ["python", "project", "experience", "skills"]

    for i, ans in enumerate(answers):
        word_score = len(ans.split())
        keyword_score = sum([1 for k in keywords if k in ans.lower()])

        final_score = word_score + (keyword_score * 5)

        st.write(f"Answer {i+1} Score: {final_score}")

