"""Execute all six research notebooks with separate kernels and save their outputs."""
from pathlib import Path
import os
import sys
import time

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager


NOTEBOOKS = (
    "01_Simulate_Monthly_Model.ipynb",
    "02_Estimate_Simulated_Data.ipynb",
    "03_Estimate_Actual_Monthly_Data.ipynb",
    "04_Construct_Annual_Model.ipynb",
    "05_Estimate_Annual_Model_and_Forecast.ipynb",
    "06_Simulate_and_Diagnose.ipynb",
)


def main():
    root = Path(__file__).resolve().parents[1]
    notebook_directory = root / "notebooks"
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    for variable, directory in (
        ("MPLCONFIGDIR", "matplotlib"),
        ("IPYTHONDIR", "ipython"),
        ("JUPYTER_CONFIG_DIR", "jupyter"),
        ("JUPYTER_RUNTIME_DIR", "jupyter_runtime"),
    ):
        cache = root / ".cache" / directory
        cache.mkdir(parents=True, exist_ok=True)
        environment[variable] = str(cache)

    for name in NOTEBOOKS:
        print(f"Running {name} in a fresh kernel", flush=True)
        started = time.perf_counter()
        path = notebook_directory / name
        notebook = nbformat.read(path, as_version=4)
        # Use this environment's interpreter, regardless of host kernel registrations.
        kernel = KernelManager(kernel_name="python3")
        kernel.kernel_spec.argv = [
            sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"
        ]
        client = NotebookClient(
            notebook, km=kernel, timeout=None, allow_errors=False,
            resources={"metadata": {"path": str(notebook_directory)}},
        )
        try:
            client.execute(env=environment, cleanup_kc=True)
            code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
            if any(cell.execution_count is None for cell in code_cells):
                raise RuntimeError("A code cell was not executed.")
            if any(output.output_type == "error" for cell in code_cells for output in cell.outputs):
                raise RuntimeError("The notebook contains an error output.")
            temporary = path.with_suffix(".ipynb.tmp")
            nbformat.write(notebook, temporary)
            temporary.replace(path)
        except Exception as error:
            print(f"Failed {name}: {error}", file=sys.stderr, flush=True)
            return 1
        print(f"Saved {name} ({len(code_cells)} code cells; "
              f"{time.perf_counter() - started:.1f} seconds)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
