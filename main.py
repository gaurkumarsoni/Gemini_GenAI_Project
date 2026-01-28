import streamlit as st
from streamlit_option_menu import option_menu
from gemini_utility import (get_gemini_response, get_image_caption, gemini_embed_text, gemini_qna_response)

# Page configuration
st.set_page_config(
    page_title="Gemini-AI",
    page_icon="🧠",
    layout="centered"
)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Gemini AI",
        options=[
            "ChatBot",
            "Image Captioning",
            "Embed Text",
            "Ask me anything"
        ],
        icons=[
            "chat-dots-fill",
            "image-fill",
            "textarea-t",
            "patch-question-fill"
        ],
        menu_icon="robot",
        default_index=0
    )

# ================= CHATBOT =================
if selected == "ChatBot":

    st.title("🤖 Gemini ChatBot")

    # Initialize memory
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    user_prompt = st.chat_input("Ask Gemini...")

    if user_prompt:
        # Save user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_prompt
        })

        st.chat_message("user").markdown(user_prompt)

        # Build Gemini contents from history
        contents = []
        for msg in st.session_state.messages:
            contents.append({
                "role": msg["role"],
                "parts": [{"text": msg["content"]}]
            })
        try:
            # Get Gemini response
            response = get_gemini_response(contents)

            # Save assistant reply
            st.session_state.messages.append({
                "role": "model",
                "content": response
            })

            st.chat_message("model").markdown(response)

        except Exception as e:
            st.error("⚠️ Gemini is currently overloaded. Please try again in a few seconds.")
            st.caption(str(e))

# ================= IMAGE CAPTIONING =================

if selected == "Image Captioning":

    st.title("🤖 Gemini Image Captioning")

    uploaded_image = st.file_uploader(
        "Upload an image..",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image is not None:


        if st.button("Generate Caption"):
            col1, col2 = st.columns(2)
            with col1:
                st.image(uploaded_image, caption="Uploaded Image", width="stretch")
            with col2:
                with st.spinner("Gemini is analyzing the image..."):
                    try:
                        image_bytes = uploaded_image.getvalue()
                        caption = get_image_caption(image_bytes)
                        st.success(caption)

                    except Exception as e:
                        st.error("⚠️ Gemini is currently overloaded. Please try again in a few seconds.")
                        st.caption(str(e))
    else:
        st.info("👆 Upload an image to get started.")


# ================= TEXT EMBEDDING =================

if selected == "Embed Text":

    st.title("🔡 Embed Text")

    text_input = st.text_area(label="", placeholder="Write something to embed")
    if st.button("embed_text"):
        embedded_result = gemini_embed_text(text_input)
        st.markdown(embedded_result)

# ================= ASK ME ANYTHING (QNA) =================

if selected == "Ask me anything":
    st.title("❓ Ask me a question.")
    text_input = st.text_area(label="", placeholder="Ask me anything...")
    if st.button("Get and answer"):
        response = gemini_qna_response(text_input)
        st.markdown(response)


