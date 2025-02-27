#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import base64
import shutil
from pathlib import Path
import markdown
from bs4 import BeautifulSoup
import mimetypes

class MarkdownPackager:
    def __init__(self, index_path='index.md', output_dir='output'):
        self.index_path = index_path
        self.output_dir = output_dir
        self.processed_files = set()
        self.current_dir = os.path.dirname(os.path.abspath(index_path))
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 配置Markdown转换器
        self.md = markdown.Markdown(extensions=[
            'markdown.extensions.tables',
            'markdown.extensions.fenced_code',
            'markdown.extensions.toc'
        ])

    def embed_image(self, image_path):
        """将图片转换为base64编码"""
        try:
            abs_image_path = os.path.join(self.current_dir, image_path)
            if not os.path.exists(abs_image_path):
                return f"data:image/png;base64,无法找到图片:{image_path}"
            
            mime_type = mimetypes.guess_type(image_path)[0]
            if not mime_type:
                mime_type = 'image/png'
            
            with open(abs_image_path, 'rb') as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
                return f"data:{mime_type};base64,{img_data}"
        except Exception as e:
            print(f"处理图片时出错 {image_path}: {str(e)}")
            return f"data:image/png;base64,处理图片出错:{image_path}"

    def process_markdown(self, md_path):
        """处理单个Markdown文件"""
        if md_path in self.processed_files:
            return
        
        self.processed_files.add(md_path)
        
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 转换Markdown为HTML
            html_content = self.md.convert(content)
            
            # 使用BeautifulSoup处理HTML
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 处理图片
            for img in soup.find_all('img'):
                src = img.get('src', '')
                if src and not src.startswith('data:'):
                    img['src'] = self.embed_image(src)
            
            # 处理Markdown链接
            for link in soup.find_all('a'):
                href = link.get('href', '')
                if href.endswith('.md'):
                    # 将.md链接转换为.html
                    link['href'] = href.replace('.md', '.html')
                    # 递归处理链接的Markdown文件
                    linked_md_path = os.path.join(os.path.dirname(md_path), href)
                    if os.path.exists(linked_md_path):
                        self.process_markdown(linked_md_path)
            
            # 生成完整的HTML文档
            html_template = f"""
            <!DOCTYPE html>
            <html lang="zh-CN">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{soup.find('h1').text if soup.find('h1') else 'Markdown文档'}</title>
                <style>
                    body {{
                        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                        line-height: 1.6;
                        padding: 20px;
                        max-width: 800px;
                        margin: 0 auto;
                        color: #333;
                    }}
                    img {{
                        max-width: 100%;
                        height: auto;
                    }}
                    pre {{
                        background-color: #f5f5f5;
                        padding: 15px;
                        border-radius: 5px;
                        overflow-x: auto;
                    }}
                    code {{
                        font-family: Consolas, Monaco, 'Andale Mono', monospace;
                    }}
                    table {{
                        border-collapse: collapse;
                        width: 100%;
                        margin: 15px 0;
                    }}
                    th, td {{
                        border: 1px solid #ddd;
                        padding: 8px;
                        text-align: left;
                    }}
                    th {{
                        background-color: #f5f5f5;
                    }}
                    blockquote {{
                        margin: 0;
                        padding-left: 1em;
                        border-left: 4px solid #ddd;
                        color: #666;
                    }}
                </style>
            </head>
            <body>
                {str(soup)}
            </body>
            </html>
            """
            
            # 保存HTML文件
            output_path = os.path.join(self.output_dir, os.path.basename(md_path).replace('.md', '.html'))
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_template)
            
        except Exception as e:
            print(f"处理文件时出错 {md_path}: {str(e)}")

    def package_all(self):
        """开始打包处理"""
        try:
            print("开始处理Markdown文件...")
            self.process_markdown(self.index_path)
            print(f"处理完成！输出目录: {self.output_dir}")
            print(f"共处理了 {len(self.processed_files)} 个文件")
        except Exception as e:
            print(f"打包过程中出错: {str(e)}")

if __name__ == "__main__":
    packager = MarkdownPackager('index.md', 'output')
    packager.package_all()
