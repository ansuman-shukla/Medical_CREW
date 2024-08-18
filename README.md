Here's the README formatted properly for a `README.md` file, ensuring that Markdown syntax is correctly applied:

---

# 🩺 Medical Report Analysis ➕

Welcome to the **Medical Report Analysis** tool! This application helps you analyze medical reports by extracting information from a PDF, searching for relevant health articles, and providing health recommendations—all in one place. Let's get started!

## 🚀 Features

- **Analyze Blood Reports:** Automatically extracts and summarizes information from a PDF blood report.
- **Health Research:** Find relevant health articles based on the analysis.
- **Personalized Recommendations:** Provides easy-to-understand health advice based on the results.

## 🛠️ Setup Instructions

Follow these steps to get the application up and running on your machine.

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/ansuman-shukla/Medical_CREW.git
```

### 2. Install Dependencies

Make sure you have Python installed. Then, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root directory and add your API keys:

```env
SERPER_API_KEY=your-serper-api-key
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL_NAME=your-model-name
OPENAI_API_BASE=your-openai-api-base-url
```

### 4. Run the Application

Finally, run the Streamlit application:

```bash
streamlit run app.py
```

### 5. Upload a PDF

Once the application is running, you can upload a PDF file by clicking on the **"Choose a PDF file"** button.

### 6. Analyze and Get Results

Click on the **"Analyze Report"** button to start the analysis. The results will be displayed on the same page, including a summary of the blood test and health recommendations with clickable links to sources.

## 🧰 Development Setup

If you're a developer and want to make changes to the code, follow these additional steps:

### 1. Enable Logging

Logging is already set up in the application. You can see detailed logs in the terminal where you run the app.

### 2. Customize Agents and Tasks

You can find the agent and task initialization functions in the `main.py` file. Feel free to modify them to fit your needs.

### 3. Update Dependencies

If you add new dependencies, update the `requirements.txt` file by running:

```bash
pip freeze > requirements.txt
```

### 4. Testing

Make sure to test your changes by running the application with different PDF files.

---

This version should render correctly in a `README.md` file, with proper spacing, line breaks, and formatting.
