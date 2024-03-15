import stubgenj

from jneqsim.jvm_service import neqsim

stubgenj.generateJavaStubs([neqsim], useStubsSuffix=False, outputDir=".")
