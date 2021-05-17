pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh "ls"
                sh "cd dockerapp"
                sh "cat Dockerfile"
                echo 'Hello World'
            }
        }
      
    }
}
