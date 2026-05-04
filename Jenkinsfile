pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'[cite: 4]
            }
        }
        stage('Test') {
            steps {
                // Runs tests and generates the 'test reports' required
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
                // This only runs if the 'Test' stage passes.
                // It creates the 'Validated Docker image'
                sh 'docker build -t bus-system-app:latest .'
            }
        }
    }
}