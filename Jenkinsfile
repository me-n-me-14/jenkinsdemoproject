pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                // Use forward slashes for paths in Jenkinsfile
                bat '"%PYTHON_HOME%/Scripts/pip" install -r app/requirements.txt'
                bat '"%PYTHON_HOME%/Scripts/pip" install -r tests/requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Use forward slashes for paths in Jenkinsfile
                bat '"%PYTHON_HOME%/Scripts/pytest" tests/test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                // Use forward slashes for paths in Jenkinsfile
                bat '"%PYTHON_HOME%/python" -u app/app.py'
            }
        }
    }
}
