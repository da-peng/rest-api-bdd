#!/bin/bash
# 1.第一个参数为 环境 env 第二个参数 需要执行的features 列表
if [[ ! -n $1 ]]&&[[ ! -n $2 ]]; then
    echo "please input env and features"
    exit 1
fi

## 2.当前目录切换python 环境，如果在本地调试，不需要这一步
#. /etc/profile.d/pyenv.sh
#python --version
#pyenv local 3.7.2
#python --version
# 3.导入环境变量
if [ "$1" = "test" ]; then
    export TestEnv='test'
elif [ "$1" = "uat" ]; then
    export TestEnv='uat'
else
    echo "please input test or uat"
    exit 1
fi
# 4.移除旧的报告文件夹
if [ -d allure_results ]; then
   rm -rf allure_results
fi

# 5.运行测试
for i in $2
do
  behave -f allure_behave.formatter:AllureFormatter -o allure_results $i --tags=$1
done