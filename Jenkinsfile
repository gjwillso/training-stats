@Library('github.com/releaseworks/jenkinslib') _

pipeline {
    agent any

    stages {
        stage('CFN Validate')  {

            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'ts_git_user', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    AWS("--region=eu-west-1 s3 ls")
                }
            }
        }
        stage('CFN Package') {
            steps {
                echo 'Performing Cloudformation Package..'
            }
        }
        stage('CFN Deploy') {
            steps {
                echo 'Performing Cloudformation Create/Update Stack....'
            }
        }
    }
}