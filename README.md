# Project README

## Project Overview

This project is a Streamlit web application that displays a resume from a Markdown file. The application is containerized using Docker for easy deployment.

## Project Structure

The project has the following file structure:

- `Dockerfile`: Defines the Docker image for running the Streamlit app.
- `app`: Directory containing the Python application code and resources.
  - `main.py`: The main script that uses Streamlit to display the resume.
  - `utils.py`: Utility functions used by the main script.
  - `rundocker.sh`: Shell script for running the Docker container.
  - `requirements.txt`: File specifying Python dependencies.
  - `pages`: Directory containing additional pages for the Streamlit app.
    - `1_security.py`: Python script for a security-related page.
    - `2_download.py`: Python script for a page allowing the download of the resume in PDF format.
  - `resume_md`: Directory containing Markdown files for the resume.
    - `main.md`: Main content of the resume.
    - `security.md`: Additional content related to security.
  - `resume_pdf`: Directory containing PDF versions of the resume.
    - `main.pdf`: PDF version of the main resume.
    - `security.pdf`: PDF version of the security-related content.
  - `.github/workflows/docker-image.yml`: GitHub Actions workflow for building and deploying the Docker image.


## Running the Application Locally

To run the application locally, follow these steps:

1. Make sure you have Docker installed on your system.

2. Run the `rundocker.sh` script:

    ```bash
    sh rundocker.sh
    ```

3. Open your web browser and go to [http://localhost:8502](http://localhost:8502) to view the Streamlit app.

## Deployment

The project includes a GitHub Actions workflow (`docker-image.yml`) that triggers on pushes to the main branch. This workflow deploys the application to a remote server using SSH and Docker.

To set up deployment to your own server, update the following secrets in your GitHub repository settings:

- `SERVER_HOST`: The hostname or IP address of your server.
- `SERVER_USERNAME`: The username for SSH access to your server.
- `SERVER_SSH_PASSWORD`: The SSH password for accessing your server.

## Notes

- The application is configured to display the resume in a user-friendly format using Streamlit.
- The Dockerfile installs necessary dependencies and exposes the application on port 8502.
- GitHub Actions workflow automates the Docker image build and deployment process.
- Security-related content is separated into specific pages for focused viewing.
- The PDF download functionality allows users to download the resume in PDF format.

Feel free to customize the content and structure according to your preferences or add more features to enhance the resume viewer application.

Happy coding!
