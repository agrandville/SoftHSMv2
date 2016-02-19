{
	'includes': [
		'configure.gypi'
	],
	'targets' : [{
			'target_name' :
				'cryptotest',
			'type' :
				'executable',
			'sources' : [
				'src/lib/crypto/test/AESTests.cpp',
				'src/lib/crypto/test/chisq.c',
				'src/lib/crypto/test/cryptotest.cpp',
				'src/lib/crypto/test/DESTests.cpp',
				'src/lib/crypto/test/DHTests.cpp',
				'src/lib/crypto/test/DSATests.cpp',
				'src/lib/crypto/test/ECDHTests.cpp',
				'src/lib/crypto/test/ECDSATests.cpp',
				'src/lib/crypto/test/GOSTTests.cpp',
				'src/lib/crypto/test/HashTests.cpp',
				'src/lib/crypto/test/MacTests.cpp',
				'src/lib/crypto/test/RNGTests.cpp',
				'src/lib/crypto/test/RSATests.cpp',
				'src/lib/crypto/test/ent.c',
				'src/lib/crypto/test/randtest.c'
			],
			'include_dirs' : [
				'src/lib/cryptoki_compat',
				'src/bin/common',
				'src/lib',
				'src/lib/crypto',
				'../../cppunit/cppunit/include',
				'src/lib/data_mgr',
				'src/lib/object_store',
				'src/lib/session_mgr',
				'src/lib/slot_mgr',
				'src/lib/common'
			],
			'conditions' : [
				['OS=="win"',{
					'sources' : [
						'src/bin/win32/getopt.cpp',
						#'src/bin/win32/config.h',
						'src/lib/win32/syslog.cpp',
					],
					'include_dirs' : [
						'src/lib/win32',
						'src/bin/win32'
					],
					'libraries' : [
						'convarch.lib',
						'Advapi32.lib',
						'User32.lib',
						'Crypt32.lib',
						'Gdi32.lib',
						'cppunit.lib'
					]
				}],
#				[ 'build_configuration=="debug"', {
#					'libraries' : [
#						'../../cppunit/cppunit/lib/cppunitd.lib'
#					],}
#				],
				[ 'build_with_botan==1', {
					'include_dirs' : [
						'../../botan/build/include'
					],
					'libraries' : [
						'../../botan/botan.lib'
					],
					'defines': [
						'WITH_BOTAN',
					]					
				}],
				[ 'build_with_openssl==1', {
					'include_dirs' : [
						'../../openssl/include'
					],
					'libraries' : [
						'../../openssl/out32/ssleay32.lib',
						'../../openssl/out32/libeay32.lib',
					],
					'defines': [
						'WITH_OPENSSL',
					]					
				}],
				[ 'enable_debug_to_stderr==1', {'defines': ['DEBUG_LOG_STDERR',],}],
			]
		}
	],
    'target_defaults': {
		'default_configuration': 'Release',
		'configurations': {
		'Debug': {
			'defines': [ 'DEBUG', '_DEBUG' ],
			'msvs_settings': {
				'VCCLCompilerTool': {
					'RuntimeLibrary': 1, 
					'Optimization': 0,
				},
				'VCLinkerTool': {
					'LinkTimeCodeGeneration': 0,
					'OptimizeReferences': 0,
					'EnableCOMDATFolding': 2,
					'LinkIncremental': 1,
					'GenerateDebugInformation': 'true',
					'AdditionalLibraryDirectories': [
						'../../openssl/out32.dbg',
						'Debug/lib',
						'../../cppunit/cppunit/lib.dbg'
					],
				}          
			},
		},
		'Release': {
			'defines': [ 'NDEBUG' ],
			'msvs_settings': {
			'VCCLCompilerTool': {
				'RuntimeLibrary': 0,
				'Optimization': 3,
				'FavorSizeOrSpeed': 1,
				'InlineFunctionExpansion': 2,
				'WholeProgramOptimization': 'true',
				'OmitFramePointers': 'true',
				'EnableFunctionLevelLinking': 'true',
				'EnableIntrinsicFunctions': 'true' 
			},
			'VCLinkerTool': {
				'LinkTimeCodeGeneration': 1,
				'OptimizeReferences': 2,
				'EnableCOMDATFolding': 2,
				'LinkIncremental': 1,
				'AdditionalLibraryDirectories': [
					'../../openssl/out32',
					'Release/lib',
					'../../cppunit/cppunit/lib'
				]            
			}
			},
			'variables': {
				'build_configuration' : 'release',
			}			
		}
		}  
	}
}
