import streamlit as st

st.title("AI Interview Preparation Assistant")
st.write("Prepare for your interviews using AI assistance")

role = st.text_input("Enter Job Role")

if st.button("Generate Questions"):
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
        st.success("Answers submitted successfully!")
