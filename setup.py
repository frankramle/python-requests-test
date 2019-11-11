from setuptools import setup

setup(
	name = 'python-request-test',
	version = '0.1',
	install_requires = [
		'Click',
		'requests'
	],
	py_modules = ['commandClick'],
	entry_points = '''
	[console_scripts]
	beonit=commandClick:runTest
	'''
)