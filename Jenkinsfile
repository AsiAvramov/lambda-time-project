pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        FUNCTION_NAME = 'TimeFunction'
    }

    stages {
        stage('Clone') {
            steps {
                echo 'שלב 1: שיבוט קוד'
                checkout scm
            }
        }

        stage('Zip Lambda') {
            steps {
                echo 'שלב 2: ייצור ZIP לקוד הלמבדה'
                sh 'zip function.zip lambda_function.py'
            }
        }

        stage('Deploy to AWS Lambda') {
            steps {
                echo 'שלב 3: העלאה ל-AWS Lambda'
                sh '''
                    aws lambda update-function-code \
                        --function-name $FUNCTION_NAME \
                        --zip-file fileb://function.zip \
                        --region $AWS_REGION
                '''
            }
        }
    }

    post {
        success {
            echo 'הפונקציה עלתה בהצלחה 🎉'
        }
        failure {
            echo 'נכשל דיפלוי 😢'
        }
    }
}
