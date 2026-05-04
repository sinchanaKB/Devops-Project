pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                bat '"C:\Program Files\Python313\Scripts\pip.exe" install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest --junitxml=results.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'results.xml'
        }
    }
}
