from pathlib import Path

import jpype


def get_neqsim_jar_path(version: tuple[int, int, int]) -> str:
    if version[0] == 1 and version[1] == 8:
        jar_path = Path(__file__).parent / "neqsim-Java8.jar"
    elif 11 <= version[0] <= 21:
        jar_path = Path(__file__).parent / "neqsim-Java11.jar"
    elif version[0] == 21:
        jar_path = Path(__file__).parent / "neqsim-Java21.jar"
    else:
        raise RuntimeError(
            "Unsupported JVM version. jneqsim requires java8, java11, or java21."
            + f"Got {version[0]}.{version[1]}.{version[2]}"
        )

    if not jar_path.is_file():
        raise FileNotFoundError("Missing required neqsim JAR! Bad build?")

    return str(jar_path)


if not jpype.isJVMStarted():
    jpype.startJVM()
    jar_path = get_neqsim_jar_path(jpype.getJVMVersion())
    jpype.addClassPath(jar_path)
import jpype.imports  # noqa

# This is the java package, added to the python scope by "jpype.imports"
neqsim = jpype.JPackage("neqsim")
