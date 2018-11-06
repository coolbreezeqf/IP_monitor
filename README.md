### 环境
```shell
python3 -m venv py3
py3/bin/pip install -r requirements.txt
```

### 使用
修改 **config.ini** 文件中配置。
邮箱的密码一般不能直接使用登陆密码，需要去获取对应的授权码。
```shell
DIR_PATH=`pwd`
echo "*/10 * * * *	 $DIR_PATH/py3/bin/python $DIR_PATH/main.py >> $DIR_PATH/out.log 2>&1 &" > timing_monitor
crontab timing_monitor
```