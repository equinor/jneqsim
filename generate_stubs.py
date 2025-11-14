import stubgenj

from jneqsim_test.jvm_service import neqsim

stubgenj.generateJavaStubs([neqsim], useStubsSuffix=False, outputDir="./jneqsim")
