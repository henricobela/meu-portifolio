import streamlit as st

def localize_path_logo():
    path_logo = ""
    path_to_logo = {
        "path_one": "app/utils/imgs/me.png",
        "path_two": "utils/imgs/me.png"}
    
    for path in path_to_logo.values():
        try:
            open(path)
            path_logo = path
        except:
            continue
    return path_logo

def home():
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        st.image(localize_path_logo())
    with col_txt:
        st.header("Henrico Nardelli Bela")
        st.subheader("Data Scientist")
    st.info("This portfolio was built in order to demonstrate my skills in machine learning and deep learning. Feel free to contact me to ask questions and chat!")
    st.markdown("---")

    st.text("Checkout my social medias!")
    col_linkedin, col_wpp, col_face = st.columns([1, 1, 1])
    with col_linkedin:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/henricobela)")
        st.markdown("[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/henricobela)")
        st.markdown("[![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)](https://www.figma.com/@henrico)")
    with col_wpp:
        st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/message/ZUQNVK6VIT6RC1)")
        st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:henrico.developer@gmail.com)")
        st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://instagram.com/henricobela)")
    with col_face:
        st.markdown("[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://web.facebook.com/henrico.bela)")
        st.markdown("[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/m4UKn6SGw5)")
        st.markdown("[![Twitch](https://img.shields.io/badge/Twitch-%239146FF.svg?style=for-the-badge&logo=Twitch&logoColor=white)](https://twitch.tv/henricobela)")
        