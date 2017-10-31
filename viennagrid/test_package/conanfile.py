from conans import ConanFile, CMake

class ViennagridConanTest(ConanFile):
    settings = "os","compiler","build_type","arch"
    generators="cmake"
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()


        
    def test(self):
        self.run("bin/package_test")
        self.run("bin/package_test2")
