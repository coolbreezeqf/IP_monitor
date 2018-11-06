### 环境
```shell
python3 -m venv py3
py3/bin/pip install -r requirements.txt
```

### 使用
修改 **timing_monitor** 文件中的路径和时间
```shell
sed -i "s#DIR_PATH#`pwd`#g" timing_monitor
corntab timing_monitor
```