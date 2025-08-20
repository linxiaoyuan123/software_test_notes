"""
api指接口，scripts指测试脚本

模块的概念：
    每一个以 `.py` 结尾的Python.代码文件都是一个模块
    模块名同样也是一个标识符，需要符合标识符的命名规则
    在模块中定义的 `全局变量、函数、类` 都是提供给外界直接使用的 `工具`
    模块就好比是工具包，要想使用这个工具包中的工具，就需要先导入模块

模块的导入方式：
    1、import 导入
    2、from ... import 导入
    (若模块名字太长，可以使用import 模块名1 as 模块别名，给模块取个简单名字，以便使用)


包的概念：
    包：(Package)是一个包含多个模块的特殊目录
    目录下有一个特殊的文件_init_py
    包名的命名方式和变量名一致
    作用：python文件较多时，方便分目录管理维护(python Package)

导包的常用方式：
    #方式一
    import 包名.模块名
    包名.模块名.工具名
    # 方式二
    from 包名 import 模块名
    模块名.工具名
    # 方式三
    from 包名.模块名 import 工具名
    工具名
"""

#导入登陆函数
# from python函数.api.login import login
# 快捷导包 ctrl + alt + 空格
from python函数.api.login import login

#调用
print(login("13488888888"))

# 断言 assert(正确无反应，但错误会报错)
"""
断言：自动判断实际结果和预期结果
用法：
1、断言相等：assert 预期结果 == 实际结果
2、断言包含：assert 预期结果 in 实际结果  （只要返回值中包含有预期结果中的内容，则PASS）
结果：
通过PASS：不显示
失败FALL：报错并提示"AssertionError'
"""
assert "账号正确" == login("13488888888")

if __name__ == '__main__':
    assert "账号正确" == login("13488888888")
    assert "账号错误" == login("13466666666")
    assert "错误" in login("13466666666")