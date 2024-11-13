import streamlit as st
import pandas as pd

# Load the dataset
data = pd.read_csv('dataset.csv')
st.write(data)  # Display the data in Streamlit
data2=pd.read_csv('dataset2.csv')
st.write(data2)


# Custom CSS for hover effect on images
st.markdown("""
    <style>
        .image-container img {
            transition: transform 0.3s ease;  /* Add smooth transition */
        }
        .image-container img:hover {
            transform: scale(1.1);  /* Zoom in effect on hover */
        }
        .image-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }
        .movie-title {
            text-align: center;
            color: #fff;
            margin-top: 5px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Displaying images and titles
for index, row in data.iterrows():
    st.markdown(f"""
        <div class="image-container">
            <img src="{row['image_url']}" alt="{row['title']}" width="150">
            <div class="movie-title">{row['title']}</div>
        </div>
    """, unsafe_allow_html=True)
