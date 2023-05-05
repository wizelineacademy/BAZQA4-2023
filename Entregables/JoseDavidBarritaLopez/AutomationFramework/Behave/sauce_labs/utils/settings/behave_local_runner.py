from typing import Optional
from paver.easy import sh, task, consume_nargs


class BehaveLocalRunner:
    def __init__(self):
        self.testing_suite: Optional[str] = None
        self.platform: Optional[str] = None
        self.platform_version: Optional[str] = None
        self.device_name: Optional[str] = None
        self.environment: Optional[str] = None
        self.program: Optional[str] = None
        self.feature: Optional[str] = None
        self.scenario: Optional[str] = None

    def with_local_testing_suite(self, testing_suite: str):
        self.testing_suite = testing_suite
        return self

    def with_local_platform(self, platform: str):
        self.platform = platform
        return self

    def with_local_platform_version(self, platform_version: str):
        self.platform_version = platform_version
        return self

    def with_local_device_name(self, device_name: str):
        self.device_name = device_name
        return self

    def with_local_environment(self, environment: str):
        self.environment = environment
        return self

    def with_local_program(self, program: str):
        self.program = program
        return self

    def with_local_feature(self, feature: str):
        self.feature = feature
        return self

    def with_local_scenario(self, scenario: str):
        self.scenario = scenario
        return self

    def get_string_with_parameters(self, testing_suite, platform, platform_version, device_name, environment, program,
                                   feature, scenario=None):
        sh_string = (f"behave --tags={testing_suite} "
                     f"-D platform={platform} "
                     f"-D platform_version={platform_version} "
                     f"-D device_name={device_name} "
                     f"-D environment={environment} "
                     f"-D program={program} "
                     f"-D testing_process=serial "
                     f"-D driver_location=local "
                     f"-f allure_behave.formatter::AllureFormatter -f pretty "
                     f"-o reports/{platform} "
                     f"features/{program}/{feature}.feature")
        if scenario is not None:
            sh_string += f'-n "{self.scenario}"'

        return sh_string

    def run_local_by_feature(self):
        if None in (self.testing_suite, self.platform, self.platform_version, self.device_name, self.environment,
                    self.program, self.feature):
            raise ValueError("Missing required parameters")
        sh_terminal = self.get_string_with_parameters(self.testing_suite, self.platform, self.platform_version,
                                                      self.device_name,
                                                      self.environment,
                                                      self.program, self.feature)
        try:
            sh(sh_terminal)
        except Exception as e:
            print(f" [behave_local_runner][run_local_by_scenario] An error occurred: {e}")

    def run_local_by_scenario(self):
        if None in (self.testing_suite, self.platform, self.platform_version, self.device_name, self.environment,
                    self.program, self.feature, self.scenario):
            raise ValueError("Missing required parameters")

        sh_terminal = self.get_string_with_parameters(self.testing_suite, self.platform, self.platform_version,
                                                      self.device_name,
                                                      self.environment,
                                                      self.program, self.feature)
        try:
            sh(sh_terminal)
        except Exception as e:
            print(f" [behave_local_runner][run_local_by_scenario] An error occurred: {e}")


############################# ------------------------------------ ##############################
############################# COMENTS FOR THE FUTURE FROM PAVEMENT ##############################
############################# ------------------------------------ ##############################

"""
@task
@consume_nargs(4)
def run_all(args):
    run_behave_all(args[0], args[1], args[2], args[3])


def run_behave_all(testing_suite, platform, platform_version, device_name):
    sh(f'behave --tags={testing_suite} '
       f'-D platform={platform} '
       f'-D platform_version={platform_version} '
       f'-D testing_process=serial '
       f'-D driver_location=local '
       f'-D environment={ENVIRONMENT} '
       f'-D device_name={device_name} '
       f'-f allure_behave.formatter::AllureFormatter '
       f'-o reports/{platform}')
"""

"""
@task
@consume_nargs(6)
def run_program(args):
    run_behave_program(args[0], args[1], args[2], args[3], args[4], args[5])


def run_behave_program(testing_suite, platform, platform_version, device_name, environment, program):
    sh(f'behave --tags={testing_suite} '
       f'-D platform={platform} '
       f'-D platform_version={platform_version} '
       f'-D device_name={device_name} '
       f'-D environment={environment} '
       f'-D program={program} '
       f'-D testing_process=serial '
       f'-D driver_location=local '
       f'-f allure_behave.formatter::AllureFormatter -f pretty '
       f'-o reports/{platform} '
       f'features/{program}/')


@task
@consume_nargs(6)
def run_browserstack_program(args):
    run_behave_browserstack_program(args[0], args[1], args[2], args[3], args[4], args[5])


def run_behave_browserstack_program(test_suite, platform, device, environment, build_name, program):
    sh(f'behave --tags={test_suite} '
       f'-D platform={platform} '
       f'-D driver_location=browserstack '
       f'-D testing_process=serial '
       f'-D environment={environment} '
       f'-D device_name={device} '
       f'-D build_name={build_name} '
       f'-f pretty '
       f'features/{program}/')
"""

