try:
    import ast
    print("==== 工具：TPC解码 ====")
    print("请输入你要解码的内容。（警告：请输入列表并不要输入字母！示范：[100, 100, 100]）")
    content = input(">>> ")
    content = ast.literal_eval(content)
    decoded_content = "".join(chr(e) for e in content)
    print(f"解码成功！内容：{decoded_content}")
except Exception as catcherror:
    print(f"遇到了错误：{catcherror}")