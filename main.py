
from datetime import datetime

PROJECT_NAME = "EduMind AI"
PROJECT_VERSION = "0.1.0"


def main():
    print("=" * 45)
    print(f"Welcome to {PROJECT_NAME}")
    print(f"Version: {PROJECT_VERSION}")
    print("Institution: University")
    print("Focus: Data Science, Machine Learning and AI")
    print(f"Started: {datetime.now():%Y-%m-%d %H:%M}")
    print("=" * 45)
    print("Project setup successful!")


if __name__ == "__main__":
    main()