"""
@task
@consume_nargs(3)
def run_browserstack_all(args):
    run_behave_browserstack_all(args[0], args[1], args[2])


def run_behave_browserstack_all(platform, device, build_name):
    sh(f'behave --tags=e2e '
       f'-D platform={platform} '
       f'-D driver_location=browserstack '
       f'-D testing_process=serial '
       f'-D environment={ENVIRONMENT} '
       f'-D device_name={device} '
       f'-D build_name={build_name} '
       f'-f pretty ')

"""

"""
@task
@consume_nargs(3)
def run_browserstack_parallel_all(args):
    parallel_threads = []
    for index in range(CONCURRENT_DEVICES):
        thread = threading.Thread(target=run_behave_browserstack_parallel_all,
                                  args=(index, args[0], args[1], args[2]))
        parallel_threads.append(thread)
        thread.start()
    for thread in parallel_threads:
        thread.join()


def run_behave_browserstack_parallel_all(index, testing_suite, platform, build_name):
    users_phones = USERS_PHONE_NUMBERS.split(",")
    user_phone = users_phones[index % len(users_phones)]

    sh(f'export THREAD_ID={index} && '
       f'export USER_PHONE_NUMBER={user_phone} && '
       f'behave --tags={testing_suite} '
       f'-k --verbose '
       f'-D platform={platform} '
       f'-D driver_location=browserstack '
       f'-D testing_process=parallel '
       f'-D environment={ENVIRONMENT} '
       f'-D device_name=none '
       f'-D build_name={build_name} '
       f'-f pretty ')


@task
@consume_nargs(4)
def run_browserstack_parallel_feature(args):
    parallel_threads = []
    for index in range(CONCURRENT_DEVICES):
        thread = threading.Thread(target=run_behave_browserstack_parallel_feature,
                                  args=(index, args[0], args[1], args[2], args[3]))
        parallel_threads.append(thread)
        thread.start()
    for thread in parallel_threads:
        thread.join()


def run_behave_browserstack_parallel_feature(index, testing_suite, platform, build_name, feature):
    users_phones = USERS_PHONE_NUMBERS.split(",")
    user_phone = USERS_PHONE_NUMBERS[index % len(users_phones)]

    sh(f'export THREAD_ID={index} && '
       f'export USER_PHONE_NUMBER={user_phone} && '
       f'behave --tags={testing_suite} '
       f'-k --verbose '
       f'-D platform={platform} '
       f'-D driver_location=browserstack '
       f'-D testing_process=parallel '
       f'-D environment={ENVIRONMENT} '
       f'-D device_name=none '
       f'-D build_name={build_name} '
       f'-f pretty features/{feature}/')


def run_behave_browserstack_parallel_scenario(index, testing_suite, platform, build_name, feature, scenario):
    users_phones = USERS_PHONE_NUMBERS.split(",")
    user_phone = users_phones[index % len(users_phones)]

    sh(f'export THREAD_ID={index} && '
       f'export USER_PHONE_NUMBER={user_phone} && '
       f'behave --tags={testing_suite} '
       f'-k --verbose '
       f'-D platform={platform} '
       f'-D driver_location=browserstack '
       f'-D testing_process=parallel '
       f'-D environment={ENVIRONMENT} '
       f'-D device_name=none '
       f'-D build_name={build_name} '
       f'features/scenarios/{feature}.feature '
       f'-n {scenario}')
"""

"""
@task
@consume_nargs(5)
def run_browserstack_parallel_scenario(args):
    parallel_threads = []
    for index in range(CONCURRENT_DEVICES):
        thread = threading.Thread(target=run_behave_browserstack_parallel_scenario,
                                  args=(index, args[0], args[1], args[2], args[3], args[4]))
        parallel_threads.append(thread)
        thread.start()
    for thread in parallel_threads:
        thread.join()

@task
@cmdopts([('testing_suite=', '-testing_suite', 'The testing suite to be executed'),
          ('platform_name=', '-platform_name', 'The platform where this will be executed (android/ios'),
          ('platform_version=', '-platform_version', 'The OS version of the device you want to use (chio: 10)'),
          ('device_name=', '-device_name', 'The name of the device separated with "_"'),
          ('environment=', '-environment', 'The environment where you want to execute the test (dev/qa/prod)'),
          ('testing_process=', '-testing_process', 'The testing process to use (serial/parallel)'),
          ('driver_location=', '-driver_location', 'The location of the driver to be used (local/browserstack)'),
          ('feature=', '-feature', 'The feature to use (canal/nuevas_iniciativas/etc)')])
def run_behave_feature_experimental(options):
    subprocess.run(f'behave --tags={options.testing_suite} '
                   f'-D platform={options.platform} '
                   f'-D platform_version={options.platform_version} '
                   f'-D device_name={options.device_name} '
                   f'-D environment={options.environment} '
                   f'-D testing_process={options.testing_process} '
                   f'-D driver_location={options.driver_location} '
                   f'-f allure_behave.formatter::AllureFormatter -f pretty '
                   f'-o reports/{options.platform} '
                   f'features/{options.feature}/', shell=True)
"""
