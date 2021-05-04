@Library('github.com/releaseworks/jenkinslib') _

pipeline {
    agent any

    stages {
        stage('CFN Validate')  {
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'aws-key', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    AWS("--region=eu-west-1 cloudformation validate-template --template-body file://template.yaml")
                }
            }
        }
        stage('CFN Package') {
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'aws-key', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    AWS("--region=eu-west-1 cloudformation package --template-file ./template.yaml --s3-bucket training-stats --output-template-file packaged.template.yaml")
                } 
            }
        }
        stage('CFN Deploy') {
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'aws-key', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    AWS("--region=eu-west-1 cloudformation deploy --template-file ./packaged.template.yaml --stack-name training-stats --capabilities CAPABILITY_IAM")
                } 
            }
        }
    }
}