pipeline {
    agent any

    parameters {
        string(name: 'USER_MESSAGE', defaultValue: 'Hola desde Jenkins', description: 'Mensaje enviado al script.')
        file(name: 'INPUT_FILE', description: 'Archivo que será leído por el script Python')
    }

    environment {
        CUSTOM_VAR = "Variable definida por el usuario"
    }

    
    triggers {
        pollSCM('0 7 * * *')
    }


    stages {

        stage('Init Info') {
            steps {
                echo "---- Información del Pipeline ----"
                echo "Usuario: ${env.BUILD_USER}"
                echo "Build ID: ${env.BUILD_ID}"
                echo "Rama: ${env.GIT_BRANCH}"
                echo "Var custom: ${CUSTOM_VAR}"
                echo "Mensaje parámetro: ${params.USER_MESSAGE}"
            }
        }

        stage('Virtualenv') {
            steps {
                sh """
                python3 -m venv venv
                . venv/bin/activate
                """
            }
        }

        stage('Install requirements') {
            steps {
                sh """
                . venv/bin/activate
                pip install -r requirements.txt
                """
            }
        }

        stage('Execute script') {
            steps {
                sh """
                . venv/bin/activate
                python script.py --msg "${params.USER_MESSAGE}" --file "${params.INPUT_FILE}"
                """
            }
        }
    }

    post {
        success {
            echo "🎉 La ejecución ha sido exitosa"
        }
        failure {
            echo "❌ La ejecución ha fallado"
        }
    }
}
