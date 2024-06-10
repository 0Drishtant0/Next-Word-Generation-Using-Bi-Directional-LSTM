import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import streamlit as st

# Load the model
model = load_model('my_model.h5')

# Load the tokenizer
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Add heading
st.title("Word Generation using Bi-LSTM", anchor='center')

# Rest of the code...
seed_text = st.text_input("Enter seed text:", "we visited a restaurant when")
next_words = st.number_input("Enter number of next words:", min_value=1, max_value=10, value=2)

max_sequence_len = 40

# Rest of the code...
for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted = model.predict(token_list, verbose=0)
    predicted = np.argmax(predicted)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word
    st.markdown(f"<span>{output_word}</span>", unsafe_allow_html=True)

st.markdown(f"<span> {seed_text}</span>", unsafe_allow_html=True)
