# WorthyPiServer
树莓派打造成一个智能终端,通过手机控制收听广播。

树莓派吃灰记——Flask搭建web服务
https://www.jianshu.com/p/b893f6fb88e2

将树莓派打造成一个智能终端，就需要能通过手机控制树莓派。要达到这个目的，最容易的方式就是搭建一个web服务，通过接口完成操作请求。下面，我们用Flask框架搭建一个web服务，并通过iPhone控制树莓派播放BBC互联网广播。

安装播放器
为了能播放互联网广播，我们需要一个播放器。通过ssh登录,调用apt命令安装mplayer：

apt-get install mplayer
完成后我们试验一下，输入：

mplayer http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-einws
有没有听到地道的英国伦敦腔？

使用Flask框架
web框架的选择有很多，Flask是相对来说非常简便的。
关于flask教程，可以通过官方文档查看。本地创建main.py，最小的flask程序长得是这样的：

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
修饰符route指定了路径，下面方法是入口方法。通过python命令运行，然后打开浏览器访问http://127.0.0.1:5000/
如果能看到熟悉的'Hello World!'，恭喜你成功了。

下面我们需要定义两个接口，用于控制播放与停止：

@app.route('/radio/play')
def radio_play():
    //TODO
    return 'play'

@app.route('/radio/stop')
def radio_stop():
    //TODO
    return 'stop'
接下来要做的就是通过python调用mplayer完成播放广播任务，可以封装一个Radio模块处理相关任务:

class Radio:
    def play(self):
        self.process = subprocess.Popen(['mplayer','http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-einws'],stdin=subprocess.PIPE)
    def stop(self):
            self.process.communicate(input=b'q')
切回main.py，创建一个全局对象myRadio

myRadio = Radio()
在//TODO处分别调用myRadio的play,stop方法，就可以通过接口控制播放停止了。

最后，部署到树莓派上，需要指定host为'0.0.0.0',否则其他机器无法访问：

app.run(host='0.0.0.0',port=80)
客户端接口调用
接口代码完成后，客户端展示就可以随意发挥了，只是需要注意因为没有部署到外网，请求路径应该是这种形式，后面的xxx是树莓派的内网ip地址：

http://192.168.xxx,xxx/radio/play
http://192.168.xxx,xxx/radio/stop
