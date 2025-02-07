# DEEPSEEK-R1-7B 自用1手5年前老笔记本即可畅玩
### 联系

1242105494@qq.com

B站 [点我🌲](https://space.bilibili.com/22708035?spm_id_from=333.1007.0.0)

GITHUB [点我🐈‍⬛](https://github.com/pingban404)

### 环境

window

---

docker [https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module)

---

ollama [https://ollama.com/library/deepseek-r1:7b](https://ollama.com/library/deepseek-r1:7b)

---

### 参考
```bash
模型：deepseek-R1-7b
电脑配置：
CPU： cpu i7 1165g7
内存：16GB
显卡：集成显卡
存储：100g
操作系统：windows11
```

### 开始
1. 安装`ollama`

地址：[Ollama](https://ollama.com/)

2. 下载模型

打开命令行工具

`ollama pull deepseek-R1-7b`

模型挑选：[https://ollama.com/search](https://ollama.com/search)

3. 运行模型（Windows）(局域网访问)(报错就是已经在运行，无视这步)（如果需要局域网范围，则把这个服务停掉，运行下面指令）

`<font style="color:rgb(51, 51, 51);">$env:OLLAMA_HOST="http://0.0.0.0:11434"; ollama serve</font>`

<font style="color:rgb(51, 51, 51);">打开新的命令行工具（win+r输入powershell）输入以下指令</font><font style="color:rgb(51, 51, 51);">👇</font>

`<font style="color:rgb(51, 51, 51);"> </font>ollama run deepseek-R1-7b`<font style="color:rgb(51, 51, 51);"> </font>

4. 请求（详细API请参考[ollama/docs/api.md at main · ollama/ollama](https://github.com/ollama/ollama/blob/main/docs/api.md)）



```python
curl http://127.0.0.1:11434/api/generate -d '{
   "model": "deepseek-r1:7b",
   "prompt": "你好",
    "options": {
      "seed": 123
    }
 }'
```



### 可视化
本文使用open-webui [https://docs.openwebui.com/](https://docs.openwebui.com/)

直接docker运行

* WIN+R输入（powershell），输入指令👇

`docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main`


* 不用了记得关闭容器! 👇
```
docker ps 
docker stop 容器ID
```

访问[http://localhost:3000](http://localhost:3000)





