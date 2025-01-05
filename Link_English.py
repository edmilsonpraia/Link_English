import streamlit as st
import pandas as pd
import plotly.express as px
st.markdown("""<style>.main {padding: 2rem;}.stButton > button {width: 100%;margin-bottom: 1rem;padding: 0.5rem;border-radius: 0.5rem;}.question-box {background-color: #f8f9fa;padding: 2rem;border-radius: 1rem;margin-bottom: 2rem;}.result-box {text-align: center;padding: 2rem;background-color: #f1f8ff;border-radius: 1rem;margin: 2rem 0;}</style>""", unsafe_allow_html=True)
questions = [
    {"question": "What is the plural of 'child'?", "options": ["childs", "children", "childes"], "correct": 1},
    {"question": "Choose the correct sentence:", "options": ["She go to school.", "She goes to school.", "She going to school."], "correct": 1},
    {"question": "What is the opposite of 'hot'?", "options": ["cold", "warm", "big"], "correct": 0},
    {"question": "Complete the sentence: 'I ___ a student.'", "options": ["am", "is", "are"], "correct": 0},
    {"question": "Which word is a color?", "options": ["apple", "blue", "run"], "correct": 1},
    {"question": "What is the past tense of 'eat'?", "options": ["eated", "ate", "eaten"], "correct": 1},
    {"question": "Choose the correct question:", "options": ["Where you live?", "Where do you live?", "Where does you live?"], "correct": 1},
    {"question": "What is the meaning of 'happy'?", "options": ["sad", "angry", "joyful"], "correct": 2},
    {"question": "Which sentence is correct?", "options": ["He don't like pizza.", "He doesn't likes pizza.", "He doesn't like pizza."], "correct": 2},
    {"question": "What is the plural of mouse?", "options": ["Mice", "Mouse", "Mouses"], "correct": 0},
    {"question": "Choose the correct phrasal verb: 'Please, ___ the lights before leaving.'", "options": ["turn on", "turn off", "turn up"], "correct": 1},
    {"question": "What is the synonym of 'intelligent'?", "options": ["smart", "lazy", "funny"], "correct": 0},
    {"question": "Complete the sentence: 'If I ___ rich, I would travel the world.'", "options": ["am", "was", "were"], "correct": 2},
    {"question": "Which sentence is in the present perfect tense?", "options": ["I have finished my homework.", "I finished my homework.", "I finish my homework."], "correct": 0},
    {"question": "What does the expression 'break the ice' mean?", "options": ["to start a conversation", "to end a relationship", "to fix something"], "correct": 0},
    {"question": "Choose the correct comparative form: 'This book is ___ than that one.'", "options": ["interesting", "more interesting", "most interesting"], "correct": 1},
    {"question": "What is the past participle of 'write'?", "options": ["wrote", "written", "writed"], "correct": 1},
    {"question": "Which sentence is correct?", "options": ["She has been working here since 5 years.", "She has been working here for 5 years.", "She has been working here since 5 years ago."], "correct": 1},
    {"question": "What is the meaning of 'boring'?", "options": ["exciting", "not interesting", "funny"], "correct": 1},
    {"question": "Choose the correct tag question: 'You like coffee, ___?'", "options": ["don't you", "do you", "aren't you"], "correct": 0},
    {"question": "What is the meaning of 'to hit the nail on the head'?", "options": ["to make a mistake", "to describe something exactly right", "to hurt someone"], "correct": 1},
    {"question": "Choose the correct conditional sentence:", "options": ["If I had known, I would have helped you.", "If I know, I will help you.", "If I knew, I would help you."], "correct": 0},
    {"question": "What is the passive voice of: 'Someone stole my wallet.'", "options": ["My wallet was stolen.", "My wallet is stolen.", "My wallet has been stolen."], "correct": 0},
    {"question": "Which word is a synonym of 'exhausted'?", "options": ["tired", "energetic", "excited"], "correct": 0},
    {"question": "What does the idiom 'piece of cake' mean?", "options": ["something difficult", "something easy", "something delicious"], "correct": 1},
    {"question": "Choose the correct sentence:", "options": ["Despite of the rain, we went out.", "Despite the rain, we went out.", "Despite the rain, we go out."], "correct": 1},
    {"question": "What is the meaning of 'to let the cat out of the bag'?", "options": ["to reveal a secret", "to lose something", "to adopt a pet"], "correct": 0},
    {"question": "Which sentence uses the passive voice correctly?", "options": ["She is reading a book.", "The book is read her.", "The book is being read by her."], "correct": 2},
    {"question": "Choose the correct comparative:", "options": ["Better", "More good", "The best"], "correct": 0},
    {"question": "Choose the correct sentence:", "options": ["Hardly had I arrived when the meeting started.", "Hardly I had arrived when the meeting started.", "Hardly had I arrived when the meeting had started."], "correct": 0}
]
def calculate_level(score, total_questions):
    percentage = (score / total_questions) * 100
    if percentage >= 90: return "C2 - Proficient", "Você tem domínio completo do inglês!"
    elif percentage >= 80: return "C1 - Advanced", "Você tem um nível avançado de inglês!"
    elif percentage >= 70: return "B2 - Upper Intermediate", "Você tem um bom domínio do inglês!"
    elif percentage >= 60: return "B1 - Intermediate", "Você tem um nível intermediário de inglês!"
    elif percentage >= 40: return "A2 - Elementary", "Você está no caminho certo! Continue estudando!"
    else: return "A1 - Beginner", "Você está começando! Não desanime!"
def main():
    st.title("Link English 📝")
    st.markdown("### Descubra seu nível de inglês!")
    if 'current_question' not in st.session_state: st.session_state.current_question = 0
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'answers' not in st.session_state: st.session_state.answers = []
    if 'test_complete' not in st.session_state: st.session_state.test_complete = False
    if not st.session_state.test_complete:
        progress = st.session_state.current_question / len(questions)
        st.progress(progress)
        st.markdown(f"**Questão {st.session_state.current_question + 1} de {len(questions)}**")
        current_q = questions[st.session_state.current_question]
        with st.container():
            st.markdown(f"### {current_q['question']}")
            for i, option in enumerate(current_q['options']):
                if st.button(f"{chr(97 + i)}) {option}", key=f"option_{i}", use_container_width=True):
                    correct = (i == current_q['correct'])
                    if correct: st.session_state.score += 1
                    st.session_state.answers.append({'question': current_q['question'], 'answered': i, 'correct': correct})
                    st.session_state.current_question += 1
                    if st.session_state.current_question >= len(questions): st.session_state.test_complete = True
                    st.rerun()
    else:
        score = st.session_state.score
        level, message = calculate_level(score, len(questions))
        st.markdown(f"""<div class='result-box'><h1 style='color: #0066cc;'>Seu Nível: {level}</h1><h2>Pontuação: {score}/{len(questions)}</h2><p style='font-size: 1.2em;'>{message}</p></div>""", unsafe_allow_html=True)
        df = pd.DataFrame(st.session_state.answers)
        fig = px.pie(names=['Corretas', 'Incorretas'], values=[score, len(questions) - score], title='Seu Desempenho', color_discrete_sequence=['#00cc66', '#ff6666'])
        st.plotly_chart(fig)
        if st.button("📝 Fazer o teste novamente"):
            for key in st.session_state.keys(): del st.session_state[key]
            st.rerun()
        st.markdown("### Análise Detalhada")
        df['result'] = df['correct'].map({True: '✅ Correto', False: '❌ Incorreto'})
        st.dataframe(df[['question', 'result']], hide_index=True, column_config={"question": "Questão", "result": "Resultado"})
if __name__ == "__main__": main()