try:
    print("==== 工具：TPC文件写入 ====")
    print("请输入你的文件路径。（注意：此功能会直接覆盖写入，请在操作前备份文件。）")
    filepath = input(">>> ")
    print("请输入你要写入的内容。")
    content = input(">>> ")
    with open(filepath, "w", encoding="UTF-8") as userfile:
        userfile.write(content)
except Exception as catcherror:
    print(f"遇到了错误: {catcherror}")