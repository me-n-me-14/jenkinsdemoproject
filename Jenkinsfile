pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\Users\\misha\\AppData\\Local\\Programs\\Python\\Python313'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/me-n-me-14/jenkinsdemoproject.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'echo PYTHON_HOME is: %PYTHON_HOME%'
                bat '"%PYTHON_HOME%\\python.exe" -m pip install -r app/requirements.txt'
                bat '"%PYTHON_HOME%\\python.exe" -m pip install -r tests/requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat '"%PYTHON_HOME%\\python.exe" -m pytest tests/test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                bat '"%PYTHON_HOME%\\python.exe" -u app/app.py'
            }
        }
    }
}
