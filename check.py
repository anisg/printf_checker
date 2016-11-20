#!/usr/bin/env python
import argparse
import os

version='0.1'
default_file='examples.txt'
script_dir=os.path.dirname(os.path.realpath(__file__))
dir_tmp=script_dir + '/' + 'tmp'

def shell_exec(cmd): 
	return os.popen(cmd).read() 

def file_put_contents(filename, data):
	f = open(filename, 'w')
	f.write(data)
	f.close()

def exec_code(code,name, index, lib_path):
	c_file=dir_tmp + '/' + name+ '_' +'test'+str(index)+'.c'
	c_bin=dir_tmp + '/' +name+ '_' +'bin'+str(index)
	shell_exec('echo \''+ code +'\' > '+c_file)
	shell_exec('gcc -o '+ c_bin +' '+ c_file +' '+ lib_path)
	s = shell_exec(dir_tmp + '/./' + name +'_bin'+str(index))
	os.remove(c_file)
	os.remove(c_bin)
	return s

def compile_tests(lib_path, header_path, filename):
	count=0
	c_write_true_begin='#include <stdio.h>\nint main(void){printf('
	c_write_true_end=');return(0);}'
	c_write_false_begin='#include \"'+ os.path.abspath(header_path) +'\"\nint main(void){ft_printf('
	c_write_false_end=c_write_true_end
	try:
		os.mkdir(dir_tmp)
	except:
		pass
	lines = filter(None, open(filename).read(1000).split('\n'))
	for i in range(0,len(lines)):
		s1 = exec_code(c_write_true_begin + lines[i] + c_write_true_end, 'true', i, '')
		s2 = exec_code(c_write_false_begin + lines[i] + c_write_true_end, 'false', i, lib_path)
		if s1 == s2:
			count += 1
		else:
			print '\033[91mfail for n'+ str(i) +' : output diff\033[0m'
			print '\033[94mthe content >>\033[0m' + lines[i] + '\033[94m<<\033[0m'
			print '\033[92mreal printf >>\033[0m' + s1 + '\033[92m<<\033[0m'
			print '\033[93myour printf >>\033[0m' + s2 + '\033[93m<<\033[0m'
			print ''
	print 'result for file \''+filename+'\': '+ str(count) + ' / ' + str(len(lines))

def main():
	parser = argparse.ArgumentParser(description='printf checker v'+ version +', check your ft_printf')
	parser.add_argument('-f', '--file',required=False,  default=script_dir + '/' + default_file,
		help='the name of the file you want to test (default: '+ default_file +')')
	parser.add_argument('-p', '--path',required=True,
                   help='the path of your libftprintf.a (example: ~/project/ft_printf/libftprintf.a), note: if you provide just the directory, we will try to do a make')
	parser.add_argument('-head', '--header',required=True,
                   help='the path of libft.h or libftprintf.h (example: ~/project/ft_printf/libftprintf.h)')
	args = parser.parse_args()
	''' verification: do a make or not? '''
	lib_path=args.path
	if os.path.isdir(args.path) == True:
		print shell_exec('make -C '+args.path)
		if os.path.isfile(args.path + '/' + 'libft.a') == True:
			lib_path=args.path + '/' + 'libft.a'
		if os.path.isfile(args.path + '/' + 'libftprintf.a') == True:
			lib_path=args.path + '/' + 'libftprintf.a'
	if os.path.isfile(lib_path) != True or os.path.isfile(args.header) != True or os.path.isfile(args.file) != True:
		print 'error: one the argument you provided isn\'t a file'
		return 0
	compile_tests(lib_path, args.header, args.file)

if __name__ == '__main__':
  main()
