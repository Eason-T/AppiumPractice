# AppiumPractice

这是一个基于Appium的Python自动化测试项目，用于Android应用的UI自动化测试。

## 环境要求

### 必需环境
- **Python**: 3.6+ (推荐3.13+)
- **Node.js**: 20.19.0+ (Appium 3.0.1要求)
- **Android SDK**: 包含ADB工具
- **Android模拟器或真机**: 用于测试

### 系统环境
- macOS (当前测试环境)
- 已安装Homebrew包管理器

## 详细安装步骤

### 1. 安装Python和虚拟环境

```bash
# 检查Python版本
python3 --version

# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate
```

### 2. 安装Python依赖

```bash
# 在虚拟环境中安装依赖
pip install -r requirements.txt
```

### 3. 安装和配置Node.js

```bash
# 使用nvm管理Node.js版本
# 安装nvm (如果未安装)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# 重新加载终端或执行
source ~/.zshrc

# 安装并切换到Node.js 20.19.0
nvm install 20.19.0
nvm use 20.19.0

# 验证版本
node --version  # 应该显示 v20.19.0
```

### 4. 安装Appium

```bash
# 全局安装Appium
npm install -g appium@latest

# 验证安装
appium --version  # 应该显示 3.0.1

# 安装UiAutomator2驱动
appium driver install uiautomator2
```

### 5. 配置Android环境

```bash
# 检查ADB是否可用
adb --version

# 检查连接的设备
adb devices

# 如果使用模拟器，确保模拟器已启动
# 可以通过Android Studio AVD Manager启动模拟器
```

## 运行测试

### 1. 启动Appium服务器

```bash
# 在终端中启动Appium服务器
appium --log-level info

# 服务器将在 http://localhost:4723 运行
# 保持此终端窗口打开
```

### 2. 验证环境

```bash
# 检查Appium服务器状态
curl -s http://localhost:4723/status

# 检查Android设备连接
adb devices
```

### 3. 运行测试

```bash
# 激活虚拟环境
source venv/bin/activate

# 运行测试
python test.py
```

## 测试说明

### 当前测试功能
测试文件 `test.py` 包含以下功能：

1. **连接设备**: 连接到指定的Android模拟器 (emulator-5554)
2. **启动应用**: 打开Android设置应用
3. **元素定位**: 使用XPath查找"Battery"文本元素
4. **执行操作**: 点击Battery选项
5. **观察效果**: 等待2秒以便观察自动化效果
6. **清理资源**: 正确关闭应用和WebDriver连接

### 测试配置
```python
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',  # 使用当前运行的模拟器
    udid='emulator-5554',  # 指定设备ID
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)
```

## 运行示例

### 完整的运行流程

#### 1. 启动Appium服务器
```bash
$ appium --log-level info
[Appium] Welcome to Appium v3.0.1
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
[Appium] Available drivers:
[Appium]   - uiautomator2@2.40.0 (automationName 'UiAutomator2')
[Appium] Available plugins:
[Appium] No plugins have been installed. Use the "appium plugin" command to install plugins.
```

#### 2. 验证环境
```bash
# 检查Appium服务器状态
$ curl -s http://localhost:4723/status
{"value":{"ready":true,"message":"The server is ready to accept new connections","build":{"version":"3.0.1"}}}

# 检查Android设备
$ adb devices
List of devices attached
emulator-5554   device
```

#### 3. 运行测试
```bash
# 激活虚拟环境并运行测试
$ source venv/bin/activate
$ python test.py
```

#### 4. 测试输出示例
```
(venv) yishenchen@YishendeMacBook-Pro-2 AppiumPractice $ python test.py
.
----------------------------------------------------------------------
Ran 1 test in 6.023s

OK
```

### 测试执行过程

当测试运行时，您会看到以下自动化过程：

1. **模拟器启动设置应用** - Android设置界面自动打开
2. **查找Battery选项** - 应用自动滚动并定位到"Battery"文本
3. **点击Battery** - 自动点击进入电池设置页面
4. **等待观察** - 停留2秒让您观察自动化效果
5. **自动关闭** - 测试完成后自动关闭应用

### 成功运行的条件

✅ **Appium服务器运行中** - 端口4723可访问  
✅ **Android模拟器连接** - `adb devices`显示设备  
✅ **Python环境正确** - 虚拟环境激活，依赖已安装  
✅ **测试文件配置正确** - 设备ID和包名匹配  

### 预期结果

- **测试通过**: 显示 `OK` 和运行时间
- **无错误**: 没有异常或失败信息
- **自动化完成**: 模拟器中的设置应用按预期操作

## 故障排除

### 常见问题

1. **Node.js版本过低**
   ```
   错误: Node version must be at least ^20.19.0
   解决: 使用 nvm install 20.19.0 && nvm use 20.19.0
   ```

2. **找不到Android设备**
   ```
   错误: Could not find a connected Android device
   解决: 确保模拟器已启动，运行 adb devices 检查
   ```

3. **Appium服务器连接失败**
   ```
   错误: Connection refused
   解决: 确保Appium服务器正在运行，检查端口4723
   ```

4. **Python依赖安装失败**
   ```
   错误: externally-managed-environment
   解决: 使用虚拟环境: python3 -m venv venv && source venv/bin/activate
   ```

### 调试命令

```bash
# 检查所有服务状态
adb devices                    # 检查Android设备
curl http://localhost:4723/status  # 检查Appium服务器
ps aux | grep appium          # 检查Appium进程

# 查看详细日志
appium --log-level debug      # 启动Appium并显示详细日志
```

## 项目结构

```
AppiumPractice/
├── test.py              # 主测试文件
├── requirements.txt     # Python依赖
├── README.md           # 项目说明
└── venv/               # Python虚拟环境
```

## 下一步

- 添加更多测试用例
- 集成测试报告生成
- 添加页面对象模式
- 配置CI/CD流水线