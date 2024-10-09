# Module 2: Introduction to VSCode, Python, and Testing

## Module Overview
This module introduces students to integrated development environments (IDEs), specifically Visual Studio Code (VSCode), and how to set up a Python development environment. Students will learn to use Python with pytest for testing, create virtual environments, and understand basic Python programming concepts like functions and variables. By the end of this module, students will be able to set up a project using GIT and GitHub that includes a simple calculator application, with automated testing using GitHub Actions.

### Why VSCode, Python, and Testing?
VSCode is a powerful, open-source IDE that supports many programming languages and has numerous extensions to enhance development productivity. Python is a versatile programming language widely used in various fields, including web development, data science, and automation. Testing is crucial to ensure code reliability and maintainability, and pytest is a popular testing framework for Python. GitHub Actions allow automated workflows to build, test, and deploy code, integrating continuous integration/continuous deployment (CI/CD) practices.

### Learning Outcomes
- Utilize GIT for version control and collaborative development.
- Create Python applications with automated testing.

## Module 2 Learning Pathway

### Recall

**Title:** Prior Experience with Python and VSCode  
**Grading Type:** Points  
**Instructions:** 
- Participate in a discussion forum to share your previous experiences with Python and VSCode.
- Discuss any challenges you faced and how you resolved them.
- This activity will help gauge your familiarity with these tools and set the stage for the new material.

### Read

1. **Article: "Getting Started with Visual Studio Code"**
   - URL: [Getting Started with VSCode](https://code.visualstudio.com/docs/introvideos/basics)
   - Purpose: To guide you through the installation and basic usage of VSCode.

2. **Article: "Python and VSCode"**
   - URL: [Python in VSCode](https://code.visualstudio.com/docs/python/python-tutorial)
   - Purpose: To help you set up Python development in VSCode.

3. **Article: "Virtual Environments in Python"**
   - URL: [Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
   - Purpose: To introduce you to creating and using virtual environments in Python.

4. **Article: "Introduction to pytest"**
   - URL: [Introduction to pytest](https://docs.pytest.org/en/stable/getting-started.html)
   - Purpose: To familiarize you with the basics of testing Python code using pytest.

5. **Article: "GitHub Actions: Basics"**
   - URL: [GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
   - Purpose: To understand the basics of GitHub Actions for CI/CD.
_____NEW_______

6. **Article: "Building Command-Line Applications in Python"**
   - URL: [Command-Line Applications in Python](https://realpython.com/command-line-interfaces-python-argparse/)
   - Purpose: To learn techniques for creating interactive command-line applications.

7. **Article: "DRY (Don't Repeat Yourself) Principle in Python"**
   - URL: [DRY Principle](https://www.makeuseof.com/python-dry-principle/)
   - Purpose: To understand and apply the DRY principle for writing maintainable and efficient Python code.

8. **Article: "Comprehensive Guide to Testing in Python"**
   - URL: [Testing in Python](https://realpython.com/python-testing/)
   - Purpose: To learn comprehensive testing strategies using pytest.


### Watch

1. **Video: "Introduction to VSCode" (15 minutes)**
   - Purpose: To provide an overview of VSCode, its features, and how to set it up for Python development.

2. **Video: "Python and Testing with pytest" (15 minutes)**
   - Purpose: To demonstrate setting up Python, creating virtual environments, and writing tests using pytest.

3. **Video: "Setting Up GitHub Actions" (15 minutes)**
   - Purpose: To provide a visual guide to setting up GitHub Actions for automated testing.

### Review

1. **Resource: VSCode Cheat Sheet**
   - [VSCode Cheat Sheet](https://vscodecandothat.com/)
   - Purpose: To provide you with a quick reference for using VSCode.

2. **Resource: Python Basics Cheat Sheet**
   - [Python Basics](https://www.pythonsheets.com/)
   - Purpose: To provide a quick reference for basic Python syntax and functions.

3. **Resource: pytest Cheat Sheet**
   - [pytest Cheat Sheet](https://www.cheatography.com/oleksii/cheat-sheets/pytest/)
   - Purpose: To offer a quick reference for writing and running tests using pytest.

### Submit

**Activity Type:** Hands-on Assignment  

**Activity Title:** Calculator Project with Automated Tests  

**Grading Type:** Points  

**Submission Instructions:** Submit a link to your repository on Canvas.

**Instructions:** 
- Create a new Git repository locally and a repository on GitHub. You will upload/push your local repo to GitHub.
- Set up a Python project in VSCode.
- Create a virtual environment for your project.
- Write a simple command line calculator application that includes functions for addition, subtraction, multiplication, and division.
- Write tests for each calculator function using pytest.
- Configure GitHub Actions to run your tests automatically on each push to the repository.
- Push your code and configuration to GitHub and ensure that GitHub Actions runs your tests successfully.

**Grading Expectations:** Completeness and accuracy of the calculator application and tests, proper use of GIT commands, successful setup of GitHub Actions for automated testing, and correct implementation of Python virtual environments.

**Alignment:** 
- Utilize GIT for version control and collaborative development.
- Create Python applications with automated testing.

### Reflect

**Title:** Module 2 Reflection  
**Grading Type:** Points  
**Instructions:** 
- Write a brief reflection (150-200 words) on your experience setting up the Python development environment and writing tests.
- Discuss how confident you feel using the tools and any areas where you need further clarification or support.
- This activity aims to encourage metacognition and connect new knowledge with prior experiences.

### Quiz

**Title:** VSCode, Python, and Testing Basics Quiz  
**Grading Type:** Points  
**Instructions:** 
- Complete a quiz covering the key concepts and commands introduced in this module.
- The quiz will test your understanding of setting up VSCode, using Python and virtual environments, writing tests with pytest, and configuring GitHub Actions.
- Review the provided cheat sheets and tutorials before taking the quiz.

### Additional Information

#### Installing Python on Mac
Mac users will need to install Python and manage packages. Follow these steps:

1. **Install Python:**
   - Open the Terminal application.
   - Paste the following command and press Enter:
     ```sh
     brew install python
     ```
   - Follow the on-screen instructions to complete the installation.

2. **Verify the Installation:**
   - Type the following command and press Enter:
     ```sh
     python3 --version
     ```
   - You should see the installed version of Python.

3. **Install VSCode:**
   - Download and install VSCode from the official website: [Visual Studio Code](https://code.visualstudio.com/).
   - Follow the on-screen instructions to complete the installation.
