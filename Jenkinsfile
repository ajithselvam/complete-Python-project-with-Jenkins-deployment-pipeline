pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Run Python App') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
