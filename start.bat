@echo off

rem 进入到前端项目文件夹
cd client

echo Building front-end...
rem 安装需要的包
npm install

rem 打包前端项目
npm run build

cd ..

echo Running Flask server...
rem 安装后端所需的包
pip install -r requirements.txt

rem 运行 Flask 服务器
python server.py

pause