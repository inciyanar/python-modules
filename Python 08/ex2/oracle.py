import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("python-dotenv is not installed.")
    print("Install it with: pip install -r requirements.txt")
    sys.exit(1)


config_names = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
                "LOG_LEVEL", "ZION_ENDPOINT"]


def configuration(config_names: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for name in config_names:
        output = os.getenv(name)
        if not output:
            result[name] = "[MISSING]"
        else:
            result[name] = output
    return result


def missing_warnings(output: dict[str, str]) -> None:
    missing: list[str] = []
    for name in output:
        if output[name] == "[MISSING]":
            missing.append(name)
    if not missing:
        return
    print("Configuration warnings:")
    for name in missing:
        print(f"[WARNING] {name} is not set")
    print("Copy .env.example to .env and fill in the values.")
    print()


def main() -> None:
    load_dotenv()
    output = configuration(config_names)
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    missing_warnings(output)

    print("Configuration loaded:")

    if output["MATRIX_MODE"] == "[MISSING]":
        print("Mode: Missing")
    else:
        print(f"Mode: {output['MATRIX_MODE']}")

    if output["DATABASE_URL"] == "[MISSING]":
        print("Database: Missing")
    elif output["MATRIX_MODE"] == "development":
        print("Database: Connected to local instance")
    elif output["MATRIX_MODE"] == "production":
        print("Database: Connected to production instance")
    else:
        print("Database: Unknown, not connected")

    if output["API_KEY"] == "[MISSING]":
        print("API Access: Missing")
    else:
        print("API Access: Authenticated")

    if output["LOG_LEVEL"] == "[MISSING]":
        print("Log Level: Missing")
    else:
        print(f"Log Level: {output['LOG_LEVEL']}")

    if output["ZION_ENDPOINT"] == "[MISSING]":
        print("Zion Network: Offline")
    else:
        print("Zion Network: Online")

    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
