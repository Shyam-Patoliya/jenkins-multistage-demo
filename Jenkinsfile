pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building Inventory API..."
                sh 'echo Installing dependencies...'
            }
        }

        stage('Test') {
            steps {
                echo "Running Tests..."
                sh 'echo No tests found'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying Application..."
                sh 'echo Deploying Inventory API on test server'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
