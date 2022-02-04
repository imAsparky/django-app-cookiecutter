"""django-app-cookiecutter test suite."""


def test_django_app_bakes_ok_with_defaults(cookies):
    """Test cookiecutter created the Django project ok."""

    default_app = cookies.bake()

    assert default_app.exit_code == 0
    assert default_app.project_path.is_dir()
    assert default_app.exception == None  # noqa: E711
    assert default_app.project_path.name == "django_app"


def test_baked_app_apps_py_file_ok(cookies):
    """Test App apps.py file has been generated correctly."""
    default_app = cookies.bake()

    apps_path = default_app.project_path / "apps.py"
    apps_file = str(apps_path.read_text().splitlines())

    assert '    name = "django_app"' in apps_file
    assert '    verbose_name = _("Django App")' in apps_file
    assert '    verbose_name_plural = _("Django Apps")' in apps_file


def test_baked_app_one_deep_apps_py_file_ok(cookies):
    """Test App apps.py file has been generated correctly with depth = one_deep."""
    non_default_app = cookies.bake(extra_context={"new_app_depth": "one_deep"})

    apps_path = non_default_app.project_path / "apps.py"
    apps_file = str(apps_path.read_text().splitlines())

    assert '    name = "bake00.django_app"' in apps_file
    assert '    verbose_name = _("Django App")' in apps_file
    assert '    verbose_name_plural = _("Django Apps")' in apps_file


def test_baked_app_custom_name_apps_py_file_ok(cookies):
    """Test App apps.py file has been generated correctly wit depth  one_deep."""
    non_default_app = cookies.bake(
        extra_context={"new_app_verbose_name": "Custom Name"}
    )

    apps_path = non_default_app.project_path / "apps.py"
    apps_file = str(apps_path.read_text().splitlines())

    assert '    name = "custom_name"' in apps_file
    assert '    verbose_name = _("Custom Name")' in apps_file
    assert '    verbose_name_plural = _("Custom Names")' in apps_file
