pipeline {
    agent any

    stages {
        stage('CFN Validate') {
            steps {
                echo 'Validating Cloudformation Template..'
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