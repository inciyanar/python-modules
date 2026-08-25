def secure_archive(file_name: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as f:
                read_data = f.read()
            return (True, read_data)
        elif action == "write":
            with open(file_name, "w") as f2:
                f2.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid action: '{action}'")
    except OSError as a:
        return (False, str(a))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from an nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("in.txt", "read"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("text.txt", "read"))
    print()

    print("Using 'secure_archive' to write previous to a new file:")
    print(secure_archive("new_file.txt", "write", "some content"))
    print()

    print("Invalid action case:")
    print(secure_archive("text.txt", "zort"))
    print()
