import os
import sys

from g4f.config import AppConfig
from g4f.api import run_api


def main() -> None:
    bind = os.environ.get("G4F_BIND", "127.0.0.1:18091")
    if len(sys.argv) > 1:
        bind = sys.argv[1]
    AppConfig.load_from_env()
    run_api(bind=bind, debug=False)


if __name__ == "__main__":
    main()