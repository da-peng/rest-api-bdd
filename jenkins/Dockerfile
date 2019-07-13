FROM jenkins/jenkins:lts
USER root
RUN whoami
RUN apt-get update && apt-get install -y vim
RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
RUN echo '#!/bin/bash ' > /etc/profile.d/pyenv.sh
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> /etc/profile.d/pyenv.sh
RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> /etc/profile.d/pyenv.sh
RUN echo 'eval "$(pyenv init -)"' >> /etc/profile.d/pyenv.sh
RUN chmod 755  /etc/profile.d/pyenv.sh
RUN exec $SHELL
# RUN source /etc/profile.d/pyenv.sh
RUN . /etc/profile.d/pyenv.sh
RUN pyenv versions
# https://github.com/pyenv/pyenv/wiki
RUN apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
RUN pyenv install 3.7.2
RUN pyenv versions
USER jenkins

#RUN pyenv versions
# drop back to the regular jenkins user - good practice

# https://bbs.testerhome.com/topics/11935
# -u：用户名 0 root用户
# 1. sudo docker run -d -u 0 -p 8080:8080 -p 50000:50000 -v /Users/grabbywu/jenkins_home:/var/jenkins_home jenkins/wxp
# 2. apt-get update && apt-get install -y vim
# 3. curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer
#
# docker build  jenkins/wxp/  -t jenkins/wxp

# https://www.jianshu.com/p/830b0b7d449c

#    echo '#!/bin/bash ' > /etc/profile.d/pyenv.sh
#    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> /etc/profile.d/pyenv.sh
#    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> /etc/profile.d/pyenv.sh
#    echo 'eval "$(pyenv init -)"' >> /etc/profile.d/pyenv.sh
#    #刷新环境变量
#    chmod 755  /etc/profile.d/pyenv.sh
#    exec $SHELL
#    source /etc/profile.d/pyenv.sh
#    #显示pyenv 版本
#    pyenv versions

# https://bbs.testerhome.com/topics/11935
# sudo docker run -d -v /var/jenkins:/var/jenkins_home -u 0 -P --name bee_jenkins jenkins