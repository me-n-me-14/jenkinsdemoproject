pipeline {
    agent any

    tools {
        python 'python3'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r app/requirements.txt'
                bat 'python -m pip install -r tests/requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                bat 'python -m flake8 .'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m pytest tests/test_app.py'
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
