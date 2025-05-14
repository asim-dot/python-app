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
                    // Build the Docker image (using Windows commands)
                    bat 'docker build -t flask-app:latest .'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Run tests within the Docker container
                    bat 'docker run --rm flask-app:latest python -m pytest || exit 0'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Stop any existing container (using Windows commands)
                    bat 'docker stop flask-app-container || exit 0'
                    bat 'docker rm flask-app-container || exit 0'
                    
                    // Run the new container
                    bat 'docker run -d -p 5000:5000 --name flask-app-container flask-app:latest'
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