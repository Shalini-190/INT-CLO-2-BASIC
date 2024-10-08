# Hybrid Cloud Resource Allocation

---

## Project Title
**Hybrid Cloud Resource Allocation Simulation**

---

## Description
This project simulates a hybrid cloud resource allocation system, which optimizes the distribution of resources between on-premises infrastructure and the cloud. It dynamically handles resource requests, such as CPU, memory, and storage, allocating them either from the on-premises data center or the cloud, depending on availability.

---

## Features
- **Resource Allocation**: Dynamically allocate CPU, memory, and storage based on the available resources.
- **Hybrid Environment**: Manage resources between on-premises infrastructure and cloud services.
- **Cloud Fallback**: Automatically allocate resources from the cloud if the on-premises resources are insufficient.

---

## Technologies Used
- **Python**: For server-side logic.
- **HTTPServer**: To serve the application and handle requests.
- **HTML**, **CSS**: For the user interface.
- **AWS EC2**: Used to deploy the application.

---

## Usage
1. Enter the CPU, Memory, and Storage demands in the respective input fields.
2. Click on the **Allocate Resources** button to allocate the required resources.
3. If sufficient on-premises resources are available, they will be allocated. Otherwise, resources will be allocated from the cloud.

---

## How it Works
- The user inputs resource demands.
- The system checks on-premises resource availability.
- If resources are available on-premises, they are allocated.
- If on-premises resources are insufficient, the allocation is made from the cloud.

---

## Setup Instructions
1. Clone the repository.
2. Install required Python dependencies.
3. 4. Access the application via the public IP of your server on port 5000 (or as configured).


