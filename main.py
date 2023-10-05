import streamlit as st
import cv2
from face_recognition import detect_faces
from options import time_stamp, live_image, download_image


class PhotoAPP:
    def __init__(self):
        self.title = None
        self.camera = None
        self.image_widget = None
        self.shot_button = None


    def main(self):
        with st.expander("Selfie with Face Recognition"):
            self.title = st.title("Selfie with AI")
            if st.button('Start / Reload'):

                st.selectbox("", options=("Enable date", "Disable date"), key="user_date_choice", index=0)
                st.selectbox("", options=("Enable recognition", "Disable recognition"), key="user_recognition_choice",
                             index=0)

                self.camera = cv2.VideoCapture(0)
                self.image_widget = st.image([])
                self.shot_button = st.button("Snap")


                while True:
                    check, current_frame = self.camera.read()
                    current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)

                    if st.session_state["user_date_choice"] == "Enable date":
                        time_stamp(frame_to_stamp=current_frame)

                    if st.session_state["user_recognition_choice"] == "Enable recognition":
                        frame_with_detection = detect_faces(current_frame)
                        live_image(frame=self.image_widget, image=frame_with_detection)

                    elif st.session_state["user_recognition_choice"] == "Disable recognition":
                        live_image(frame=self.image_widget, image=current_frame)

                    if self.shot_button and check:
                        rgb_frame = cv2.cvtColor(current_frame, cv2.COLOR_RGB2BGR)
                        _, buffer = cv2.imencode('.jpg', rgb_frame)
                        shot = buffer.tobytes()
                        break

                download_image(shot)


if __name__ == '__main__':
    app = PhotoAPP()
    app.main()
