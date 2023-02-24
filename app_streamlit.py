"""
This app is about take a image and return a image inferenced using YOLOv5
"""

import streamlit as st
from PIL import Image
import torch

DEFAULT_IMAGE_SIZE = (640, 480)

def main(model: torch.hub):
    # Display default image before user uploads an image
    # Allow user to upload an image
    uploaded_image = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])
    
    if uploaded_image is not None:
        # Read the uploaded image and convert it to RGB format
        uploaded_image = Image.open(uploaded_image)
        uploaded_image = uploaded_image.convert('RGB')
        
        # Resize the uploaded image to the default image size
        uploaded_image = uploaded_image.resize(DEFAULT_IMAGE_SIZE)
        
        # Display the uploaded image
        st.image(uploaded_image, caption='Uploaded Image')
    else:
        # Display default image
        default_image = Image.new('RGB', DEFAULT_IMAGE_SIZE, color='white')
        st.image(default_image, caption='Default Image')

if __name__ == '__main__':
    # 사전 학습된 모델 뽑아내기
    model = torch.hub.load('ultralytics/yolov5', 'yolov5l6')  # or yolov5n, yolov5x6, custom
    
    main(model)
