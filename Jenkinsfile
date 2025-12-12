pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'ahmedmostafa22'
        APP_NAME = 'ansible_project'
    }

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    def newVersion = "2.0.0"  
                    sh """
                        docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${newVersion} \
                        roles/app_deploy/files/app/
                    """
                }
            }
        }

        stage('Push to Registry') {
            steps {
                echo "Simulating push to registry. In a real pipeline, this would be enabled."
            }
        }

        stage('Run Ansible Rolling Update') {
    steps {
        sh '''
        # Fix TMP for Ansible
        export ANSIBLE_LOCAL_TEMP=/tmp/ansible_tmp
        export ANSIBLE_REMOTE_TEMP=/tmp/ansible_tmp
        mkdir -p /tmp/ansible_tmp

        # Fix SSH key permissions for Vagrant keys
        chmod 600 .vagrant/machines/web1/virtualbox/private_key || true
        chmod 600 .vagrant/machines/web2/virtualbox/private_key || true
        chmod 600 .vagrant/machines/lb1/virtualbox/private_key || true

        # Run playbook
        ansible-playbook playbooks/rolling_update.yml --extra-vars "new_version=2.0.0"
        '''
    }
}
    }
}





// pipeline {
//     agent any

//     environment {
//         // This would be your registry URL
//         DOCKER_REGISTRY = 'ahmedmostafa22'
//         // This would be your app name
//         APP_NAME = 'ansible_project'
//         // This is where ansible is installed
//         ANSIBLE_HOME = tool 'ansible'
//     }

//     stages {
//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     // Get the new version, e.g., from a tag or build number
//                     def newVersion = "2.0.0" // In a real pipeline, this would be dynamic
//                     sh "docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${newVersion} roles/app_deploy/files/app/"
//                 }
//             }
//         }

//         stage('Push to Registry') {
//             steps {
//                 script {
//                     // You would configure credentials for your registry
//                     // withDockerRegistry([url: "https://${DOCKER_REGISTRY}", credentialsId: 'docker-registry-credentials']) {
//                     //     sh "docker push ${DOCKER_REGISTRY}/${APP_NAME}:${newVersion}"
//                     }
//                     echo "Simulating push to registry. In a real pipeline, this would be enabled."
//                 }
//             }
//         }

//         stage('Run Ansible Rolling Update') {
//             steps {
//                 // This assumes your Jenkins agent has SSH access to the Ansible control node
//                 // and the necessary credentials to connect to the target VMs.
//                 sh '''
//                 ansible-playbook playbooks/rolling_update.yml --extra-vars "new_version=2.0.0"
//                 '''
//             }
//         }
//     }
// }
