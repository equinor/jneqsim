import jpype
import importlib.resources

def get_neqsim_jar_path(version: tuple[int, int, int]) -> str:
    if version[0] == 1 and version[1] == 8:
        import jneqsim_java8  # type: ignore
        with importlib.resources.path("jneqsim_java8", "neqsim-Java8.jar") as jar_path:
            return str(jar_path)
    elif 11 <= version[0] < 21:
        import jneqsim_java11  # type: ignore
        with importlib.resources.path("jneqsim_java11", "neqsim-Java11.jar") as jar_path:
            return str(jar_path)
    elif version[0] >= 21:
        import jneqsim_java21  # type: ignore
        with importlib.resources.path("jneqsim_java21", "neqsim-Java21.jar") as jar_path:
            return str(jar_path)
    else:
        raise RuntimeError("Unsupported JVM version...")

if not jpype.isJVMStarted():
    jpype.startJVM()
    jar_path = get_neqsim_jar_path(jpype.getJVMVersion())
    jpype.addClassPath(jar_path)
import jpype.imports  # noqa

# This is the java package, added to the python scope by "jpype.imports"
neqsim = jpype.JPackage("neqsim")
