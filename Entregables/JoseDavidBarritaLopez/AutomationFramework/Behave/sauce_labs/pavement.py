import threading
import os.path
import sys

sys.path.append(os.path.abspath(""))

from paver.easy import sh, task, consume_nargs
from utils.settings.behave_local_runner import BehaveLocalRunner


@task
@consume_nargs(7)
def run_feature(args):
    BehaveLocalRunner().with_local_testing_suite(args[0]).with_local_platform(
        args[1]
    ).with_local_platform_version(args[2]).with_local_device_name(
        args[3]
    ).with_local_environment(
        args[4]
    ).with_local_program(
        args[5]
    ).with_local_feature(
        args[6]
    ).run_local_by_feature()


@task
@consume_nargs(1)
def report(args):
    generate_allure_report(args[0])


def generate_allure_report(platform):
    sh(f"allure serve reports/{platform}")
