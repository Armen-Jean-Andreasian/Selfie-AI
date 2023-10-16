import streamlit as st
import cv2
from face_recognition import Recognize
from options import Options


class PhotoAPP:
    def __init__(self):
        self.title = None
        self.camera = None
        self.image_widget = None
        self.shot_button = None

    def initialize_camera(self):
        self.camera = cv2.VideoCapture(0)
        self.image_widget = st.image([])
        self.shot_button = st.button("Snap")
        st.selectbox("", options=("Enable date", "Disable date"), key="user_date_choice", index=0)
        st.selectbox("", options=("Enable recognition", "Disable recognition"), key="user_recognition_choice", index=0)

    def capture_frame(self):
        while True:
            check, current_frame = self.camera.read()
            current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
            if st.session_state["user_date_choice"] == "Enable date":
                Options.time_stamp(frame_to_stamp=current_frame)
            if st.session_state["user_recognition_choice"] == "Enable recognition":
                frame_with_detection = Recognize.detect_faces(current_frame)
                Options.live_image(frame=self.image_widget, image=frame_with_detection)
            elif st.session_state["user_recognition_choice"] == "Disable recognition":
                Options.live_image(frame=self.image_widget, image=current_frame)
            if self.shot_button and check:
                rgb_frame = cv2.cvtColor(current_frame, cv2.COLOR_RGB2BGR)
                _, buffer = cv2.imencode('.jpg', rgb_frame)
                shot = buffer.tobytes()
                break
        return shot

    def main(self):
        with st.expander("Selfie with Face Recognition"):
            self.title = st.title("Selfie with AI")
            if st.button('Start / Reload'):
                try:
                    self.initialize_camera()
                    shot = self.capture_frame()
                    Options.download_image(shot)
                except Exception:
                    st.error(
                        "Camera not detected: Please ensure that the camera is connected and that camera permissions are set correctly.")


if __name__ == '__main__':
    app = PhotoAPP()
    app.main()
