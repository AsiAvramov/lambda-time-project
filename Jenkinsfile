pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        FUNCTION_NAME = 'TimeFunction'
        RUNTIME = 'python3.11'
        ROLE_ARN = 'arn:aws:iam::<your-account-id>:role/<your-lambda-role>'
        HANDLER = 'lambda_function.lambda_handler'
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

        stage('Create or Update Lambda') {
            steps {
                echo 'שלב 3: יצירת או עדכון הפונקציה'

                // נבדוק אם הפונקציה קיימת, אם לא - ניצור אותה
                sh '''
                if aws lambda get-function --function-name $FUNCTION_NAME --region $AWS_REGION > /dev/null 2>&1; then
                    echo "פונקציה קיימת - מבצע עדכון קוד"
                    aws lambda update-function-code \
                        --function-name $FUNCTION_NAME \
                        --zip-file fileb://function.zip \
                        --region $AWS_REGION
                else
                    echo "פונקציה לא קיימת - מבצע יצירה"
                    aws lambda create-function \
                        --function-name $FUNCTION_NAME \
                        --runtime $RUNTIME \
                        --role $ROLE_ARN \
                        --handler $HANDLER \
                        --zip-file fileb://function.zip \
                        --region $AWS_REGION
                fi
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 הפונקציה נוצרה או עודכנה בהצלחה!'
        }
        failure {
            echo '❌ שגיאה במהלך יצירה/עדכון הפונקציה'
        }
    }
}
