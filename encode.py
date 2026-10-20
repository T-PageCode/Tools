try:
    print("==== 工具：TPC编码 ====")
    print("请输入你要编码的内容。")
    content = input(">>> ")
    encoded_content = [ord(e) for e in content]
    print(f"编码成功！内容：{encoded_content}")
except Exception as catcherror:
    print(f"遇到了错误：{catcherror}")