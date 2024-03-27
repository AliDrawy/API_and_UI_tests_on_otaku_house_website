pipeline {
    agent any

    environment {
        JIRA_API = credentials('JIRA_TOKEN')
        TOKEN = credentials('WEBSITE_TOKEN')
        MAIL = credentials('MAIL_TOKEN')
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat 'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m venv venv'
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Setup Environment success.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Setup Environment failed.")
                }
            }
        }

        stage('Setup Selenium Server HUB') {
            steps {
                echo 'Setting up Selenium server HUB...'
                bat "start /b java -jar selenium-server-4.17.0.jar hub"
                bat 'ping 127.0.0.1 -n 11 > nul'
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Setup Selenium Server HUB success.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Setup Selenium Server HUB failed.")
                }
            }
        }

        stage('Setup Selenium Server nodes') {
            steps {
                echo 'Setting up Selenium server nodes...'
                bat "start /b java -jar selenium-server-4.17.0.jar node --port 5555 --selenium-manager true"
                bat 'ping 127.0.0.1 -n 11 > nul'
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Setup Selenium Server nodes success.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Setup Selenium Server nodes failed.")
                }
            }
        }

        stage('Running Tests') {
            steps {
                echo 'Testing..'
                bat "venv\\Scripts\\python.exe test_runner_ui_and_api.py"
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Running Tests success.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Running Tests failed.")
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Deploy success.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Deploy failed.")
                }
            }
        }

        stage('Check Reports Directory') {
            steps {
                bat 'dir reports'
            }
        }

        stage('Publish Report') {
            steps {
                bat 'powershell Compress-Archive -Path reports/report.html -DestinationPath report.zip -Force'
                archiveArtifacts artifacts: 'report.zi', onlyIfSuccessful: true
//                     bat 'Compress-Archive -Path "source_file_or_directory" -DestinationPath "destination.zip"'
//                     bat 'cd reports && zip -r ../report.zip report.html'
//                     archiveArtifacts artifacts: 'report.zip', onlyIfSuccessful: true
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            slackSend (color: 'warning', message: "NOTIFICATION: Cleaning up resources...")
        }
        success {
            echo 'Build succeeded.'
            slackSend (color: 'good', message: "SUCCESS: Build success.")
        }
        failure {
            echo 'Build failed.'
            slackSend (color: 'danger', message: "FAILURE: Build failed.")
        }
    }
}
