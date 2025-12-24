pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/ajithselvam/complete-Python-project-with-Jenkins-deployment-pipeline'
            }
        }

        stage('Run Python App') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
