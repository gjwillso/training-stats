pipeline {
    agent any

    stages {
        stage('CFN Validate')  {

            steps {

                echo 'Validating Cloudformation Template..'
       
                withCredentials([[
                    $class: ‘AmazonWebServicesCredentialsBinding’,
                    credentialsId: ‘ts_git_user’,
                    accessKeyVariable: ‘AWS_ACCESS_KEY_ID’,
                    secretKeyVariable: ‘AWS_SECRET_ACCESS_KEY’
            ]]) {
                sh ”’
                    export AWS_REGION=eu-west-1
                    aws cloudformation validate-template --template-body file://template.yaml
                ’”
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