from conans import ConanFile, CMake
import os

class YamlCppTestConan( ConanFile ):
  settings = 'os', 'compiler', 'build_type', 'arch'
  generators = 'cmake'

  def build( self ):
    cmake = CMake( self.settings )
    self.run( 'cmake "%s" %s' % ( self.conanfile_directory, cmake.command_line ) )
    self.run( 'cmake --build . %s' % cmake.build_config )

  def imports( self ):
    self.copy( '*.dll', 'bin', 'bin' )
    self.copy( '*.dylib', 'bin', 'bin' )

  def test( self ):
    os.chdir( 'bin' )
    self.run( '.%sexample' % os.sep )
