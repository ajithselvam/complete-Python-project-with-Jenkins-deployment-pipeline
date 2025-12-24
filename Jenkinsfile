pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ajithselvam/complete-Python-project-with-Jenkins-deployment-pipeline.git'
            }
        }

        stage('Run Python App') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
