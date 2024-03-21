pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setup Environment..'
                bat 'pip install -r requirements.txt'

            }
        }
        stage('Setup Selenium Server HUB') {
            steps {
                echo 'Setup Selenium HUB..'
                bat "start /b java -jar selenium-server-4.17.0.jar hub"
                bat 'ping 127.0.0.1 -n 11 > nul'
            }
        }
        stage('Setup Selenium Server nodes') {
            steps {
                echo 'Setup Selenium nodes..'
                bat "start /b java -jar selenium-server-4.17.0.jar node --port 5555 --selenium-manager true"
                bat 'ping 127.0.0.1 -n 11 > nul'
            }
        }
        stage('Test POC ') {
            steps {
                echo 'Testing..'
                bat 'python -m unittest test/test_ui_and_api.py'


            }
        }
//         stage('Test UI ') {
//             steps {
//                 echo 'Testing..'
//                 bat 'python -m unittest API_tests_on_GamePower_and_UI_tests_on_YouTube/tests/ui_test/run_all_tests.py'
//
//             }
//         }
    }
}


