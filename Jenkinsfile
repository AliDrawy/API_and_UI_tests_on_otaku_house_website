pipeline {
    agent any
    environment {
        PIP_PATH = 'C:\\Program Files\\Python310\\Scripts\\pip.exe'
        PYTHON_PATH = 'C:\\Program Files\\Python310\\python.exe'
    }
    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setup Environment..'
                bat "${PYTHON_PATH} pip install -r requirements.txt"

            }
        }
        stage('Setup Selenium Server HUB') {
            steps {
               echo 'Setup Selenium HUB..'
               bat "start /b java -jar selenium-server-4.17.0.jar hub"
                        // Delay for 10 seconds
               bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds

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


