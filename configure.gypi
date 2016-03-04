{
  'variables': {
	'build_with_botan' : '0',
	# botan headers
	'botan_headers' : './third_party/botan/build/include',
	# botan libs
	'botan_libs' : './third_party/botan/botan.lib',
	'build_with_openssl' : '1',
	# openssl headers
	'openssl_headers' : './third_party/openssl/include',
	# openssl lib
	'openssl_libs' : ['./third_party/openssl/out32/ssleay32.lib','./third_party/openssl/out32/libeay32.lib'],
	# Compile with GOST support
	'enable_ghost' : '1',
	# Compile with ECC support
	'enable_ecc' : '1',
	# Define if advanced AES key wrap without pad is supported
	'enable_aes_key_wrap' : '0',
	# Debug to stderr
	'enable_debug_to_stderr' : '1',
	# enable unix mutex
	'enable_pthread' : '0',
	# cppunit headers
	'cppunit_headers' : './third_party/cppunit/include',
	# cppunit libs
	'cppunit_libs' : './third_party/cppunit/lib/cppunitd.lib',
	# PACKAGE_VERSION
	'package_version' : '2.0.0b2',
	# VERSION_MAJOR
	'version_major' : '2',
	# VERSION_MINOR
	'version_minor' : '0',
	# MAX_PIN_LEN 
	'max_pin_len' : 255,
	# MIN_PIN_LEN 
	'min_pin_len' : 4,
	# DEFAULT_SOFTHSM2_CONF
	'default_softhsm2_conf' : 'softhsm2.conf',
	# DEFAULT_LOG_LEVEL
	'default_log_level' : "INFO",
	# DEFAULT_OBJECTSTORE_BACKEND
	'default_objectstore_backend' : 'file',
	# DEFAULT_TOKENDIR 
	'default_tokendir' : 'tokens'
  }
}