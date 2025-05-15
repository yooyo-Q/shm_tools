# README

## 项目简介

### 中文
该项目包含了一些工具，用于通过共享内存进行数据传输。主要功能包括通过共享内存发送和接收视频帧、字符串和列表数据。`samples` 目录中的文件仅用于提供用法参考，并不是工程的核心部分。

### English
This project includes some tools for data transmission via shared memory. The main functionality includes sending and receiving video frames, strings, and list data through shared memory. The files in the `samples` directory are only for usage reference and are not the core part of the project.

## 安装

### 中文
1. 克隆仓库：
    ```bash
    git clone <仓库地址>
    ```
2. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```

### English
1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 使用方法

### 中文
1. 运行 `samples/send_demo.py` 文件：
    ```bash
    python samples/send_demo.py
    ```
2. 确保共享内存名称和数据格式正确。

### English
1. Run the `samples/send_demo.py` file:
    ```bash
    python samples/send_demo.py
    ```
2. Ensure the shared memory name and data format are correct.

## 文件结构

### 中文
- `samples/send_demo.py`: 示例脚本文件，用于演示如何发送数据到共享内存。
- `shm_tools/shmcom.py`: 包含共享内存通信的工具。

### English
- `samples/send_demo.py`: Sample script file demonstrating how to send data to shared memory.
- `shm_tools/shmcom.py`: Contains tools for shared memory communication.

## 贡献

### 中文
欢迎提交问题和贡献代码。请确保遵循项目的代码规范和提交指南。

### English
Feel free to submit issues and contribute code. Please make sure to follow the project's code standards and submission guidelines.

## 许可证

### 中文
该项目使用MIT许可证。

### English
This project is licensed under the MIT License.
