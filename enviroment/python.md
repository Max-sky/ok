首先需要按ESC键回到命令模式；
然后输入命令:w fileName，文件不存在会自动新建文件。



								            








pip指定python版本安装						
（1） pip install -t /usr/lib/python3.4/site-packages/ccxt ccxt
     

（2）mv pip pip3

https://blog.csdn.net/junbujianwpl/article/details/51598506
SOLUTIONS

方法步骤：

1、保证2个版本的Python都安装了pip。

首先默认的Python版本大多数安装了pip，如果没有，也很容易通过一条指令安装

sudo apt install python-pip1

如何为另一版本python安装pip呢。第一种可以通过源码的方式，下载源码，再用指定的python版本执行安装

python3.5 setup.py install 1

另外可以从官网下载 get-pip.py，然后执行：

 

python3.5 get-pip.py1

即完成为Python3.5版本安装pip。

2、创建pip3.5

先看下pip文件的内容:

vim /usr/bin/pip1

  1 #!/usr/bin/python                                                           
  2 # GENERATED BY DEBIAN
  3 
  4 import sys
  5 
  6 # Run the main entry point, similarly to how setuptools does it, but because
  7 # we didn't install the actual entry point from setup.py, don't use the
  8 # pkg_resources API.
  9 from pip import main
 10 if __name__ == '__main__':
 11     sys.exit(main())
~                           123456789101112

亲，发现亮点没有，在第一行啊。#!/usr/bin/python。记得在修改默认python版本时的做法吗。修改软链接指定另外的Python版本。此处，只需要将python换成python3.5。那这个pip文件就是python3.5专属的pip脚本了啊。亲，感到激动了木有。是不是很简单就搞定了这个曾经一度困扰的世界性难题。 
那么解决方案来了将第一行python改为python3.5，另存为/usr/bin/pip3.5，即可。 
当需要为python3.5安装相应的类库时：

pip3.5 install pymongo1



mac:
卸载pip     python3 -m pip uninstall pip setuptools 
             cur   https://bootstrap.pypa.io/get-pip.py | python3
	     
	     


库：sklearn  matplotlib  tushare  beautifulsoup4  tensorflow    keras 

