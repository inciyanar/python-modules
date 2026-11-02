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
    print(f"Database: {output["DATABASE_URL"]}")
    print(f"API Access: {output["API_KEY"]}")
    print(f"Log Level: {output["LOG_LEVEL"]}")
    print(f"Zion Network: {output["ZION_ENDPOINT"]}")
    print()
    print("Environment security check:")
    print("The Oracle sees all configurations.")
