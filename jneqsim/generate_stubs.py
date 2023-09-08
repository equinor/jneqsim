import stubgenj

import jneqsim
from jneqsim import neqsim

stubgenj.generateJavaStubs([neqsim], useStubsSuffix=False, outputDir="../jneqsim-stubs/jneqsim-stubs")
