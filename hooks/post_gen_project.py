#!/usr/bin/env python
"""django-cookiecutter post project generation jobs."""
import os
import re


def update_apps_py_file_with_name(
    DEPTH_FROM_ROOT: str = None, PROJECT_DIRECTORY: list = None
) -> None:

    APP_NAME: str = ""

    # Create the new django app name
    match DEPTH_FROM_ROOT:

        case "in_project_root":
            APP_NAME = PROJECT_DIRECTORY[-1]
        case "one_deep":
            APP_NAME = ".".join(
                [
                    PROJECT_DIRECTORY[-2],
                    PROJECT_DIRECTORY[-1],
                ]
            )
        case "two_deep":
            APP_NAME = ".".join(
                [
                    PROJECT_DIRECTORY[-4],
                    PROJECT_DIRECTORY[-3],
                    PROJECT_DIRECTORY[-2],
                    PROJECT_DIRECTORY[-1],
                ]
            )
        case "three_deep":
            APP_NAME = ".".join(
                [
                    PROJECT_DIRECTORY[-4],
                    PROJECT_DIRECTORY[-3],
                    PROJECT_DIRECTORY[-2],
                    PROJECT_DIRECTORY[-1],
                ]
            )
    try:
        with open("apps.py", "r+", encoding="utf-8") as f:
            text = f.read()
            text = re.sub("update_name", APP_NAME, text)
            text = re.sub(
                "update_verbose_name", "{{cookiecutter.new_app_verbose_name}}", text
            )
            text = re.sub(
                "update_verbose_plural_name",
                "{{cookiecutter.new_app_verbose_name}}" "s",
                text,
            )
            f.seek(0)
            f.write(text)
            f.truncate()

    except OSError as exception:
        print(
            "\nAPP POST GENERATION UPDATE ERROR\n",
            exception,
            "\nYour apps.py file has not been generated correctly or missing.",
            "\nPlease update the apps.py `names` values or your app wont work",
            "\nas expected.",
        )
    finally:
        f.close()
        print(
            "\nSUCCESS: Your {{cookiecutter.new_app_verbose_name}} \
            app has been generated successfully!",
            "\nRemember to:"
            "\n1. Check apps.py has the correct `names` values inserted.",
            "\n2. Add ",
            APP_NAME,
            " to installed apps.",
            "\n3. Update the appropriate urls.py files.",
        )


if __name__ == "__main__":

    update_apps_py_file_with_name(
        "{{cookiecutter.new_app_depth}}",
        list(os.path.realpath(os.path.curdir).split("/")),
    )
