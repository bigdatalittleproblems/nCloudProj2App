pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh "ls"
                sh "cd dockerapp/Flask"
                sh "cat Dockerfile"
                echo 'Hello World'
            }
        }
      
    }
}
