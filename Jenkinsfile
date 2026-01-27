pipeline {
    agent any

    environment {
        IMAGE_NAME = "100-movies-qa"
        IMAGE_TAG  = "${BUILD_NUMBER}"
        ENV        = "prod"
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

        stage('Manual Approval') {
            steps {
                input "Deploy to PRODUCTION?"
            }
        }

        stage('Deploy to QA') {
            steps {
                echo "🚀 Deploying ${IMAGE_NAME}:${IMAGE_TAG} to QA environment"
                // kubectl apply -f qa-deployment.yaml
            }
        }
    }

    post {
        success {
            echo "✅ QA pipeline successful"
        }
        failure {
            echo "❌ QA pipeline failed"
        }
    }
}