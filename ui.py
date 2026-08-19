import streamlit as st 
from YoutubeAnalyzer import youtube_agent

st.set_page_config(page_title="YouTube Video Analyzer", layout="centered")
st.title("🎥 AI YouTube Video Analyzer")


#cache 
def get_agent():
    return youtube_agent()

agent = get_agent()

#input box 
video_url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=example")
button = st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing video..."):
        response = agent.run(f"Analyze this video: {video_url}")
    
    
    st.markdown("### Analysis Result:")
    st.markdown(response.content)