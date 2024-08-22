import streamlit as st

# Title of the app
st.title('Kaphaアンバランス度診断アプリ')

# Instructions
st.write('以下の質問にお答えください。各質問に最も当てはまる答えを選んでください。')

# Questions from the Excel file
questions = [
    "体が重く、何事もおっくうである",
    "寒く、湿気が多い気候になると体調が悪い",
    "手足がだるかったり、関節の痛みがある",
    "口内が甘い。あるいは口中がネバネバする",
    "食事を抜いても苦にならない",
    "風邪気味で鼻みずや鼻づまりがぬけない",
    "たんが出る咳が多い",
    "すぐに居眠りやうつらうつらしてしまう",
    "少なくても8時間はぐっすり寝てしまう",
    "みみずばれのような発疹ができやすい",
    # Add additional questions here
]

# Mapping response options to their corresponding scores
options = {
    "当てはまる": 4,
    "まあまあ当てはまる": 3,
    "どちらともいえない": 2,
    "あまり当てはまらない": 1,
    "当てはまらない": 0,
}

# Initialize the total score
total_score = 0

# Display questions and collect responses
for question in questions:
    response = st.radio(question, list(options.keys()), key=question)
    total_score += options[response]

# Button to view the diagnosis
if st.button('診断結果を見る'):
    # Calculate the score as a percentage of the maximum score (40)
    percentage_score = (total_score / 40) * 100

    # Display the result based on the percentage
    st.write("## 診断結果")

    if percentage_score <= 20:
        st.success("安定している状態です。この状態を維持するように心がけてください。")
    elif percentage_score <= 40:
        st.info("比較的安定している状態です。乱れが多く出ないように心がけてください。")
    elif percentage_score <= 60:
        st.warning("乱れが少し出ている状態です。安定化に向けて心がけてください。")
    elif percentage_score <= 80:
        st.warning("乱れが多く出ている状態です。安定化に向けて積極的に対応してください。")
    else:
        st.error("とても乱れている状態です。改善に向けて迅速に対応してください。")

    st.write(f"あなたのスコアは: {total_score} / 40 ({percentage_score:.2f}%)")
