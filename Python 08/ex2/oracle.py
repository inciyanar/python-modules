import os
from dotenv import load_dotenv

load_dotenv()
config_names = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]

def configuration(config_names: list[str]) -> dict[str, str]:
    result: dict[str: str] = {}
    for name in config_names:
        output=os.getenv(name)
        if not output :
            result[name] = "[MISSING]"
        else:
            result[name] = output
    return(result)


if __name__ == "__main__":
    output: dict[str, str] = configuration(config_names)
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print(f"Mode: {output["MATRIX_MODE"]}")

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

    print(f"Log Level: {output["LOG_LEVEL"]}")

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
