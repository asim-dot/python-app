pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t flask-app:latest .'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Run tests within the Docker container
                    sh 'docker run --rm flask-app:latest python -m pytest'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Stop any existing container
                    sh 'docker stop flask-app-container || true'
                    sh 'docker rm flask-app-container || true'
                    
                    // Run the new container
                    sh 'docker run -d -p 5000:5000 --name flask-app-container flask-app:latest'
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}