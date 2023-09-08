import stubgenj

from jneqsim import neqsim

stubgenj.generateJavaStubs(
    [neqsim], useStubsSuffix=False, outputDir="../old-stubs/old-stubs"
)
