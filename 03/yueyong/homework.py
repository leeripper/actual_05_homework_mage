#encoding: utf-8

'''
1.定义一个字典存储数据
    users = {}
    {'kk' : {'name': name,'age": age,'tel':tel},{}}
2.用户输入的三次，修改为一次，使用：分隔用户信息
3.查找的时候使用包含关系，name包含查找的字符串
'''
users = {}
user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|'
user_info_header = user_info_tpl.format('name','age','telephone')
while True:
    action = input('please input action(find/list/add/delete/update/exit):')
    if action == 'add':
        #增加用户
        user_txt=input('请输入用户信息（用户名：年龄：电话：)')
        name,age,tel = user_txt.split(':')
        if name in users:
            print('添加用户失败，原因是用户名已存在')
        else:
            users[name] = {'name': name, 'age' : age, 'tel' : tel }
            print('添加用户成功')
    elif action == 'delete':
        #删除用户
        name = input('请输入你要删除的用户名：')
        if name in users:
            del users[name]
            print('删除用户成功')
        else:
            print('删除用户失败，原因是用户不存在')
    elif action == 'update':
        #更新用户
        user_txt = input('请输入用户信息(用户名：年龄：电话：)')
        name,age,tel = user_txt.split(':')
        if name in users:
            users[name] = {'name':name,'age':age,'tel':tel}
            print('更新用户成功')
        else:
            print('更新用户失败，错误原因是用户不存在')
    elif action == 'find':
        #查找用户
        name = input('请输入你要查找的用户名:')
        for user in users.values():
                if user['name'].find(name) != -1:
                    print(user_info_header)
                    print(user_info_tpl.format(user['name'],user['age'],user['tel']))
                    is_exists = True

        if not is_exists:
            print('没有该用户信息')

    elif action == 'list':
        #列出所有用户
        print(user_info_header)
        for user in users.values():
            print(user_info_tpl.format(user['name'],user['age'],user['tel']))
    elif action == 'exit':
        #退出程序
        break
    else:
        print('输入错误')


