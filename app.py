import streamlit as st
import pickle
movies_list = pickle.load(open('movie_list.pkl', 'rb'))
#movies=pd.DataFrame(movies_list)
st.title('Movie Recomender System')

option= st.selectbox(
    'Which movie do you want to recommend?',movie_list
)

