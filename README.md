## SafeRoads-AI Enabled Accident Detection

## Project Overview:
Accident detection from CCTV footage plays a pivotal role in enhancing public safety and emergency response capabilities. CCTV cameras are ubiquitous in urban environments, roadways, and critical infrastructure, serving as vigilant electronic eyes that monitor real-time activities. The ability to automatically identify and respond to accidents in this footage is crucial for several reasons.
Firstly, timely accident detection facilitates rapid response from emergency services, minimizing the impact on victims and potentially saving lives. Emergency personnel can be dispatched swiftly to the scene, equipped with accurate information about the incident's nature and severity. Additionally, it aids in efficient traffic management, allowing authorities to divert or regulate traffic to prevent secondary accidents and congestion.
Our project revolves around the development of an advanced AI-based Accident Detection System utilizing state-of-the-art technology to enhance public safety and emergency response mechanisms. Leveraging the YOLOv8 classifier model, we have meticulously designed a robust system that analyzes CCTV footage for real-time identification of accidents.

## Key Features:
1. **YOLOv8 Classifier Model:**
   We conducted comprehensive evaluations of various YOLO models and found that the YOLOv8 classifier yielded the most satisfactory results. This deep learning model enables precise detection of accidents within video frames, providing accurate bounding boxes and labels.
2. **Gemini-vision Integration:**
   In the event of an accident, our system seamlessly integrates with the Gemini-vision model to extract detailed descriptions of the incident from the images. This enhances the depth of information available for emergency responders and authorities.
3. **Twilio Messaging API:**
   To ensure swift response, the system utilizes the Twilio messaging API to send alert messages with the timestamp of the accident occurrence to registered mobile numbers. This feature facilitates timely intervention and enhances emergency services.
4. **Gradio User Interface:**
   We have implemented a user-friendly interface using Gradio, allowing users to input videos for prediction and view the detected accidents along with detailed descriptions. This simplifies the interaction with our system and makes it accessible to a broader audience.

## Tech Stack:
- Ultralytics for YOLOv8 model implementation.
- Twilio Messaging API for real-time alerts.
- OpenCV for efficient image processing.
- Gradio for building an intuitive user interface.

## Model Evaluation:
After thorough experimentation with various models on our dataset, we present the performance results in the following table. Our evaluation showcases the superior capabilities of the YOLOv8 classifier, demonstrating its efficacy with impressive precision, recall, metrics/mAP_0.5, and metrics/mAP_0.5:0.95 metrics.
### Result Table of Detection models:
|     Model Name    |     Weights    |     Epochs    |     Precision    |     Recall     |     metrics/mAP_0.5    |     metrics/mAP_0.5:0.95    |
|-------------------|----------------|---------------|------------------|----------------|------------------------|-----------------------------|
|     YOLOv5        |     yolov5n    |     30        |     0.8885       |     0.884      |     0.9340             |     0.640                   |
|                   |     yolov5n    |     50        |     0.9256       |     0.915      |     0.9559             |     0.9628                  |
|                   |     yolov5l    |     30        |     0.9543       |     0.9340     |     0.97               |     0.7724                  |
|     YOLOv7        |     yolov7     |     20        |     0.036        |     0.0136     |     0.2645             |     0.1694                  |
|     YOLOv8        |     yolov8n    |     40        |     0.95278      |     0.92164    |     0.953              |     0.74679                 |
|                   |     yolov8s    |     40        |     0.95246      |     0.93964    |     0.953              |     0.74829                 |
|                   |     Yolov8m    |     40        |     0.8463       |     0.7756     |     0.875              |     0.6961                  |

### Result Table of Classification models:
|     Model Name     |     Epochs    |     Top1_ac    |     Top5_acc    |     Recall    |     metrics/mAP_0.5    |     metrics/mAP_0.5:0.95    |
|--------------------|---------------|----------------|-----------------|---------------|------------------------|-----------------------------|
|     yolov8n-cls    |     30        |     0.953      |     0.983       |     0.884     |     0.9340             |     0.640                   |
|     yolov8m-cls    |     30        |     0.954      |     0.994       |     0.915     |     0.9559             |     0.9628                  |
|     yolov8l-cls    |     30        |     0.968      |     1.00        |     0.9340    |     0.97               |     0.7724                  |

In summary, the model's exemplary performance in real-time evaluation on CCTV footage, with an impressive accuracy of 98-99%, reinforces its efficacy as a powerful tool for accident detection. This achievement reflects a significant milestone in our pursuit of leveraging advanced AI technologies for the enhancement of road safety, highlighting the potential impact of our model in real-world accident prevention and management scenarios.
  
## Implementation :
- Notebook: https://drive.google.com/drive/folders/1awd9kdlGUin9qzkSepF_iInEwxJmJrno?usp=sharing
- Download Model: https://drive.google.com/drive/folders/1IgwjwLaDJ52XmplS4TrLbga03SHN_MPi?usp=sharing
- Documentation: https://drive.google.com/file/d/1QC_zcRO4e4dRmghkrcP6WGJN98zomum0/view?usp=sharing

## Team Members:
1. Team Leader: Anindya Mitra
   - University/College: The Neotia University
   - Email: anindyamitra2018@gmail.com

2. Team Member 2: Ripan Purkait
   - University/College: The Neotia University
   - Email: ripanpurkait695@gmail.com

3. Team Member 3: Sudip Dhara
   - University/College: The Neotia University
   - Email: sudip.dhara.code@gmail.com
   

For any inquiries, please contact the team leader at anindyamitra2018@gmail.com. Thank you for your consideration and interest in our project!
