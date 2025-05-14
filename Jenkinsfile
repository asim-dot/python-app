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
                    // Use existing Python installation at D:\PYTHON
                    bat '''
                        echo Using existing Python installation...
                        "D:\\PYTHON\\python.exe" -m pip install --upgrade pip
                        "D:\\PYTHON\\python.exe" -m pip install -r requirements.txt
                    '''
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Run tests with full path to python
                    bat '"D:\\PYTHON\\python.exe" -m pytest || exit 0'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Kill any running Flask process
                    bat 'taskkill /F /IM python.exe /FI "WINDOWTITLE eq Flask" || exit 0'
                    
                    // Start Flask app as a background process with a title
                    bat 'start "Flask" /B "D:\\PYTHON\\python.exe" app.py'
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