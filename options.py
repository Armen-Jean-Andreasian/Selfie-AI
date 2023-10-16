import streamlit as st
import cv2
from datetime import datetime

current_time = datetime.now()


class Options:

    @staticmethod
    def live_image(image: bytes, frame):
        if image is not None:
            frame.image(image)
        else:
            pass

    @staticmethod
    def download_image(my_frame):
        if my_frame is not None:
            st.download_button(label="Download Image", data=my_frame, file_name='picture.jpg', mime='image/jpeg')

    @staticmethod
    def time_stamp(frame_to_stamp):
        date_now = current_time.strftime("%d-%m-%Y")
        time_now = current_time.strftime("%H:%M:%S")
        day_of_week = current_time.strftime("%A")

        def place_text(frame, text, org, color):
            cv2.putText(img=frame, text=text, org=org,
                        fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=color,
                        thickness=2, lineType=cv2.LINE_AA)

        place_text(frame=frame_to_stamp, text=date_now, org=(20, 50), color=(255, 255, 255))
        place_text(frame=frame_to_stamp, text=time_now, org=(20, 100), color=(255, 255, 255))
        place_text(frame=frame_to_stamp, text=day_of_week, org=(20, 150), color=(255, 0, 0))
