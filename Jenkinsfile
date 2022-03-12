pipeline {
    agent any
    stages {
        stage('Checkout Codebase'){
            steps{
                checkout scm: [$class: 'GitSCM', userRemoteConfigs: [[credentialsId: 'Gitlab', url: 'git@192.168.77.129:topaz/aws_saturday.git']]]
            }
        }

        stage('Test'){
            steps(
                sh 'echo Test'
            )
        }

        stage('Deploy'){
            steps(
                sh 'echo Deploy'
            )
        }
    }

}
