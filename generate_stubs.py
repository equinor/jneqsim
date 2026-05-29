import os
import re

import stubgenj

from jneqsim.jvm_service import neqsim

stubgenj.generateJavaStubs([neqsim], useStubsSuffix=False, outputDir="./jneqsim")


def _fix_absolute_to_relative_imports(stubs_root: str) -> None:
    """Convert absolute imports to relative imports in all __init__.pyi files so Pyright can read them.
    stubgenj generates: import jneqsim.neqsim.process.processmodel
    Pyright needs:      from . import processmodel as processmodel
    """
    for dirpath, _, filenames in os.walk(stubs_root):
        for filename in filenames:
            if filename != "__init__.pyi":
                continue
            filepath = os.path.join(dirpath, filename)
            with open(filepath) as f:
                content = f.read()

            def replace_import(m: re.Match) -> str:
                full_module = m.group(1)
                alias = m.group(2) if m.group(2) else full_module.split(".")[-1]
                return f"from . import {alias} as {alias}"

            new_content = re.sub(
                r"^import\s+jneqsim\.neqsim[\w.]*\.([\w]+)(?:\s+as\s+(\w+))?$",
                replace_import,
                content,
                flags=re.MULTILINE,
            )

            if new_content != content:
                with open(filepath, "w") as f:
                    f.write(new_content)


_fix_absolute_to_relative_imports(os.path.join("./jneqsim", "neqsim"))
