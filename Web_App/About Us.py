import streamlit as st
st.set_page_config(page_title="About Us")
st.title("Meet the Team!")

phillip, videsh, edison = st.columns(3)


#header = st.container()
#with header:
    

with phillip:
    st.header("Phillip Park")
    st.image("./Assets/default-avatar.png")
    st.subheader("R & D Lead")
    st.write("Introduction here...")
    st.markdown("[LinkedIn](#)")

with videsh:
    st.header("Videsh Narine")
    st.image("./Assets/default-avatar.png")
    st.subheader("Engineering Lead")
    st.write("Introduction here...")
    st.markdown("[LinkedIn](#)")

with edison:
    st.header("Edison Enerio")
    st.image("./Assets/default-avatar.png")
    st.subheader("Project Lead")
    st.write("Introduction here...")
    st.markdown('[LinkedIn](https://www.linkedin.com/in/edison-enerio)')