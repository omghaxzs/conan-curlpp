from conan import ConanFile
from conan.tools.scm import Git
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class CurlppConan(ConanFile):
    name = "curlpp"
    version = "0.8.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Curlpp here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        git = Git(self, folder=self.source_folder)
        git.clone('https://github.com/jpbarrette/curlpp.git', self.source_folder)
        git.checkout(f'v{self.version}')

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["curlpp"]
