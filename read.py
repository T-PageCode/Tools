try:
    print("==== 工具：TPC文件读取 ====")
    print("请输入你的文件路径。")
    filepath = input(">>> ")
    with open(filepath, "r", encoding="UTF-8") as userfile:
        readcontent = userfile.read()
        print(f"读取成功！文件内容: {readcontent}")
except Exception as catcherror:
    print(f"遇到了错误：{catcherror}")