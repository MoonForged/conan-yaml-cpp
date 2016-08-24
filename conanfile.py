from conans import ConanFile, CMake, tools
from conans.tools import download, unzip
import os
import shutil
import textwrap

class YamlCppConan( ConanFile ):
  name = 'yaml-cpp'
  version = '0.5.3'
  license = 'MIT https://github.com/jbeder/yaml-cpp/blob/master/LICENSE'
  url = 'https://github.com/MoonForged/conan-yaml-cpp'
  settings = 'os', 'compiler', 'build_type', 'arch'
  options = { 'shared': [ True, False ] }
  default_options = 'shared=False'
  generators = 'cmake'
  requires = 'Boost/1.60.0@lasote/stable'
  folder = '%s-%s-%s' % ( name, name, version )

  def source( self ):
    zip_name = '%s-%s.tar.gz' % ( self.name, self.version )
    download( 'https://github.com/jbeder/yaml-cpp/archive/%s' % zip_name, zip_name )
    unzip( zip_name )
    os.unlink( zip_name )
    shutil.move( '%s/CMakeLists.txt' % self.folder, '%s/CMakeListsOriginal.cmake' % self.folder )

    with open( '%s/CMakeLists.txt' % self.folder, 'w' ) as f:
      f.write( textwrap.dedent( '''\
        cmake_minimum_required( VERSION 2.8 )
        project( conanyamlcpp )
        include( ${CMAKE_CURRENT_SOURCE_DIR}/../conanbuildinfo.cmake )
        conan_basic_setup()
        include( "CMakeListsOriginal.cmake" )
        ''' ) )

  def build( self ):
    cmake = CMake( self.settings )
    flags = '-DBUILD_SHARED_LIBS=ON' if self.options.shared else ''
    self.run( 'cd %s && mkdir _build' % self.folder )
    configure_command = 'cd %s/_build && cmake .. %s' % ( self.folder, cmake.command_line )
    self.output.info( 'Configure with: %s' % configure_command )
    self.run( 'cd %s/_build && cmake .. %s %s' % ( self.folder, cmake.command_line, flags ) )
    self.run( "cd %s/_build && cmake --build . %s" % ( self.folder, cmake.build_config ) )

  def package( self ):
    self.copy( '*.h', dst='include', src='%s/include' % self.folder )
    self.copy( '*yaml-cpp*.lib', dst='lib', keep_path=False )
    self.copy( '*yaml-cpp*.dll', dst='bin', keep_path=False )
    self.copy( '*yaml-cpp*.so', dst='lib', keep_path=False )
    self.copy( '*yaml-cpp*.a', dst='lib', keep_path=False )

  def package_info( self ):
    if self.settings.os == 'Windows':
      self.cpp_info.libs = [ 'libyaml-cppmd' ]
    else:
      self.cpp_info.libs = [ 'yaml-cpp' ]
