from path import Path as path
import environ
import os

INSTALLED_APPS = (
    'kdl_careerpaths'
)

env = environ.Env(
    LMS_URL=(str, None)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

APP_ROOT = (
    path(__file__).abspath().dirname().dirname()
)  # /blah/blah/blah/.../example-digital-learning-openedx/openedx_plugin
REPO_ROOT = APP_ROOT.dirname()  # /blah/blah/blah/.../example-digital-learning-openedx


LMS_URL = env("LMS_URL")



def plugin_settings(settings):
    # Update the provided settings module with any app-specific settings.
    # For example:
    #     settings.FEATURES['ENABLE_MY_APP'] = True
    #     settings.MY_APP_POLICY = 'foo'
    pass