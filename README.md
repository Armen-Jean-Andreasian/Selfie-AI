# Selfie-AI
![image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftalkjarvis.com%2Fwp-content%2Fuploads%2F2019%2F12%2F1-1.jpg&f=1&nofb=1&ipt=f97256ba48e23d92004bcc7c20e20b8e54ced69c68c2cb85c6fc1e7d99743414&ipo=images)

This is a selfie camera app that incorporates Face Recognition capabilities. 
The app allows users to capture selfies using their device's camera and apply face recognition to identify faces in the images. 


## Features

The SelfieCamera-with-FaceRecognition app offers the following features:

1. **Enable Recognition**: This mode enables face recognition functionality. When capturing a selfie, the app will detect faces in the image and display the recognized faces along with their names (if known).

2. **Disable Recognition**: This mode disables face recognition. Users can still capture selfies, but the app will not perform any face recognition.

3. **Enable Date**: This mode enables the display of the current date and time on the captured selfie.

4. **Disable Date**: This mode disables the display of the date and time on the captured selfie.

## Installation and Setup

To use the SelfieCamera-with-FaceRecognition app, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Armen-Jean-Andreasian/Selfie-AI.git
   ```
   
2. Install the required dependencies. The app requires the following packages:

- cv2
- streamlit
  > You can install these packages using the following command:
  > ```bash
  > pip install cv2 streamlit
  > ```
  > 
  > Run the app using the following command:
  > ```bash
  > streamlit run main.py
  > ```

This will start the app, and you can access it in your web browser at http://localhost:8501.

---
## Deployment Notes

Notes: 
- If you want to deploy this app not on Heroku but on Streamlit:
  - Streamlit support suggests to include `opencv-python-headless ` to the `requirements.txt`
  - However, if you want to completely overcome the issues you can try to use `streamlit-webrtc`

---
## Contributing
I welcome contributions to the Selfie AI app! To contribute, please follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine:

   ```bash
   git clone https://github.com/Armen-Jean-Andreasian/Selfie-AI.git
   ```
   
3. Create a new branch for your contribution:

   ```bash
   git checkout -b new-feature
   ```
   
4. Make your desired changes to the codebase.

5. Commit your changes with descriptive commit messages:

   ```bash
   git commit -m "Add new feature"
   ```

6. Push your branch to your forked repository: 
   ```bash
   git push origin new-feature
   ```

7. Open a pull request on the original repository, explaining your changes and the purpose of the pull request.
