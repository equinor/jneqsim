from pathlib import Path

def get_jar_path():
    """Get the path to the NeqSim Java 8 JAR file."""
    jar_path = Path(__file__).parent / "neqsim-Java8.jar"
    if not jar_path.exists():
        raise FileNotFoundError(f"JAR file not found: {jar_path}")
    return str(jar_path)

__version__ = "0.0.1"