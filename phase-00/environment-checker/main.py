import os
import platform
import shutil
import sys

import requests


def check_python():
    version = sys.version.split()[0]
    print(f"✓ Python {version}")
    return True


def check_virtual_environment():
    if sys.prefix != sys.base_prefix:
        print("✓ Virtual environment active")
        return True

    print("✗ Virtual environment not active")
    return False


def check_git():
    git_path = shutil.which("git")

    if git_path:
        print(f"✓ Git installed: {git_path}")
        return True

    print("✗ Git not found")
    return False


def check_requests():
    try:
        print(f"✓ requests {requests.__version__}")
        return True
    except AttributeError:
        print("✗ requests could not be verified")
        return False


def check_system():
    print(f"✓ Operating System: {platform.system()} {platform.release()}")
    print(f"✓ Machine: {platform.machine()}")


def check_docker():
    docker_path = shutil.which("docker")

    if docker_path:
        print(f"✓ Docker installed: {docker_path}")
        return True

    print("✗ Docker not installed")
    return False


def check_postgresql():
    postgres_path = shutil.which("psql")

    if postgres_path:
        print(f"✓ PostgreSQL client installed: {postgres_path}")
        return True

    print("✗ PostgreSQL client not found")
    return False


def check_disk_space():
    total, used, free = shutil.disk_usage(os.getcwd())

    free_gb = free / (1024 ** 3)

    print(f"✓ Free disk space: {free_gb:.2f} GB")

    return free_gb >= 10


def check_internet():
    try:
        response = requests.get("https://example.com", timeout=5)

        if response.ok:
            print("✓ Internet connection available")
            return True

        print("✗ Internet connection check failed")
        return False

    except requests.RequestException:
        print("✗ Internet connection unavailable")
        return False


def main():
    print("=" * 45)
    print("AI DEVELOPMENT ENVIRONMENT CHECK")
    print("=" * 45)

    results = []

    results.append(check_python())
    results.append(check_virtual_environment())
    results.append(check_git())
    results.append(check_requests())

    check_system()

    results.append(check_docker())
    results.append(check_postgresql())
    results.append(check_disk_space())
    results.append(check_internet())

    print("=" * 45)

    if all(results):
        print("Environment Status: READY")
    else:
        print("Environment Status: NOT READY")
        print("Some required tools still need attention.")

    print("=" * 45)


if __name__ == "__main__":
    main()