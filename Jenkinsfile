pipeline {
    agent any

    environment {
        IMAGE_NAME = "100-movies-dev"
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install beautifulsoup4 requests pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                  docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Deploy to DEV') {
            steps {
                echo "🚀 Deploying ${IMAGE_NAME}:${IMAGE_TAG} to DEV"
                // kubectl apply -f dev-deployment.yaml (later)
            }
        }
    }

    post {
        success {
            echo "✅ DEV pipeline successful"
        }
        failure {
            echo "❌ DEV pipeline failed"
        }
    }
}