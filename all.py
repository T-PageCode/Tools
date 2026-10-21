import ast # 导入 ast 模块，用于解码时转换
import os # 导入 os 模块，用于删除文件
print("==== T-PageCode Tools ====")
def write_file(): # 定义写入文件工具函数
    try:
        # 输入/提示代码
        print("==== 工具：TPC文件写入 ====")
        print("请输入你的文件路径。（注意：此功能会直接覆盖写入，请在操作前备份文件。）")
        filepath = input(">>> ") # 不能加 replace 处理空格，进 Exception 至少比 Hello World 变成 HelloWorld 好
        print("请输入你要写入的内容。")
        content = input(">>> ")
        # 开始写入文件
        with open(filepath, "w", encoding="UTF-8") as userfile: # with 保证在发生错误时关闭操作从而防止内存泄漏
            userfile.write(content)
        print("写入成功！你可以使用读取工具来查看此文件。") # 提示用户使用读取工具验证
    except FileNotFoundError: # 文件不存在时容错
        print(f"你的路径（{filepath}）可能存在错误，请检查后重试。") # f 字符串可直接在字符串中嵌入变量的值
    except Exception as catcherror: # Exception 来捕获错误信息
        print(f"遇到了错误: {catcherror}") # 同理

def read_file(): # 同理
    try:
        print("==== 工具：TPC文件读取 ====")
        print("请输入你的文件路径。")
        filepath = input(">>> ")
        with open(filepath, "r", encoding="UTF-8") as userfile:
            readcontent = userfile.read() # 不能加 strip，如果用户本身写入的内容前后有空格，那么会被去掉导致用户产生疑惑
        print(f"读取成功！文件内容: {readcontent}")
    except FileNotFoundError:
        print(f"你的路径（{filepath}）可能存在错误，请检查后重试。")
    except Exception as catcherror:
        print(f"遇到了错误：{catcherror}")

def add_file():
    try:
        print("==== 工具: TPC文件追加 ====")
        print("请输入你的文件路径。(注意：此功能会直接追加写入，请在操作前备份文件。)")
        filepath = input(">>> ")
        print("请输入你要写入的内容。")
        content = input(">>> ")
        with open(filepath, "a", encoding="UTF-8") as userfile:
            userfile.write(content + "\n")
        print("追加成功！你可以使用读取工具来查看此文件。") # 同理
    except FileNotFoundError:
        print(f"你的路径（{filepath}）可能存在错误，请检查后重试。")
    except Exception as catcherror:
        print(f"遇到了错误：{catcherror}")

def encode():
    try:
        print("==== 工具：TPC编码 ====")
        print("请输入你要编码的内容。")
        content = input(">>> ")
        encoded_content = [ord(e) for e in content] # 生成列表，通过 ord 来编码
        print(f"编码成功！内容：{encoded_content}") # 显示编码后的内容
    except Exception as catcherror:
        print(f"遇到了错误：{catcherror}")

def decode():
    try:
        print("==== 工具：TPC解码 ====")
        print("请输入你要解码的内容。（警告：请输入列表并不要输入字母！示范：[100, 100, 100]）")
        content = input(">>> ")
        content = ast.literal_eval(content) # 使用 ast 将字符串转为列表
        decoded_content = "".join(chr(e) for e in content) # join 去掉括号和逗号，chr 用来解码
        print(f"解码成功！内容：{decoded_content}") # 同理，但显示的是解码后的内容
    except ValueError: # 判断 ValueError 错误，如输入的数字过大或过小
        print("你输入的数字好像有问题，请重新输入合法的数字。")

    except SyntaxError: # 判断 SyntaxError 错误，如输入了字母或其他字符
        print("你输入的文本好像存在错误，请输入列表形式的数字重试。")

    except Exception as catcherror:
        print(f"遇到了错误：{catcherror}")

def delete():
    try:
        print("==== 工具：TPC文件删除 ====")
        print("请输入你的文件路径。").replace(" ", "") # 防手滑
        filepath = input(">>> ")
        print("警告：文件会被永久删除，无法恢复！你确定删除此文件吗？") # 警告
        delask = input(">>> ") # 确认
        if delask == "确定":
            os.remove(filepath) # 删除文件

        if delask == "取消":
            print("取消成功！")
        else:
            print("你好像输入了无效内容，请重新输入。")

    except FileNotFoundError:
        print(f"你的路径（{filepath}）可能存在错误，请检查后重试。")

    except PermissionError:
        print("文件正在被占用，请结束相关进程重试。") # 文件占用提示
        
    except Exception as catcherror:
        print(f"遇到了错误：{catcherror}")

def exit_tools():
    # 确认提示
    print("你确定要退出吗？（输入“确定”退出，“取消”不退出）")
    ask = input(">>> ").replace(" ","") # 删除空格，避免用户输入时手滑导致进了 else
    # 确认代码逻辑
    if ask == "确定":
        print("正在退出，感谢你的使用！")
        return "exit" # exit 字符串来给 if 传递信息，但不是 Python 的 exit 函数

    elif ask == "取消":
        print("取消成功！")
        return "none" # 返回 none，elif 里会直接忽略，但不是 Python 的 None 函数

    else: # else 为前面的判断都不是的时候进行的最终判断
        print("你好像输入了无效内容，请重新输入。") # 打印容错提示
        return "none" # 同理

# 通过 while True 无限循环来实现程序循环运行
while True:
    # print 提示
    print("请输入1 ~ 6数字来进行以下操作：\n1.写入文件\n2.读取文件\n3.追加文件\n4.编码\n5.解码\n6.删除\n7.退出")
    input_number = input(">>> ").replace(" ","") # 防手滑同理
    # 接下来开始一个一个的判断
    if input_number == "1":
        write_file()

    elif input_number == "2":
        read_file()

    elif input_number == "3":
        add_file()

    elif input_number == "4":
        encode()

    elif input_number == "5":
        decode()
    elif input_number == "6":
        delete()

    elif input_number == "7":
        if exit_tools() == "exit":
            break # 终止 while True 循环，等于退出程序

    # else 同理
    else:
        print("你好像输入了无效内容，请重新输入。")