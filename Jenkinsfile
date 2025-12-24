pipeline {
    agent any
    
    environment {
        APP_NAME = "python-flask-app"
        DOCKER_IMAGE = "${APP_NAME}:${BUILD_NUMBER}"
        DOCKER_IMAGE_LATEST = "${APP_NAME}:latest"
        CONTAINER_NAME = "${APP_NAME}-container"
        APP_PORT = "5000"
        HOST_PORT = "5000"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    sh """
                        docker build -t ${DOCKER_IMAGE} .
                        docker tag ${DOCKER_IMAGE} ${DOCKER_IMAGE_LATEST}
                    """
                }
            }
        }
        
        stage('Test Image') {
            steps {
                echo 'Testing Docker image...'
                script {
                    sh """
                        docker run --rm ${DOCKER_IMAGE} python -c 'import flask; print("Flask imported successfully")'
                    """
                }
            }
        }
        
        stage('Stop Old Container') {
            steps {
                echo 'Stopping and removing old container...'
                script {
                    sh """
                        docker stop ${CONTAINER_NAME} || true
                        docker rm ${CONTAINER_NAME} || true
                    """
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying new container...'
                script {
                    sh """
                        docker run -d \
                            --name ${CONTAINER_NAME} \
                            -p ${HOST_PORT}:${APP_PORT} \
                            -e ENVIRONMENT=production \
                            --restart unless-stopped \
                            ${DOCKER_IMAGE}
                    """
                }
            }
        }
        
        stage('Verify Deployment') {
            steps {
                echo 'Verifying deployment...'
                script {
                    sleep(time: 5, unit: 'SECONDS')
                    sh """
                        curl -f http://localhost:${HOST_PORT}/health || exit 1
                    """
                }
            }
        }
        
        stage('Cleanup Old Images') {
            steps {
                echo 'Cleaning up old Docker images...'
                script {
                    sh """
                        docker images ${APP_NAME} --format '{{.Tag}}' | \
                        grep -v 'latest' | grep -v '${BUILD_NUMBER}' | \
                        head -n -3 | \
                        xargs -I {} docker rmi ${APP_NAME}:{} || true
                    """
                }
            }
        }
    }
    
    post {
        success {
            echo '✅ Deployment successful!'
            echo "Application is running at: http://localhost:${HOST_PORT}"
        }
        failure {
            echo '❌ Deployment failed!'
            sh "docker logs ${CONTAINER_NAME} || true"
        }
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
