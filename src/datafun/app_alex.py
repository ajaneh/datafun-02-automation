# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("P02", level="INFO")

# === DECLARE GLOBAL CONSTANTS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
PROCESSED_DIR: Final[Path] = DATA_DIR / "processed_custom"


CATION_LIST: Final[list[str]] = ["sodium", "calcium", "potassium"]
CHARGE_DICT: Final[dict[str, int]] = {
    "sodium": 1,
    "calcium": 2,
    "potassium": 1,
    "chloride": -1,
    "sulfate": -2,
    "nitrate": -1,
}
ANION_LIST: Final[list[str]] = ["chloride", "sulfate", "nitrate"]

WAIT_SECONDS: Final[int] = 1
FILE_COUNT: Final[int] = 2


# === DECLARE A HELPER FUNCTION TO WRITE A FILE ===


def write_text_file(*, path: Path, content: str) -> None:
    """Write content to a text file, creating parent directories as needed.

    Arguments:
        path: Full path to the file to create or overwrite.
        content: Text content to write.

    Returns:
        None
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    LOG.info(f"Wrote file: {path.name}")


# === DECLARE REPETITION FUNCTION 2: FOR LOOP OVER TWO LISTS ===


def create_files_from_list() -> None:
    """Create one text file per item in a list using a for loop.


    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 2: for loop over two lists")
    LOG.info("========================")

    LOG.info(f"Cation list: {CATION_LIST}")
    LOG.info(f"Anion list:  {ANION_LIST}")
    LOG.info("Creating one file per cation, with content about anion pairs")

    for cation_name in CATION_LIST:
        filename: str = f"{cation_name}.txt"
        path: Path = PROCESSED_DIR / filename
        content: str = f"Selected Cation '{cation_name}' - Complementary Anions: "
        for anion_name in ANION_LIST:
            content += f" '{anion_name}',"
        write_text_file(path=path, content=content)


# === DECLARE REPETITION FUNCTION 3: DICTIONARY COMPREHENSION ===


def create_files_using_list_comprehension() -> None:
    """
    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 3: Dictionary comprehension")
    LOG.info("========================")

    prefix: str = "Charge of "
    ion_list: list[str] = CATION_LIST + ANION_LIST

    for ion in ion_list:
        filename: str = f"{ion}_charge.txt"
        path: Path = PROCESSED_DIR / filename
        charge = CHARGE_DICT[ion]
        content: str = f"{prefix}: {charge}\n"
        write_text_file(path=path, content=content)


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None
    Returns: None
    """
    log_header(LOG, "P02")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    create_files_from_list()
    create_files_using_list_comprehension()

    LOG.info("========================")
    LOG.info("Executed successfully!")
    LOG.info("========================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: Only call main() when running this file directly as a script.
# This is standard Python boilerplate.

if __name__ == "__main__":
    main()
