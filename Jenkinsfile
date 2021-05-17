pipeline {
    agent any

    stages {
        stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */
        checkout scm
    }
        stage('Hello') {
            steps {
                sh "ls"
                echo 'Hello World'
            }
        }
        stage('Build Docker'){
            steps 
        }
    }
}
