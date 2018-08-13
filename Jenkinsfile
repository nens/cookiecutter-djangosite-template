node {
   stage "Build"
   checkout scm
   sh "rm -rf .venv"
   sh "pipenv lock"
   sh "PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev"

   stage "Test"
   sh "pipenv run nosetests"
   step $class: 'JUnitResultArchiver', testResults: 'nosetests.xml'
}
