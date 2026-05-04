pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                bat '"C:/Program Files/Python313/pip.exe" install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest --junitxml=results.xml'
            }
        }
        stage('Debug') {
            steps {
                bat 'where python'
                bat 'echo %PATH%'
            }
        }
    }
    

    post {
        always {
            junit allowEmptyResults: true, testResults: 'results.xml'
        }
    }
}
