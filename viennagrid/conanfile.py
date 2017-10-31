from conans import ConanFile, CMake, tools
import os

class ViennagridConan(ConanFile):
    name = "viennagrid"
    version = "2.1.0"
    license = "MIT"
    url = "https://github.com/weatherhead99/conan-packages/tree/master/viennagrid"
    description = "ViennaGrid is a C++ library designed for the handling of structured and unstructured meshes in arbitrary spatial dimensions using different coordinate systems."
    generators = "cmake"
    
    def source(self):
        self.run("git clone https://github.com/viennagrid/viennagrid-dev")
        os.chdir("viennagrid-dev")
        self.run("git checkout release-2.1.0")

    def build(self):
        #need to specify generator otherwise conan complains about not specifying
        #settings
        cmake = CMake(self,generator="Unix Makefiles")
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["BUILD_EXAMPLES"] = "OFF"
        cmake.configure(source_dir="%s/viennagrid-dev" % self.conanfile_directory)
        cmake.build()
        cmake.install()
        
    def package(self):
        #not needed, done by cmake.install()
        pass
        
    def package_id(self):
        self.info.header_only()
