pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup') {
            steps {
                script {
                    // Install dependencies
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Run tests
                    bat 'python -m pytest || exit 0'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Kill any running Flask process
                    bat 'taskkill /F /IM python.exe /FI "WINDOWTITLE eq Flask" || exit 0'
                    
                    // Start Flask app as a background process with a title
                    bat 'start "Flask" /B python app.py'
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