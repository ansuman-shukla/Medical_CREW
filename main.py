import os
import logging
from dotenv import load_dotenv
import streamlit as st
from crewai import Agent, Task, Crew, Process
from crewai_tools import (SerperDevTool)
from pypdf import PdfReader

# Load environment variables from .env file
load_dotenv()

# Constants for API keys and settings
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_environment_variables():
    """
    Loads and returns the environment variables required for the application.

    Returns:
        dict: A dictionary with environment variable names as keys and their values.
    """
    return {
        "SERPER_API_KEY": SERPER_API_KEY,
        "OPENAI_API_KEY": OPENAI_API_KEY,
        "OPENAI_MODEL_NAME": OPENAI_MODEL_NAME,
        "OPENAI_API_BASE": OPENAI_API_BASE,
    }


def initialize_agents():
    """
    Initializes and returns the agents used in the application.

    Returns:
        tuple: A tuple containing the initialized agents.
    """
    medical_analyst = Agent(
        role='Medical Analyst',
        goal='Analyze the blood test report and provide a summary in simple terms.',
        verbose=True,
        memory=True,
        backstory=(
            "An expert in interpreting medical data and explaining it to non-medical people."
        ),
        max_iter=7,
        # max_rpm=2,
        allow_delegation=False
    )

    health_researcher = Agent(
        role='Health Researcher',
        goal='Search the internet for articles based on the blood test analysis. You should then search the web for articles tailored to the persons health needs based on the blood test results',
        verbose=True,
        memory=True,
        backstory=(
            "Skilled at finding accurate and relevant health information online."
        ),
        max_iter=7,
        # max_rpm=2,
        allow_delegation=False,
        tools=[SerperDevTool(api_key=SERPER_API_KEY)]
    )

    health_advisor = Agent(
        role='Health Advisor',
        goal='Provide health recommendations based on the articles and blood test summary.',
        verbose=True,
        memory=True,
        backstory=(
            "Experienced in providing personalized health advice."
        ),
        max_iter=7,
        # max_rpm=2,
        allow_delegation=False
    )

    return medical_analyst, health_researcher, health_advisor


def initialize_tasks(medical_analyst, health_researcher, health_advisor):
    """
    Initializes and returns the tasks used in the application.

    Args:
        medical_analyst (Agent): The medical analyst agent.
        health_researcher (Agent): The health researcher agent.
        health_advisor (Agent): The health advisor agent.

    Returns:
        list: A list of initialized tasks.
    """
    analyze_blood_test = Task(
        description='Details of patient on the top then analyze the extracted text from the blood test report and provide a summary.',
        expected_output='Details of patient on the top,summary of the blood test in simple terms.',
        agent=medical_analyst,
    )

    search_for_articles = Task(
        description='Search the web for articles relevant to the health issues identified in the blood test summary.',
        expected_output='A list of articles with URLs and a brief description of each.',
        tools=[SerperDevTool(api_key=SERPER_API_KEY)],
        agent=health_researcher,
    )

    provide_recommendations = Task(
        description='''
            Provide health recommendations based on the articles and blood test summary.give health recommendations and provide links to the relevant articles   
        ''',
        expected_output='''
            A short and concise paragraph summary of the blood report in simple easy-to-understand terms 
            followed by a bullet list of actionable health recommendations, with each bullet point containing 
            links to its source // FOLLOW GIVEN FORMAT !!! //

            ## Summary
            [Provide a simple short summary of the blood report here , **If needed only do this step:-(Example:-Use data from blood report like (total platlets level[use from the orignal blood report ]))** ]

            ## Recommendations
            - [Recommendation 1 (ex:- eat healthy)](https://source1.com)
            - [Recommendation 2 (ex:- drink water)](https://source2.com)
            - [Recommendation 3 (ex:- eat healthy)](https://source3.com)
        ''',
        agent=health_advisor,
    )

    return [analyze_blood_test, search_for_articles, provide_recommendations]




def main():
    st.title("Medical Report Analysis ➕")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Extract text from PDF
        text = ""
        try:
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text += page.extract_text()
        except Exception as e:
            st.error(f"Error reading the PDF file: {e}")
            logger.error(f"Error reading the PDF file: {e}")
            return

        if st.button("Analyze Report"):
            st.write("Analyzing the report... This may take a few minutes.")
            logger.info("Report analysis started")

            # Initialize agents and tasks
            medical_analyst, health_researcher, health_advisor = initialize_agents()
            tasks = initialize_tasks(medical_analyst, health_researcher, health_advisor)

            # Form the crew and define the process
            crew = Crew(
                agents=[medical_analyst, health_researcher, health_advisor],
                tasks=tasks,
                process=Process.sequential
            )

            # Kick off the crew process with the extracted text
            with st.spinner("Processing..."):
                try:
                    result = crew.kickoff(inputs={"text": text})
                    logger.info("Report analysis completed successfully")
                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}")
                    logger.error(f"An error occurred during analysis: {e}")
                    return

            # Display results using Markdown for word wrapping and clickable links
            st.subheader("Analysis Results")
            st.markdown(result)
    else:
        st.write("Please upload a PDF file to begin analysis.")


if __name__ == "__main__":
    main()
