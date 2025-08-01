pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\Users\misha\AppData\Local\Programs\Python\Python313'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON_HOME%\python.exe" -m pip install -r app/requirements.txt'
                bat '"%PYTHON_HOME%\python.exe" -m pip install -r tests/requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                bat '"%PYTHON_HOME%\python.exe" -m flake8 .'
            }
        }
        stage('Test') {
            steps {
                bat '"%PYTHON_HOME%\python.exe" -m pytest tests/test_app.py'
            }
        }
        stage('Build') {
            steps {
                bat 'docker build -t my-app .'
            }
        }
        stage('Deploy') {
            steps {
                bat 'docker run -d -p 8080:80 my-app'
            }
        }
    }
}
