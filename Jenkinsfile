pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r app/requirements.txt'
                bat 'pip install -r tests/requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'pytest tests/test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                bat 'python app/app.py'
            }
        }
    }
}