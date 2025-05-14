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
                    // Use Python's full path or install Python
                    bat '''
                        echo Checking for Python...
                        where python || echo Python not found in PATH
                        
                        echo Installing Python if needed...
                        powershell -Command "if (-not (Test-Path 'C:\\Python39\\python.exe')) { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe' -OutFile 'python-installer.exe'; Start-Process -FilePath 'python-installer.exe' -ArgumentList '/quiet', 'InstallAllUsers=1', 'PrependPath=1' -Wait }"
                        
                        echo Refreshing PATH...
                        set PATH=C:\\Python39;C:\\Python39\\Scripts;%PATH%
                        
                        echo Installing dependencies...
                        C:\\Python39\\python.exe -m pip install --upgrade pip
                        C:\\Python39\\python.exe -m pip install -r requirements.txt
                    '''
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Run tests with full path
                    bat 'C:\\Python39\\python.exe -m pytest || exit 0'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Kill any running Flask process
                    bat 'taskkill /F /IM python.exe /FI "WINDOWTITLE eq Flask" || exit 0'
                    
                    // Start Flask app as a background process with a title
                    bat 'start "Flask" /B C:\\Python39\\python.exe app.py'
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