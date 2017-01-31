node {
  stage 'Checkout'
    checkout scm

    // branch name from Jenkins environment variables
    print "My branch is: ${env.BRANCH_NAME}"

    print "Pull Request ID?!: ${env.CHANGE_ID}"
    print "Author: ${env.CHANGE_AUTHOR}"

    def workspace = pwd()
    env.PATH="${workspace}/venv/bin:${env.PATH}"

    sh 'virtualenv venv'
    sh 'pip install -r requirements.txt'
    sh 'python setup.py install'

  stage 'Lint'
    step([$class: 'CheckStylePublisher', canComputeNew: false, defaultEncoding: '', healthy: '', pattern: '', unHealthy: ''])

  stage 'Test'
    sh 'py.test tests'
    step([$class: 'JUnitResultArchiver', testResults: 'result.xml'])

  stage 'Cleanup'
    sh 'rm -rf venv'
    step([$class: 'GitHubCommitStatusSetter', errorHandlers: [[$class: 'ChangingBuildStatusErrorHandler', result: 'FAILURE']]])
}
