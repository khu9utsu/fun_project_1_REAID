import streamlit as st
import random
import time

# Set page configuration
st.set_page_config(
    page_title="Kuis Python Dasar",
    page_icon="🐍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS untuk animasi dan styling
st.markdown("""
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
  * {
    font-family: 'Montserrat', sans-serif;
    }
  .main {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
    border-radius: 15px;
  }
  .stButton>button {
      background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
      color: white;
      font-weight: bold;
      border: none;
      border-radius: 25px;
      adding: 12px 30px;
      margin: 10px 0;
      cursor: pointer;
      transition: all 0.3s ease;
      box-shadow: 0 4px 15px 0 rgba(0, 0, 0, 0.2);
      width: 100%;
  }    
  .stButton>button:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
      background: linear-gradient(to right, #00f2fe 0%, #4facfe 100%);
  }
    
  .stButton>button:disabled {
      background: rgba(255, 255, 255, 0.3);
      transform: none;
      box-shadow: none;
      cursor: not-allowed;
    }    
  .score-display {
      font-size: 1.4em;
      font-weight: bold;
      color: white;
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
      animation: pulse 2s infinite;
  }    
  .title {
      color: white;
      text-align: center;
      font-size: 2.8em;
      font-weight: 700;
      margin-bottom: 10px;
      text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
      animation: bounce 1.5s ease infinite;
  }
  .subtitle {
      color: white;
      text-align: center;
      font-size: 1.2em;
      margin-bottom: 30px;
      animation: fadeIn 2s ease;
  }
  .option-button {
      transition: all 0.3s ease !important;
  }
  .option-button:hover {
      transform: scale(1.03) !important;
  }
  .celebration {
      display: flex;
      justify-content: center;
      margin: 20px 0;
      font-size: 3em;
      animation: celebrate 1s ease infinite;
  }
  .progress-bar {
      height: 10px;
      border-radius: 5px;
      background: rgba(255, 255, 255, 0.3);
      margin: 20px 0;
      overflow: hidden;
    }
  .progress-fill {
      height: 100%;
      border-radius: 5px;
      background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
      transition: width 0.5s ease;
  }
    
  @keyframes fadeIn {
      from { 
        opacity: 0; 
          transform: translateY(20px); 
      }
      to { 
          opacity: 1; 
          transform: translateY(0); 
      }
  }
    
  @keyframes pulse {
      0% { 
          transform: scale(1); 
      }
      50% { 
          transform: scale(1.05); 
      }
      100% { 
          transform: scale(1); 
      }
  }
    
  @keyframes bounce {
      0%, 100% { 
          transform: translateY(0); 
      }
      50% { 
          transform: translateY(-10px); 
      }
  }
    
  @keyframes celebrate {
      0%, 100% { 
          transform: scale(1); 
      }
      50% { 
          transform: scale(1.2); 
      }
  }
    
  @keyframes confetti {
      0% {
          transform: translateY(0) rotate(0);
          opacity: 1;
      }
      100% {
          transform: translateY(100vh) rotate(720deg);
          opacity: 0;
      }
  }
    
  .confetti {
      position: fixed;
      width: 10px;
      height: 10px;
      opacity: 0;
      pointer-events: none;
  }
  .firework {
      position: fixed;
      width: 5px;
      height: 5px;
      border-radius: 50%;
      pointer-events: none;
      opacity: 0;
  }
  </style>
    """, unsafe_allow_html=True)

# Data pertanyaan kuis
questions = [
    {
      "question": "Manakah cara yang benar untuk membuat fungsi di Python?",
      "options": [
          "def my_function():",
          "function my_function():",
          "create my_function():",
          "define my_function():"
      ],
      "correct_answer": "def my_function():",
      "explanation": "Di Python, fungsi didefinisikan menggunakan kata kunci 'def' diikuti dengan nama fungsi dan tanda kurung."
    },
    {
      "question": "Apa output dari: print(3 * 'hi'?)",
      "options": [
          "hihihi",
          "3hi",
          "Error",
          "hi hi hi"
      ],
      "correct_answer": "hihihi",
      "explanation": "Di Python, mengalikan string dengan integer akan mengulang string sebanyak nilai integer tersebut."
    },
    {
      "question": "Metode apa yang digunakan untuk menghapus elemen terakhir dari list?",
      "options": [
          "remove()",
          "pop()",
          "delete()",
          "cut()"
      ],
      "correct_answer": "pop()",
      "explanation": "Metode pop() menghapus dan mengembalikan elemen terakhir dari list jika tidak ada index yang ditentukan."
    }
]

# Inisialisasi state kuis
def initialize_quiz():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = None
    if 'answered' not in st.session_state:
        st.session_state.answered = False
    if 'questions' not in st.session_state:
        st.session_state.questions = random.sample(questions, min(5, len(questions)))
    if 'start_time' not in st.session_state:
        st.session_state.start_time = time.time()
    if 'quiz_complete' not in st.session_state:
        st.session_state.quiz_complete = False

# Animasi konfetti sederhana
def show_confetti():
    confetti_html = st.markdown("<div class='celebration'>🎉 🎊 🐍 🥳 🎈</div>", unsafe_allow_html=True)

# Pindah ke pertanyaan berikutnya
def next_question():
    if st.session_state.current_question < len(st.session_state.questions) - 1:
        st.session_state.current_question += 1
        st.session_state.selected_option = None
        st.session_state.answered = False
    else:
        st.session_state.quiz_complete = True
        st.session_state.end_time = time.time()

# Periksa jawaban
def check_answer(selected_option):
    st.session_state.selected_option = selected_option
    current_q = st.session_state.questions[st.session_state.current_question]
    if selected_option == current_q['correct_answer']:
        st.session_state.score += 1
    st.session_state.answered = True

# Mulai ulang kuis
def restart_quiz():
    for key in st.session_state.keys():
        del st.session_state[key]
    initialize_quiz()

# Fungsi utama
def main():
    initialize_quiz()

    # Judul dengan animasi
    st.markdown("<h1 class='title'>🐍 Kuis Python Interaktif</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Uji pengetahuan Pythonmu dengan kuis seru ini!</p>", unsafe_allow_html=True)

    # Progress bar
    progress = (st.session_state.current_question + 1) / len(st.session_state.questions)
    st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    """, unsafe_allow_html=True)

    # Tampilkan skor dan progress
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='score-display'>Pertanyaan: {st.session_state.current_question + 1}/{len(st.session_state.questions)}</div>", 
            unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='score-display' align='right'>Skor: {st.session_state.score}</div>", 
        unsafe_allow_html=True)

    # Tampilkan pertanyaan jika kuis belum selesai
    if not st.session_state.quiz_complete:
        current_q = st.session_state.questions[st.session_state.current_question]
        st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress * 100}%"></div>
        </div>
    """, unsafe_allow_html=True)
        st.markdown(f"<h3>{current_q['question']}</h3>", unsafe_allow_html=True)

    # Tampilkan opsi sebagai button dengan animasi
        for option in current_q['options']:
            if st.button(option, key=option, use_container_width=True, 
                        disabled=st.session_state.answered,
                        on_click=check_answer, args=(option,)):
                pass

    # Tampilkan penjelasan jika sudah dijawab
        if st.session_state.answered:
            if st.session_state.selected_option == current_q['correct_answer']:
                st.success("✅ Benar! " + current_q['explanation'])

            # Animasi untuk jawaban benar
                st.balloons()
            else:
                st.error(f"❌ Salah. Jawaban yang benar: {current_q['correct_answer']}")
                st.info("💡 Penjelasan: " + current_q['explanation'])

            # Button pertanyaan berikutnya
            st.button("Pertanyaan Berikutnya →", on_click=next_question)
            st.markdown("</div>", unsafe_allow_html=True)

    else:
        # Kuis selesai
        time_taken = round(st.session_state.end_time - st.session_state.start_time, 2)
        
        # Tampilkan animasi konfetti
        show_confetti()
        st.balloons()
        
        st.subheader("🎉 Kuis Selesai!")
        st.markdown(f"**Skor Akhir: {st.session_state.score}/{len(st.session_state.questions)}**")
        st.markdown(f"**Waktu: {time_taken} detik**")
        
        # Pesan performa
        percentage = (st.session_state.score / len(st.session_state.questions)) * 100
        if percentage == 100:
            st.success("Sempurna! Anda ahli Python! 🐍")
        elif percentage >= 50:
            st.warning("Usaha yang baik! Terus belajar dan berlatih!")
        else:
            st.info("Terus pelajari Python! Anda akan semakin baik dengan latihan!")
        
        # Button restart
        st.button("🔄 Mulai Kuis Lagi", on_click=restart_quiz)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Info di sidebar
    with st.sidebar:
        st.header("ℹ️ Tentang Kuis")
        st.info("Kuis ini menguji pengetahuan dasar Python. Jawablah pertanyaan dengan memilih opsi yang benar!")
        
        st.header("💡 Tips")
        st.markdown("- Baca setiap pertanyaan dengan seksama\n"
            "- Pertimbangkan semua opsi sebelum menjawab\n"
            "- Pelajari penjelasan untuk setiap jawaban")
        
        st.header("🔧 Dibuat dengan")
        st.markdown("- Python\n- Streamlit\n- HTML/CSS")
        
        st.header("©️ Andri Purnama 2025")

if __name__ == "__main__":
    main()