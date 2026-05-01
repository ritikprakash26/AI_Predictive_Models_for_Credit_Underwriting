import streamlit as st
from styles import apply_styles
def show():
    apply_styles()
    st.title("👨‍💻 About Me")
    
    st.markdown("""
    ## Hi there! I'm **Ritik Prakash**, a AI & Machine Learning Enthusiast 🚀
    
    ### 🌟 Key Areas of Interest:
    - Artificial Intelligence (AI)
    - Machine Learning (ML)
    
    ### 📬 Let's Connect:
    - **LinkedIn**: [Ritik Prakash](https://www.linkedin.com/in/ritik-prakash-226595360?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
    - **GitHub**: [ritikprakash26](https://github.com/ritikprakash26)
    - **Email**: [ritikprakash26@gmail.com](mailto:ritikprakash26@gmail.com)

    Feel free to reach out for collaborations, learning, or discussions on anything AI & ML-related!
    """)

    st.markdown("___")
    st.markdown("I'm always excited to connect with like-minded individuals and share knowledge!")
