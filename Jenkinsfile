pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                // Ensure this line is clean and inside single quotes
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Runs pytest and creates the report file
                sh 'pytest --junitxml=results.xml'
            }
            post {
                always {
                    // This creates the visual report in Jenkins
                    junit 'results.xml'
                }
            }
        }
        stage('Build & Package') {
            steps {
                // This builds your "Validated Docker image"
                sh 'docker build -t bus-system-app:latest .'
            }
        }
    }
}
