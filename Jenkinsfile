pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'echo PYTHON_HOME is: %PYTHON_HOME%'
                bat '"%PYTHON_HOME%/Scripts/pip" install -r app/requirements.txt'
                bat '"%PYTHON_HOME%/Scripts/pip" install -r tests/requirements.txt'
                bat '"C:/Users/misha/AppData/Local/Programs/Python/Python313/python.exe" install -r app/requirements.txt
            }
        }
        stage('Test') {
            steps {
                bat '"%PYTHON_HOME%/Scripts/pytest" tests/test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                bat '"%PYTHON_HOME%/python" -u app/app.py'
            }
        }
    }
}
