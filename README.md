Lung Cancer Detection

Readme.md

project description: 
Our project is focusing on Turning Machine Intelligence Against Lung Cancer. 
Our project is using a data set of high-resolution image scans of lungs from hundreds of patients provided by the National Cancer Institute. 

We will develop algorithms that could accurately determine when lesions in the lungs are cancerous. This will dramatically reduce the false positive rate that plagues the current detection technology, get patients earlier access to life-saving interventions, and give radiologists more time to spend with their patients.

In general, we need to predict whether a CT scan is of a patient who either has or will develop cancer within the next 12 months or not. We will train a network to segment out potentially cancerous nodules and then use the characteristics of that segmentation to make predictions about the diagnosis of the scanned patient within a 12 month time frame.

In order to identify regions with nodules, we will use a U-Net style convolutional network which was designed for segmenting neuronal structures.You can view our code whose title starts with LUNA, they show how we process the LUNA data and train a simple CONV network.(They are based on the LUNA database)

