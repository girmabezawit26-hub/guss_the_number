import streamlit as st
import random
st.title("guss the number")
st.write("i am thinking of a number about 1 and 20. ")
if "secret" not in st.session_state:
    st.session_state.secret= random.randint(1,20)
guss= st.number_input("whats you guss ediot?", min_value=1
                     ,max_value=20,
                     step=1)
if st.button("guss!"):
    if guss==st.session_state.secret:
        st.success("you got it, boring")
    elif guss < st.session_state.secret:
        st.info("always too low try higher, youii like it")
    else:
       st. warning("too high, are you drunk")
if st.button("new game"):
    st.session_state.secret=random.randint(1,20)
    st.rerun()
