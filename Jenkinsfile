node {
   stage "Build"
   checkout scm
   sh "python3 bootstrap.py"
   sh "bin/buildout"

   stage "Test"
   sh "bin/test"
   step $class: 'JUnitResultArchiver', testResults: 'nosetests.xml'
}
