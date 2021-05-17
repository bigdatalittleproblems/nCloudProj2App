pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh "ls"
                // sh "cd dockerapp/Flask"
                sh "cat dockerapp/Flask/Dockerfile"
                echo 'Hello World'
            }
        }
      
    }
}
