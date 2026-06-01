"""Post-process generated stubs to fix imports for Pyright/Pylance.
This script
1. Adds 'import jneqsim' to all .pyi files so qualified type refs resolve.
2. Converts absolute imports to 'from . import X as X' in __init__.pyi files so Pyright can resolve them.
"""

import os
import re

JNEQSIM_IMPORT = "import jneqsim\n"


def fix_stub_files(stubs_root: str) -> None:
    files_processed = 0

    for dirpath, _, filenames in os.walk(stubs_root):
        for filename in filenames:
            if not filename.endswith(".pyi"):
                continue
            filepath = os.path.join(dirpath, filename)
            files_processed += 1

            with open(filepath) as f:
                content = f.read()

            new_content = content

            # Add 'import jneqsim' at the top if not already present
            if not re.search(r"^import jneqsim$", new_content, re.MULTILINE):
                new_content = JNEQSIM_IMPORT + new_content

            # For __init__.pyi files, convert absolute imports to relative
            if filename == "__init__.pyi":

                def replace_import(m: re.Match) -> str:
                    full_module = m.group(1)
                    alias = m.group(2) if m.group(2) else full_module.split(".")[-1]
                    return f"from . import {alias} as {alias}"

                new_content = re.sub(
                    r"^import\s+jneqsim\.neqsim[\w.]*\.([\w]+)(?:\s+as\s+(\w+))?\r?$",
                    replace_import,
                    new_content,
                    flags=re.MULTILINE,
                )

            if new_content != content:
                with open(filepath, "w") as f:
                    f.write(new_content)

    print(f"Processed {files_processed} .pyi files.")


if __name__ == "__main__":
    fix_stub_files(os.path.join("./jneqsim", "neqsim"))
