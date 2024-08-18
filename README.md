Here's the updated README file that includes instructions for creating the environment variable file and a detailed explanation of how the application works.

---

# 🩺 Medical Report Analysis ➕

Welcome to the **Medical Report Analysis** tool! This application helps you analyze medical reports by extracting information from a PDF, searching for relevant health articles, and providing health recommendations—all in one place. Let's get started!

## 🚀 Features

- **Analyze Blood Reports:** Automatically extracts and summarizes information from a PDF blood report.
- **Health Research:** Finds relevant health articles based on the analysis.
- **Personalized Recommendations:** Provides easy-to-understand health advice based on the results.

## 🛠️ Setup Instructions

Follow these steps to get the application up and running on your machine.

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/ansuman-shukla/Medical_CREW.git
```

### 2. Create and Activate a Virtual Environment

It's recommended to create a virtual environment to manage your dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root directory and add your API keys:

```bash
touch .env
```

Open the `.env` file in a text editor and add the following:

```env
SERPER_API_KEY=your-serper-api-key
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL_NAME=your-model-name
OPENAI_API_BASE=your-openai-api-base-url
```

Replace the placeholder values with your actual API keys and settings.

### 5. Run the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

### 6. Upload a PDF

Once the application is running, you can upload a PDF file by clicking on the **"Browse file"** button.
![Screenshot 2024-08-18 095558](https://github.com/user-attachments/assets/8019f9e1-3822-4fba-98f7-ffb7254d5b4d)


### 7. Analyze and Get Results

Click on the **"Analyze Report"** button to start the analysis. The results will be displayed on the same page, including a summary of the blood test and health recommendations with clickable links to sources.

## 🔍 How Agents Works

This application uses a team of AI agents to analyze a medical report and provide health recommendations. Here’s how it works:

### 1. Medical Analyst Agent

- **Role:** The Medical Analyst is the first agent to work. This agent is responsible for analyzing the blood test report and extracting key information.
- **Task:** It reads the uploaded PDF file, extracts the text, and produces a summary of the blood test in simple terms.

### 2. Health Researcher Agent

- **Role:** After the Medical Analyst has completed its task, the Health Researcher takes over.
- **Task:** This agent searches the internet for relevant health articles based on the blood test analysis. It compiles a list of articles with URLs and brief descriptions.

### 3. Health Advisor Agent

- **Role:** Finally, the Health Advisor reviews the analysis and the articles provided by the Health Researcher.
- **Task:** This agent generates personalized health recommendations. It produces a short summary of the blood test report, followed by actionable health tips, each with a link to the relevant source.

### 4. Sequential Process

- **Execution:** The application uses a sequential process where each agent completes its task before passing the output to the next agent. This ensures that the final recommendations are based on thorough analysis and well-researched information.

### 5. Final Output

- **Result:** The output is a concise report displayed in Markdown format, including a summary of the blood test and a list of health recommendations with clickable links to relevant articles.

## 🧰 Development Setup

If you're a developer and want to make changes to the code, follow these additional steps:

### 1. Enable Logging

Logging is already set up in the application. You can see detailed logs in the terminal where you run the app.

### 2. Customize Agents and Tasks

You can find the agent and task initialization functions in the `app.py` file. Feel free to modify them to fit your needs.

### 3. Update Dependencies

If you add new dependencies, update the `requirements.txt` file by running:

```bash
pip freeze > requirements.txt
```

### 4. Testing

Make sure to test your changes by running the application with different PDF files.

---
