import os

dir_path = 'html'
if not os.path.exists(dir_path):
    print("⚠️ 没找到 html 文件夹，请把脚本放在和 html 同级的目录！")
else:
    files = sorted([f for f in os.listdir(dir_path) if f.endswith('.html')])
    
    html_content = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>PySide6 文档索引</title>
    <style>
        body { font-family: sans-serif; padding: 40px; background: #f4f7f9; }
        .box { background: #fff; padding: 20px; border-radius: 10px; max-width: 800px; margin: 0 auto; }
        a { display: block; padding: 8px 0; text-decoration: none; color: #2c3e50; border-bottom: 1px solid #eee; }
        a:hover { background: #f0f0f0; padding-left: 10px; }
    </style>
</head>
<body>
<div class="box">
    <h1>PySide6 文档目录</h1>
'''
    for f in files:
        name = f.replace('.html', '').replace('PySide6-', '')
        html_content += f'    <a href="html/{f}">📄 {name}</a>\n'

    html_content += '''
</div>
</body>
</html>
'''
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("✅ 成功！index.html 已自动生成。")