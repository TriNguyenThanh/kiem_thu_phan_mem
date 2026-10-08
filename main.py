import subprocess
import sys


def main():
    """Chạy toàn bộ bộ kiểm thử đăng nhập UTC bằng Pytest."""
    cmd = [sys.executable, "-m", "pytest", *sys.argv[1:]]
    sys.exit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
