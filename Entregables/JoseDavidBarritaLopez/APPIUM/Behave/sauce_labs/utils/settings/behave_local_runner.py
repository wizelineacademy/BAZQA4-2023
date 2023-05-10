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