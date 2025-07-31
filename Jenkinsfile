pipeline {
    agent any

    // No 'tools' block is needed. We will use an environment variable instead.

    stages {
        stage('Install Dependencies') {
            steps {
                // We use an environment variable (%PYTHON_HOME% on Windows) to find pip.
                // The variable must be configured in your Jenkins agent settings.
                bat '"%PYTHON_HOME%\Scripts\pip" install -r app/requirements.txt'
                bat '"%PYTHON_HOME%\Scripts\pip" install -r tests/requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Use the full path to python to run pytest
                bat '"%PYTHON_HOME%\Scripts\pytest" tests/test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                // Use the full path to the python executable
                bat '"%PYTHON_HOME%\python" -u app/app.py'
            }
        }
    }
}