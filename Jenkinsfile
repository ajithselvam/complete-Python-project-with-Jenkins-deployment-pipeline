pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Python App') {
            steps {
                sh '''
                  echo "Hello Ajith 👋"
                  echo "Python App Deployed Using Jenkins 🚀"
                '''
            }
        }
    }
}
