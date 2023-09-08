import stubgenj

import jneqsim
from jneqsim import neqsim

stubgenj.generateJavaStubs(
    [neqsim], useStubsSuffix=False, outputDir="../old-stubs/old-stubs"
)
