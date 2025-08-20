"""
Allure报告
    介绍
        能生成美观易读的报告
        支持多种开发语言，如java、python等
        能快速上手
    操作步骤
        生成测试结果文件(json文件)
        使用allure命令生成在线报告

    1、安装环境
        安装插件：pip install allure-pytest
        验证：pip show allure-pytest
        下载allure：https://github.com/allure-framework/allure2/releases(需要解压到纯英文的路径)
        添加环境变量：点开path，新增，将allure的bin路径复制进去
        确认是否成功添加：allure --version
    2、调整配置文件
        report文件夹没有会自动创建
        在pytest.ini文件里的添加--alluredir report
            #添加命令行参数
            addopts=-s --alluredir report
    3、生成测试报告
        运行测试脚本：pytest
        生成测试报告：allure serve report

"""