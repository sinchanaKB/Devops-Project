pipeline {
    agent any

    stages {

        stage('Debug') {
            steps {
                bat 'where python'
                bat 'where pip'
                bat 'echo %PATH%'
            }
        }

        stage('Install') {
            steps {
                bat '"C:/Program Files/Python313/Scripts/pip.exe" install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '"C:/Program Files/Python313/python.exe" -m pytest --junitxml=results.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'results.xml'
        }
    }
}
