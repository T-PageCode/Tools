import os
try:
    print("==== 工具：TPC文件删除 ====")
    print("请输入你的文件路径。")
    filepath = input(">>> ")
    print("警告：文件会被永久删除，无法恢复！你确定删除此文件吗？")
    delask = input(">>> ")
    if delask == "确定":
        os.remove(filepath)
    else:
        print("你好像输入了无效内容，请重新输入。")
except PermissionError:
    print("文件正在被占用，请结束相关进程重试。")
except Exception as catcherror:
    print(f"遇到了错误：{catcherror}")