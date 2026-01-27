pipeline {
    agent {
        docker {
            image 'python:3.12-slim'

        }
    }

    environment {
        IMAGE_NAME = "100-movies-dev"
        IMAGE_TAG  = "${BUILD_NUMBER}"
        ENV        = "dev"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Runtime') {
            steps {
                sh '''
                    python --version
                    pip --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
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
                // kubectl apply -f dev-deployment.yaml
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